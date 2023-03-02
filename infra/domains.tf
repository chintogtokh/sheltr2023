resource "cloudflare_record" "frontend_domain" {
  name    = var.frontend_domain
  value   = "${var.frontend_domain}.${var.root_domain}.s3-website-ap-southeast-2.amazonaws.com"
  type    = "CNAME"
  proxied = true
  zone_id = var.zone_id
}

data "aws_lb" "sheltr_backend_alb" {
  arn = aws_alb.sheltr_backend_alb.arn
}

resource "cloudflare_record" "backend_domain" {
  name    = var.backend_domain
  value   = data.aws_lb.sheltr_backend_alb.dns_name
  type    = "CNAME"
  proxied = true
  zone_id = var.zone_id
}

data "aws_lb" "mongo_elb" {
  name = aws_lb.mongo_elb.name
}

resource "cloudflare_record" "mongo_domain" {
  name    = var.mongo_domain
  value   = data.aws_lb.mongo_elb.dns_name
  type    = "CNAME"
  proxied = false
  zone_id = var.zone_id
}
