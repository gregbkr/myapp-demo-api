#!/bin/bash
set -ex

ENV_NAME_ARG=$1
GITHUB_REPO=$2
GITHUB_TOKEN=$3

INFRA_STACK=${ENV_NAME_ARG}-api-infra

if ! aws cloudformation describe-stacks --stack-name ${ENV_NAME_ARG}-infra; then
    aws cloudformation deploy --stack-name ${INFRA_STACK} \
        --capabilities CAPABILITY_NAMED_IAM \
        --template-file ./main.yml \
        --parameter-overrides \
            GitHubRepo=${GITHUB_REPO} \
            GitHubToken=${GITHUB_TOKEN}
fi

echo "$(date):create:${ENV_NAME_ARG}:success"