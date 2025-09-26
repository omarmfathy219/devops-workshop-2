variable "aws_region" {
  description = "The AWS region where resources will be created."
  type        = string
  default     = "us-east-2"
}

variable "image_tag" {
  description = "The tag for the Docker image to be deployed."
  type        = string
  default     = "latest"
} 