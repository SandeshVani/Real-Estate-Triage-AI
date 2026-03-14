# 1. Telling Terraform to use AWS
provider "aws" {
  region = "ap-south-1"   # Mumbai region
}

# Creating an EC2 instance that will act as our server
resource "aws_instance" "real_estate_server" {

  # Using an Ubuntu machine image
  ami = "ami-0c7217cdde317cfec"

  # Small instance type (AWS Free Tier eligible)
  instance_type = "t2.micro"

  # Name tag for the instance
  tags = {
    Name = "Real-Estate-Production-Server"
  }
}
