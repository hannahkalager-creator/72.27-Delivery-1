
## Notes - while doing the TP1

### Git Workflow**

This project follows a structured branching strategy to keep the codebase clean and avoid conflicts.

**Branch structure:**
```
main
└── develop
      ├── feature/grid-world
      ├── feature/bfs-dfs
      ├── feature/astar-heuristics
      └── feature/visualization
```

- `main` — stable, final version. Only updated when the project is complete.
- `develop` — active development branch. All features are merged here first.
- `feature/*` — one branch per feature. This is where day-to-day coding happens.

**When a feature is done:**
Open a Pull Request on GitHub from your `feature/` branch into `develop`. The rest of the team reviews and approves before merging.

**General rules:**
- Never commit directly to `main` or `develop`
- Commit often with descriptive messages
- Pull from `develop` regularly to stay up to date and avoid conflicts

