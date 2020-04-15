import json

def lambda_handler(event, context):
  
  capitals={
      "france": "Paris", 
      "england": "London",
      "Spain": "Madrid"
  }

  #1. Parse out query string params
  country = event['queryStringParameters']['country']
  print('country=' + country)

  #2. find capital
  cap = capitals['france']
  print('Capital of france is: ' + cap)

  #3. Construct the body of the response object
  response = {}
  response['capital'] = cap

  #4. Construct http response object
  responseObject = {}
  responseObject['statusCode'] = 200
  responseObject['headers'] = {}
  responseObject['headers']['Access-Control-Allow-Origin'] = '*'
  responseObject['headers']['Content-Type'] = 'application/json'
  responseObject['body'] = json.dumps(response)

  #5. Return the response object
  return responseObject