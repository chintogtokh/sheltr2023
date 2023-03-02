## Infrastructure

Initialise a `.tfvars` file using the `.tfvars.example` and run the following.

```
terraform plan -var-file=".tfvars"
terraform apply -var-file=".tfvars"
```