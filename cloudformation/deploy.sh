#!/bin/bash
set -ex

ENV_NAME_ARG=$1
GITHUB_REPO=$2

# if ! aws cloudformation describe-stacks --stack-name ${ENV_NAME_ARG}-infra; then
    aws cloudformation deploy --stack-name ${ENV_NAME_ARG}-infra \
        --capabilities CAPABILITY_NAMED_IAM \
        --template-file ./main.yml \
        --parameter-overrides \
            GitHubRepo=${GITHUB_REPO}
# fi

echo "$(date):create:${ENV_NAME_ARG}:success"