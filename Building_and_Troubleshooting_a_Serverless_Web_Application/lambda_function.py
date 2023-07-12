import json
import boto3
import random

client = boto3.client('dynamodb')

def lambda_handler(event, context):

  data = client.get_item(
    TableName='fortunes',
    Key={
        'fort_id': {
          'N': str(random.randint(1,16))
        }
        },
        ProjectionExpression='fortune'
    )

  json_string = json.dumps(data)
  resp_dict=json.loads(json_string)
  fort_string=json.dumps(resp_dict['Item'])
  fort_dict=json.loads(json.dumps(json.loads(fort_string)['fortune']))

  response = {
      'statusCode': 200,
      'headers': {
        'Access-Control-Allow-Origin': '*',
      },
      'body': json.dumps(fort_dict['S'])

  }
  
  return response
