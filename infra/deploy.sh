#!/usr/bin/env bash
set -e
REGION="ap-south-1"
ARTIFACT_BUCKET="homemindai-artifacts-demo"
STACK_NAME="HomeMindAI-Infra"
aws cloudformation deploy --stack-name ${STACK_NAME} --template-file homemindai-infra.yaml --capabilities CAPABILITY_NAMED_IAM --region ${REGION} --parameter-overrides ArtifactBucketName=${ARTIFACT_BUCKET} ProjectSuffix=homemind
