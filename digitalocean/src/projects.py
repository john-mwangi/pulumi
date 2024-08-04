import pulumi_digitalocean as do
from dotenv import load_dotenv
from src.buckets import create_bucket
from src.databases import create_postgres_db_cluster
from src.droplets import create_droplet, resize_droplet
from src.options import opts

load_dotenv()

droplet = do.Droplet(
    resource_name="jmwangi-vm",
    name="jmwangi-vm",
    opts=None,
    backups=True,
    graceful_shutdown=True,
    image="ubuntu-22-04-x64",
    region=do.Region.AMS3,
    size="s-2vcpu-4gb",
    user_data="""#!/bin/bash

    sudo ufw allow https
    sudo ufw allow https
    sudo ufw allow OpenSSH

    curl -fsSL https://get.docker.com/ | sh
    
    """,
)

project = do.Project(
    resource_name="jmwangi-project",
    description="A project to represent development resources",
    environment="development",
    name="john-mwangi",
    purpose="development",
    resources=[droplet.droplet_urn],
)