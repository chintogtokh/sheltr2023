terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }

    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 3.0"
    }
  }
}

provider "cloudflare" {
  api_token = var.cloudflare_api_token
}

provider "aws" {
  region     = "ap-southeast-2"
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}

resource "aws_s3_bucket" "sheltr_bucket" {
  bucket = "${var.frontend_domain}.${var.root_domain}"
}

resource "aws_s3_bucket_website_configuration" "sheltr_bucket_website" {
  bucket = aws_s3_bucket.sheltr_bucket.id
  index_document {
    suffix = "index.html"
  }
  error_document {
    key = "index.html"
  }
}

resource "aws_s3_bucket_acl" "sheltr_bucket_acl" {
  bucket = aws_s3_bucket.sheltr_bucket.id
  acl    = "public-read"
}

resource "aws_s3_bucket_policy" "sheltr_bucket_bucket_policy" {
  bucket = aws_s3_bucket.sheltr_bucket.id
  policy = templatefile("${path.module}/s3_policy.json.tmpl", {
    frontend_domain = "${var.frontend_domain}.${var.root_domain}"
  })
}
