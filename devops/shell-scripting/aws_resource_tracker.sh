#!/bin/bash

# AWS Resource Tracker

echo "AWS Resource Report"
echo "==================="

# S3 Buckets
echo ""
echo "S3 Buckets:"
aws s3 ls

# EC2 Instances
echo ""
echo "EC2 Instances:"
aws ec2 describe-instances \
  --query "Reservations[*].Instances[*].[InstanceId,State.Name]" \
  --output table

# Lambda Functions
echo ""
echo "Lambda Functions:"
aws lambda list-functions \
  --query "Functions[*].[FunctionName]" \
  --output table

# IAM Users
echo ""
echo "IAM Users:"
aws iam list-users \
  --query "Users[*].[UserName]" \
  --output table

echo ""
echo "Report Complete!"