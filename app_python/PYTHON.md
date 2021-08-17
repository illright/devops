# Best practices for a Python web application

## Framework

- The application is written using Sanic
  - It is lightweight, and therefore, well-suited for a small application
    like this one.
  - It is very performant due to its asynchronous nature.
  - It is production-ready.
  - It comes with a built-in production-grade web server so no extra
    dependencies are needed.
  - The whole application is just 16 lines of well-formatted code.

## Package manager

- This project uses Pipenv to manage dependencies and scripts
  for running the application.
- Pipenv uses virtual environments which prevents version conflicts
- The dependencies are bounded to exclude major version upgrades,
  which ensures the dependencies do not introduce any breaking
  changes upon updates, but the security fixes and new features still get installed.
- The lockfile is checked into version control to ensure reproducible builds
  locally and in CI.
- Two running scripts are available: to run the app in development 
  and production modes.

## Linting

- The project is linted with PyLint.
- A script is available to run the linter.

## Readme

- The README contains the instructions for running the application.
