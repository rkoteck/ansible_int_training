#!/bin/bash 

# uptime - used like an Ansible  module 
#
# must return JSON format (via stdout)
#
echo -e "{\"uptime\":\""$(uptime)"\"}"
