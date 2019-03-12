import json

def lambda_handler(event, context):
    # TODO implement
    if not 'game_id' in event:
        raise Exception('No game_id specified.')
    if not 'turn_number' in event:
        raise Exception('No turn_number specified.')
    
    return  json.dumps(int(event['turn_number'])+1)
