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

variable "mongo_initdb_root_username" {
  description = "mongo_initdb_root_username"
  type        = string
  sensitive   = true
}

variable "mongo_initdb_root_password" {
  description = "mongo_initdb_root_password"
  type        = string
  sensitive   = true
}

variable "mongo_initdb_root_database" {
  description = "mongo_initdb_root_database"
  type        = string
  sensitive   = true
}

