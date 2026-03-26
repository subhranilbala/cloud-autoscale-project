#!/bin/bash

echo "Creating EC2 instance..."

aws ec2 run-instances \
  --image-id ami-0f559c3642608c138 \
  --count 1 \
  --instance-type t3.micro \
  --key-name vccassignmentkey \
  --security-group-ids sg-090eeb19ef28cf44b \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=AutoScaledVM}]'
