#!/bin/bash
set -ex

ENV_NAME_ARG=$1
BRANCH=$2

BUCKET=${ENV_NAME_ARG}-infra
SAM_STACK=${ENV_NAME_ARG}-sam-${BRANCH}

sam build --parameter-overrides \
    ParameterKey=ApiName, ParameterValue=${SAM_STACK}
    ParameterKey=Branch, ParameterValue=${BRANCH}

sam package --output-template-file packaged.yaml --s3-bucket ${BUCKET}
sam deploy --template-file packaged.yaml --stack-name ${SAM_STACK} --s3-bucket ${BUCKET} --capabilities CAPABILITY_IAM --region eu-west-1

echo "$(date):create:${SAM_STACK}:success"