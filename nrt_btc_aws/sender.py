import json
import logging

import boto3
from botocore.exceptions import ClientError


def send_to_firehose(stream_name: str, current_price: str, ing_date: str):
    """Sends 60B per file ingested"""
    firehoseclient = boto3.client('firehose')
    try:
        firehoseclient.put_record(
            DeliveryStreamName=stream_name,
            Record={
                'Data': json.dumps({
                    'current_price': current_price,
                    'ing_date': ing_date,
                })
            },
        )
    except ClientError as e:
        logging.error(e)
        return False
    else:
        return True
