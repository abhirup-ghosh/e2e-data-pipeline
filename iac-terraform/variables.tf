variable "credentials" {
  description = "Google Application Credentials"
  default     = "~/.gc/gcp_service_capstone.json"
}

variable "project" {
  description = "GCP Project ID"
  default     = "e2e-data-pipeline-capstone"
  type        = string
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default     = "europe-north1"
  type        = string
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "gcs_bucket_name" {
  description = "Storage Bucket Name"
  default     = "capstone_datalake"
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default     = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type        = string
  default     = "capstone_dataset"
}
