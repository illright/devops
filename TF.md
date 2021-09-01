# Terraform best practices

- The resources are given meaningful names
- The lockfile and the state are checked into Git
- Variables store common and changeable values
- AWS credentials must be supplied from the outside to avoid key leakage
- Different kinds of entities are stored in different files
- Outputs provide useful information for DevOps engineers
