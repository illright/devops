# Docker best practices

- Multi-stage build for the TypeScript app allows avoiding
  the installation of `pnpm` and compiling dependencies.
- The images are based on Alpine Linux, which provides
  a very slim container
- The Dockerfiles are linted
- The parts of the Dockerfile that rarely change are pushed up
  to enable successful caching of layers
- A running command is available in every Dockerfile
