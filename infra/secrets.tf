variable "aws_access_key" {
    description = "aws_access_key"
    type        = string
    sensitive   = true 
}

variable "aws_secret_key" {
    description = "aws_secret_key"
    type        = string
    sensitive   = true 
}

variable "cloudflare_api_token" {
    description = "cloudflare_api_token"
    type        = string
    sensitive   = true 
}