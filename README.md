# DevOps Lab 1

A web application that simply shows the current time in Moscow.

There are two versions:

- in Python (using [Sanic](https://sanicframework.org/) as the backend)  
  See the [development decisions](./app_python/PYTHON.md)
  for the Python project.
- in TypeScript (using [Svelte](https://svelte.dev)
  as the interface framework)  
  See the [development decisions](./app_ts/TYPESCRIPT.md)
  for the TypeScript project.

## Linting the project

You may lint the formatting and Markdown in both versions of the app
with `pnpm` from the root directory:

```shell
pnpm lint
```

To lint the Python code in `app_python`, run the following command
from the `app_python/` directory:

```shell
pipenv run lint
```

To lint the TypeScript/Svelte code in `app_ts`, run the following
command from the `app_ts/` directory:

```shell
pnpm lint
```

## Credits

This project is created by Lev Chelyadinov (B18-SE-01).

## License

This project is [MIT licensed](./LICENSE).