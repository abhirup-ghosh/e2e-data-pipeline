# Terraform: Infrastructure as Code (IaC)

*We use terraform to construct our GCP resources: Google Cloud Storage Bucket: `capstone_datalake` and Google BigQuery Dataset: `capstone_dataset`.*

Pre-requisites: [Setup GCP project and VM](../notes/reproducibility.md).

```bash
$~> cd terraform
$~/terraform> terraform init
Initializing the backend...

Initializing provider plugins...
- Reusing previous version of hashicorp/google from the dependency lock file
- Installing hashicorp/google v5.22.0...
- Installed hashicorp/google v5.22.0 (signed by HashiCorp)

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

```bash
$~/terraform> terraform apply
.
.
.
google_bigquery_dataset.dataset: Creating...
google_storage_bucket.data-lake-bucket: Creating...
google_bigquery_dataset.dataset: Creation complete after 1s [id=projects/e2e-data-pipeline-capstone/datasets/capstone_dataset]
google_storage_bucket.data-lake-bucket: Creation complete after 3s [id=capstone_datalake]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```