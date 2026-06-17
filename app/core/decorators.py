# myapp/decorators.py
from django.conf import settings

if settings.DEBUG:  # noqa: C901
    from drf_spectacular.utils import OpenApiExample
    from drf_spectacular.utils import OpenApiParameter
    from drf_spectacular.utils import OpenApiTypes
    from drf_spectacular.utils import extend_schema
    from drf_spectacular.utils import extend_schema_view
else:
    # No-op decorators and classes for production
    def extend_schema_view(**kwargs):
        def decorator(cls):
            return cls

        return decorator

    def extend_schema(**kwargs):
        def decorator(fn):
            return fn

        return decorator

    class OpenApiParameterMeta(type):
        def __getattr__(cls, name):
            return None

    class OpenApiParameter(metaclass=OpenApiParameterMeta):
        def __init__(self, *args, **kwargs):
            pass

    class OpenApiExample:
        def __init__(self, *args, **kwargs):
            pass

    class OpenApiTypesMeta(type):
        def __getattr__(cls, name):
            return None

    class OpenApiTypes(metaclass=OpenApiTypesMeta):
        pass
