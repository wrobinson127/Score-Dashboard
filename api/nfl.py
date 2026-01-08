import json
import urllib.request
import urllib.error

def handler(request):
    try:
        url = 'https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard'
        with urllib.request.urlopen(url) as response:
            data = response.read()
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': data.decode('utf-8')
        }
    except urllib.error.URLError as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
