# Use a base image
FROM ubuntu:latest

# Install required dependencies
RUN apt-get update && apt-get install -y wget unzip

# Download and install Terraform
RUN wget https://releases.hashicorp.com/terraform/1.0.0/terraform_1.0.0_linux_amd64.zip \
    && unzip terraform_1.0.0_linux_amd64.zip \
    && mv terraform /usr/local/bin/

# Set the working directory
WORKDIR /app

# Copy your Terraform files into the container
COPY . /app

# Set an environment variable for Terraform
ENV TF_LOG=INFO

# Run Terraform commands
CMD ["terraform", "--version"]
