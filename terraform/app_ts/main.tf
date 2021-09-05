variable "aws_access_key_id" {
  description = "The access key ID for the AWS API"
  type        = string
}

variable "aws_access_key_secret" {
  description = "The access key secret for the AWS API"
  type        = string
}

provider "aws" {
  region     = "us-east-1"
  access_key = var.aws_access_key_id
  secret_key = var.aws_access_key_secret
}

variable "ami_id" {
  description = "The ID of the desired image for the server"
  type        = string
}

variable "keypair_name" {
  description = "The name of the keypair to add to an EC2 instance"
  type        = string
}

variable "setup_script" {
  description = "A script to run on instance initialization"
  type        = string
}

resource "aws_instance" "moscow-time-server" {
  ami             = var.ami_id
  instance_type   = "t2.micro"
  key_name        = var.keypair_name
  user_data       = var.setup_script
  security_groups = [aws_security_group.allow-web-ssh.name]

  tags = {
    Name = "Moscow Time Server"
  }
}

output "Server-URL" {
  value = "http://${aws_instance.moscow-time-server.public_dns}"
}

output "SSH-command" {
  value = "ssh -i ~/.ssh/${var.keypair_name}.pem ubuntu@${aws_instance.moscow-time-server.public_dns}"
}
