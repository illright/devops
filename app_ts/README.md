# DevOps Lab 1 – TypeScript version

## Running the application

Ensure you have Node 8+ and [`pnpm`](https://pnpm.io) installed.

1. Install dependencies:

   ```shell
   pnpm i
   ```

2. Start the application  
   In development mode:

   ```shell
   pnpm dev
   ```

   In production mode:

   ```shell
   pnpm build
   pnpm start
   ```

   Optionally you may pass `--host ...` and `--port ...` after an extra `--`
   (`pnpm start -- --port 8080`) to change where the application will
   be listening for requests.
