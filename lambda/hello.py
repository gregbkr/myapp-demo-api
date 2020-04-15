import json

def lambda_handler(event, context):

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
