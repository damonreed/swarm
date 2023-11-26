#
# swarm_mon - main.tf 
#

terraform {
 backend "gcs" {
   bucket  = "swarm_mon_tfstate"
   prefix  = "terraform/state"
 }
}

provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

resource "google_storage_bucket" "swarm_mon_tfstate" {
  name          = "swarm_mon_tfstate"
  force_destroy = false
  location      = "US"
  storage_class = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }
}

resource "google_compute_network" "main" {
  name                    = "main"
  auto_create_subnetworks = false
  mtu                     = 1460
}

resource "google_compute_subnetwork" "default" {
  name          = "default"
  ip_cidr_range = "10.0.1.0/24"
  network       = google_compute_network.main.id
}

# Create a single Compute Engine instance
resource "google_compute_instance" "flask-vm" {
  name         = "flask-vm"
  machine_type = "e2-micro"
  tags         = ["ssh"]

  boot_disk {
    initialize_params { image = "debian-cloud/debian-11" }
  }

  # Install Flask
  metadata_startup_script = "sudo apt-get update; sudo apt-get install -yq build-essential python3-pip rsync; pip install flask"

  network_interface {
    subnetwork = google_compute_subnetwork.default.id
    access_config {}
  }
}

resource "google_compute_firewall" "flask" {
  name    = "flask-app-firewall"
  network = google_compute_network.main.id

  allow {
    protocol = "tcp"
    ports    = ["5000"]
  }
  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_firewall" "ssh" {
  name = "allow-ssh"
  allow {
    ports    = ["22"]
    protocol = "tcp"
  }
  direction     = "INGRESS"
  network       = google_compute_network.main.id
  priority      = 1000
  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["ssh"]
}

