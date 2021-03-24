import boto3
import json

print('Loading function')
dynamo = boto3.client('dynamodb')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,GET'
        },
    }


def get_last_10(all_sensor_data):
    last_10 = []
    if all_sensor_data:
        last_10_raw = all_sensor_data['Items'][-10:]
        for entry_raw in last_10_raw:
            entry = {}
            for key, data in entry_raw['payload']['M'].items():
                value = None
                if 'Alarm' in key:
                    value = data['BOOL']
                else:
                    value = data['N']
                entry[key] = value
            last_10.append(entry)
    return last_10

def lambda_handler(event, context):
    '''
    Gets the last 10 entries in the DynamoDB database, formats the data,
    then returns it to the user.
    '''

    operation = event['httpMethod']
    if operation == 'GET':
        payload = { 'TableName': 'Sensor_Data_1' }
        all_sensor_data = dynamo.scan(**payload)
        last_10 = get_last_10(all_sensor_data)
        return respond(None, last_10)
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
