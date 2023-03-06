from storysniffer import StorySniffer
import json

def lambda_handler(event, context):
    url = event['url']
    title = event['title']

    sniffer = StorySniffer()
    res = sniffer.guess(
        url,
        text=title
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }