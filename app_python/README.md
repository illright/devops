# DevOps Lab 1 – Python version

Now with a visits counter!

## Running the application

Ensure you have Python 3.9 and [Pipenv](https://pipenv.pypa.io/en/latest/) installed.

1. Install dependencies:

   ```shell
   pipenv install
   ```

2. Start the application  
   In development mode:

   ```shell
   pipenv run dev
   ```

   In production mode:

   ```shell
   pipenv run start
   ```

   Optionally you may pass `--host=...` and `--port=...` to change where
   the application will be listening for requests.
