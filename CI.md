# Continuous integration best practices

## GitHub Actions

- Only run on pushes to `main`
- Cache the installed dependencies
- Run linting and testing on the CI server to ensure code quality
- Use the latest Ubuntu for GitHub Actions

## Jenkins

- The pipeline is stored in version control
- Linting and testing is done in parallel
