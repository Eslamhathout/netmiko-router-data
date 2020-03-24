# netmiko-router-data

## Description: 
A project to retrieve router info such as:
*Hostname
*Model
*Uptime of each device
*Current software version
*Device serial number
*MAC address for each active Ethernet interface

## Installation:
To start using the attached script, you need to setup Python, GNS3, and Netmiko. Here are a list of commands to assest installation:

*apt-get update
apt-get install software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get install python3.7
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3.7 get-pip.py
pip3 install cryptography
pip3 install paramiko
pip3 install netmiko*

## Usage: 
To use the attached script, you need to build a simple network on GNS3 and use a Docker Ubuntu image to send the file's commands to the router.
