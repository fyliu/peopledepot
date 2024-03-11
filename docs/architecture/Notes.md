# Troubleshooting

## ModHeader

- ModHeader will break Google drive if Authentication Bearer token is set. The Google drive website pops up a dialog saying:

    ```text
    "You are not signed in.
    You are signed out. Sign back in, then click 'Retry'.
    Retry"
    ```

    The solution is to disable the Authentication header and Google drive will work as normal.

## Git graphs

### Feature branch and merge

```mermaid
gitGraph
   commit
   commit
   branch feature
   checkout feature
   commit
   commit
   checkout main
   merge feature
   commit
   commit
```

### Feature branches and merge

```mermaid
---
config:
  gitGraph:
    parallelCommits: true
---
gitGraph:
   commit
   commit
   branch feature
   checkout feature
   commit
   commit
   checkout main
   commit
   branch feature2
   checkout feature2
   commit
   checkout main
   merge feature
   commit
   commit
   checkout feature2
   merge main
    checkout main
    merge feature2
```
