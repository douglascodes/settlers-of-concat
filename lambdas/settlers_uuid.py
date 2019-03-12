import json
import uuid

def lambda_handler(event, context):
    # TODO implement
    return {
        'uuid': str(uuid.uuid4())
    }
