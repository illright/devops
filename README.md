# DevOps Lab 1

[![Lint and test on pushes](https://github.com/illright/devops/actions/workflows/lint-test-on-push.yaml/badge.svg)](https://github.com/illright/devops/actions/workflows/lint-test-on-push.yaml)

A web application that simply shows the current time in Moscow.

There are two versions:

- in Python (using [Sanic](https://sanicframework.org/) as the backend)  
  See the [development decisions](./app_python/PYTHON.md)
  for the Python project.
- in TypeScript (using [Svelte](https://svelte.dev)
  as the interface framework)  
  See the [development decisions](./app_ts/TYPESCRIPT.md)
  for the TypeScript project.

## Deploying the project to AWS

### Create a server

Make sure you have Terraform installed on your machine.

You will need to [create an access key](https://console.aws.amazon.com/iam/home#/security_credentials) for AWS. Use it to set the following environment variables:

- `TF_VAR_aws_access_key_id` – the AWS access key ID
- `TF_VAR_aws_secret_access_key` – the AWS access key secret

You will also need to [create an SSH keypair](https://console.aws.amazon.com/ec2/v2/home#KeyPairs:) in the AWS management console for SSH access to your server. We will use the name `main` and you can, too, but if you want a different name, make sure to use that name in the `keypair_name` variable in the `terraform/app_ts/terraform.tfvars` file.  
We will store the downloaded `main.pem` private key file in the `~/.ssh`, directory and you can, too, but if you want to store it somewhere else, pay attention later when we get to Ansible.

In the `terraform/app_ts` directory, run the following commands:

```bash
terraform init
terraform apply
```

This will spin up an EC2 instance of a `t2.micro` tier.

### Deploy the application to the server

Make sure you have Python 3 and Ansible installed on your machine.

Install (or verify the presence of) these Python packages:

- `boto3`
- `botocore`

Install (or verify the presence of) these Ansible packages:

- `ansible-galaxy collection install amazon.aws`
- `ansible-galaxy collection install community.docker`
- `ansible-galaxy install geerlingguy.docker`

Set the following environment variables:

- `AWS_ACCESS_KEY_ID` – the same value as `TF_VAR_aws_access_key_id`
- `AWS_SECRET_ACCESS_KEY` – the same value as `TF_VAR_aws_secret_access_key`

In the `ansible/playbooks` directory, run the following commands:

```bash
ansible-playbook playbooks/prepare-for-deployment.yaml --key-file ~/.ssh/main.pem
```

If you picked a different name/location for your EC2 keypair file, update the `--key-file` argument in the command above accordingly.

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

## Docker images

[![Python container](https://img.shields.io/docker/image-size/illright/devops_lab1_python/1.1.1?label=Python%20container)](https://hub.docker.com/r/illright/devops_lab1_python)
[![TypeScript container](https://img.shields.io/docker/image-size/illright/devops_lab1_ts/1.0.1?label=TypeScript%20container)](https://hub.docker.com/r/illright/devops_lab1_ts)

Both containers serve the applications on `0.0.0.0:3000`.

## Unit tests

The Python application contains a test suite. You may run it with:

```shell
pipenv run test
```

## Authors

This project is created by Lev Chelyadinov (B18-SE-01).

## License

This project is [MIT licensed](./LICENSE).
