resource "cloudflare_record" "frontend_domain" {
  name    = var.frontend_domain
  value   = "${var.frontend_domain}.${var.root_domain}.s3-website-ap-southeast-2.amazonaws.com"
  type    = "CNAME"
  proxied = true
  zone_id = var.zone_id
}
