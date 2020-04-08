import json

# import requests


def hello(event, context):

  # more on CORS: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-integration-settings-integration-response.html
  return {
    "statusCode": 200,
    "headers": {
        "Access-Control-Allow-Origin": "*"
    },
    "body": json.dumps({
        "message": "hello world from Python Lambda !!",
    })
  }


def sum(event, context):

  sum = event['key1'] + event['key2']
  # more on CORS: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-integration-settings-integration-response.html
  return {
    "statusCode": 200,
    "headers": {
        "Access-Control-Allow-Origin": "*"
    },
    "body": json.dumps({
        "message": sum,
    })
  }
