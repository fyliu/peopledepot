from datetime import datetime
from zoneinfo import ZoneInfo

from dateutil.rrule import WEEKLY
from django.test import TestCase
from recurrence import MONDAY
from recurrence import Rule

from core.models import Event
from core.models import Project


class RecurringEventTestCase(TestCase):
    def setUp(self):
        self.tz = ZoneInfo("America/Los_Angeles")
        self.project = Project.objects.create(name="Test Project")

    def test_create_recurring_event_at_6pm(self):
        """Test that a recurring event is created at 6pm local time."""
        start_dt = datetime(2026, 9, 1, 18, 0, 0, tzinfo=self.tz)

        event = Event.objects.create(
            name="Team Standup",
            start_time=start_dt,
            timezone="America/Los_Angeles",
            project=self.project,
        )

        # Assertions
        self.assertEqual(event.name, "Team Standup")
        self.assertEqual(event.start_time.hour, 18)
        self.assertEqual(event.start_time.minute, 0)
        self.assertEqual(event.timezone, "America/Los_Angeles")

    def test_recurring_event_occurrences_are_6pm(self):
        """Test that all occurrences happen at 6pm local time."""
        start_dt = datetime(2026, 9, 1, 18, 0, 0, tzinfo=self.tz)

        event = Event.objects.create(
            name="Team Standup",
            start_time=start_dt,
            timezone="America/Los_Angeles",
            project=self.project,
        )

        rule = Rule(WEEKLY, byday=MONDAY)
        event.recurrence.rrules.append(rule)
        event.save()

        # Get occurrences over 3 months
        dtstart = datetime(2026, 9, 1, 18, 0, 0, tzinfo=self.tz)
        dtend = datetime(2026, 12, 1, 18, 0, 0, tzinfo=self.tz)
        occurrences = event.recurrence.occurrences(dtstart=dtstart, dtend=dtend)

        # Verify each occurrence is at 6pm
        occurrences_list = list(occurrences)
        self.assertGreater(len(occurrences_list), 0)

        for occ in occurrences_list:
            self.assertEqual(occ.hour, 18, f"Occurrence {occ} is not at 6pm")
            self.assertEqual(occ.minute, 0)

    def test_recurring_event_handles_dst_transition(self):
        """Test that occurrences remain at 6pm through DST transitions."""
        # Create event in summer (PDT)
        start_dt = datetime(2026, 6, 1, 18, 0, 0, tzinfo=self.tz)

        event = Event.objects.create(
            name="Team Standup",
            start_time=start_dt,
            timezone="America/Los_Angeles",
            project=self.project,
        )

        rule = Rule(WEEKLY, byday=MONDAY)
        event.recurrence.rrules.append(rule)
        event.save()

        # Get occurrences spanning DST transition (Nov 2)
        dtstart = datetime(2026, 9, 1, 18, 0, 0, tzinfo=self.tz)
        dtend = datetime(2026, 12, 1, 18, 0, 0, tzinfo=self.tz)
        occurrences = event.recurrence.occurrences(dtstart=dtstart, dtend=dtend)

        occurrences_list = list(occurrences)
        self.assertGreater(len(occurrences_list), 0)

        # All should be at 6pm local time
        for occ in occurrences_list:
            self.assertEqual(occ.hour, 18)
            # print UTC time for debugging
            print(f"Occurrence {occ} is at {occ.astimezone(ZoneInfo('UTC'))}")
