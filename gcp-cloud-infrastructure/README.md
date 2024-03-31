# Google Cloud Platform: Cloud infrastructure

*We build our end-to-end data pipeline that visualises football data using the cloud, specifically, tools and infrastructure from the Google Cloud Platform. For that, we first setup our Google Project, service accounts, and our virtual machine (VM). We also setup a connection to our local machine, as well as to our project github repository.*

## Setup GCP Project and Service Accounts

* GCP project
  * Go to: https://console.cloud.google.com/
  * Create a 'New Project':
    * Project number: 1021722663072 
    * Project ID: `e2e-data-pipeline-capstone`

* IAM & Admin --> Service Accounts [Follow instructions in video: [DE Zoomcamp 1.3.2 - Terraform Basics](https://youtu.be/Y2ux7gq3Z0o?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)]
  * Go to: https://console.cloud.google.com/iam-admin/serviceaccounts
  * Create service account with:
    * Details: `terraform-runner`
    * Permissions: **Storage Admin**, **BigQuery Admin**, **Compute Admin**
  * Generate private key (json) for `terraform-runner` and save it locally under: `~/.gc/gcp_service_capstone.json`

## Setup GCP Compute Engine/VM Instance 

[Follow instructions in video: [DE Zoomcamp 1.4.1 - Setting up the Environment on Google Cloud (Cloud VM + SSH access)](https://youtu.be/ae-CV2KfoN0?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb) or the markdown page: [2_gcp_overview.md](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/1_terraform_gcp/2_gcp_overview.md)]

[First time: `Enable` Compute Engine API &rarr; `Enable` Billing Account &rarr; select `My Billing Account`]

* Go to: https://console.cloud.google.com/compute
* **Create SSH Key pair** using the instructions [here](https://cloud.google.com/compute/docs/connect/create-ssh-keys).
  * Local Machine (MacOS): `ssh-keygen -t rsa -f ~/.ssh/gcp -C abhirup.ghosh -b 2048`
  * GCP Compute Engine: **Metadata** &rarr; **SSH Keys** &rarr; add content of (local machine): `cat ~/.ssh/gcp.pub` into SSH Key 1 and save
* **CREATE INSTANCE** with name `e2e-data-pipeline-capstone-vm` and specifications:
  * Region/Zone: `europe-north1 (Finland)`/`europe-north1-a` 🚨🚨 SUPER IMPORTANT
  * Machine configuration: `e2-standard-4` (4 vCPU, 2 core, 16GB memory)
  * Boot disk: 30GB Ubuntu 20.04 LTS (x86/64, amd64 focal image built on 2024-03-07)

* **sftp Google credentials** (`~/.gc/gcp_service_capstone.json` created above) to VM:

  ```bash
  $~> cd .gc
  $~/.gc> sftp capstone # on local machine
  sftp> mkdir .gc
  sftp> cd .gc
  sftp> put gcp_service_capstone.json
  Uploading gcp_service_capstone.json to /home/abhirup.ghosh/.gc/gcp_service_capstone.json
  gcp_service_capstone.json              100% 2404    46.1KB/s   00:00    
  ```

## Setup SSH into VM

* **SSH into VM** from local machine:

    ```bash
    $~> cd ${HOME}
    $~> EXTERNAL_IP="XX.XX.XXX.XXX"
    $~> ssh -i ~/.ssh/gcp abhirup.ghosh@${EXTERNAL_IP}

    Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-1053-gcp x86_64)
    .
    .
    .
    .
    abhirup.ghosh@e2e-data-pipeline-capstone-vm:~$ 
    ```

* **Setup local `~/.ssh/config`** with the following content for shortcut:

    ```vim
    Host = capstone
            Hostname XX.XX.XXX.XXX
            User abhirup.ghosh
            IdentityFile /Users/abhirupghosh/.ssh/gcp
    ```

    and later ssh into VM using:

    ```
    $~> ssh capstone
    ```

* **Enable ssh with VS Code** by installing **Remote-SSH** plugin and connecting to the remote host using the above configuration file. The instructions are [here](https://youtu.be/ae-CV2KfoN0?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&t=1073).

* Forward ports 6789 (Mage), 8888 (Jupyter), 4040 (pgadmin) and 8080 (spark) from VM to local machine.

## Setup environment on VM

### 1. Google Cloud SDK [comes pre-installed]

```bash
$~> gcloud --version
Google Cloud SDK 467.0.0
alpha 2024.02.29
beta 2024.02.29
bq 2.0.101
bundled-python3-unix 3.11.8
core 2024.02.29
gcloud-crc32c 1.0.0
gsutil 5.27
minikube 1.32.0
skaffold 2.9.0
```

**Google Cloud SDK Authentication**

After we have downloaded the key and put it to some location, e.g. `.gc/gcp_service_capstone.json`, we set `GOOGLE_APPLICATION_CREDENTIALS` to point to the file.

```bash
$~> export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/gcp_service_capstone.json
```

Now authenticate:

```bash
$~> gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
Activated service account credentials for: [terraform-runner@e2e-data-pipeline-capstone.iam.gserviceaccount.com]
```

### 2. Anaconda

```
$~> wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh
$~> bash Anaconda3-2024.02-1-Linux-x86_64.sh
```

This installs Anaconda under `/home/abhirup.ghosh/anaconda3` and should modify the `~/.bashrc` to change the default prompt.


### 3. Docker and docker-compose

**Docker**

Install docker using:
```bash
$~> sudo apt-get update
$~> sudo apt-get install docker.io
```

We need to be able to use Docker with sudo privileges. For that we follow the instructions here: https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md

and test using:
```bash
$~> docker run hello-world
.
.
.
Hello from Docker!
```

**docker-compose**

* Create folder called `bin` under `${HOME}`
* Download the latest release of docker-compose (Linux/x86_64 version) from https://github.com/docker/compose/releases
* Make it an executable
* Include `${HOME}/bin` in `${PATH}` but putting a statement in `~/.bashrc`

```bash
$~> mkdir bin
$~> cd bin
$~/bin> wget https://github.com/docker/compose/releases/download/v2.26.0/docker-compose-linux-x86_64 -O docker-compose
$~/bin> chmod +x docker-compose
$~/bin> cd
$~> export PATH="${HOME}/bin:${PATH}" >> ~/.bashrc
$~> . ~/.bashrc
$~> docker-compose --version
Docker Compose version v2.26.0
```

### Terraform

Download the latest AMD64 release of terraform from: https://developer.hashicorp.com/terraform/install#linux and install it (after unzipping) in the `${HOME}/bin` directory. Because of the line we added in our `~/.bashrc`, the executable automatically gets added to our `${PATH}` variable.

```bash
$~/bin> wget https://releases.hashicorp.com/terraform/1.7.5/terraform_1.7.5_linux_amd64.zip
$~/bin> sudo apt-get install unzip
$~/bin> unzip terraform_1.7.5_linux_amd64.zip
$~/bin> rm terraform_1.7.5_linux_amd64.zip 
```

## Clone Repository

First, one needs to create an SSH key pair between the VM and github.

```bash
$~> git clone git@github.com:abhirup-ghosh/e2e-data-pipeline.git
$~> cd e2e-data-pipeline
```

## Setup conda environment for testing

```bash
conda create --name e2e-data-pipeline python=3.10
conda activate e2e-data-pipeline
conda install numpy pandas scikit-learn seaborn jupyter
```

or else build the environment using the environment file:

```bash
conda env create -f res/environment.yml
```