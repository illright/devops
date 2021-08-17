# Best practices for a TypeScript web application

## Framework

- The application is written using Svelte
  - It is a compiler, so the application is very small and performant.
  - It is production-ready.

## Package manager

- This project uses `pnpm` to manage dependencies and scripts
  for running the application.
  - It is the fastest package manager for JS among the well-known ones.
  - It is highly efficient in terms of storage.
- The dependencies are bounded to exclude major version upgrades,
  which ensures the dependencies do not introduce any breaking
  changes upon updates, but the security fixes and new features still get installed.
- The lockfile is checked into version control to ensure reproducible builds
  locally and in CI.
- Three running scripts are available: to run the app in development,
  compile for production and start in production mode.

## Linting

- The project is linted with ESLint.
- Code formatting is ensured by Prettier.
- A script is available to run the linter.

## Readme

- The README contains the instructions for running the application.
