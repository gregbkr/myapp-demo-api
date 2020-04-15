import json

def lambda_handler(event, context):
  
  request_body = json.loads(event['body'])
  print(request_body)
  
  n1 = int( float( request_body['key1'] ))
  n2 = int( float( request_body['key2'] ))
  
  mysum = n1 + n2
  print(mysum)
  
  # more on CORS: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-integration-settings-integration-response.html
  return {
    "statusCode": 200,
    "headers": {
        "Access-Control-Allow-Origin": "*"
    },
    "body": json.dumps({
      "result": mysum
    })
  }
