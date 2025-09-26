output "load_balancer_dns" {
  description = "The DNS name of the Application Load Balancer."
  value       = aws_lb.app_lb.dns_name
} 