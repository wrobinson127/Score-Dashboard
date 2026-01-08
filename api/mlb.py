from http.server import BaseHTTPRequestHandler
import json
import urllib.request
import urllib.error
from datetime import datetime, timedelta

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Get dates for the next 2 days of MLB games
            dates = []
            for i in range(-1, 3):  # Yesterday through 2 days ahead
                date = (datetime.now() + timedelta(days=i)).strftime('%Y%m%d')
                dates.append(date)
            
            all_events = []
            
            # Fetch games for each date
            for date in dates:
                url = f'https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates={date}'
                try:
                    with urllib.request.urlopen(url) as response:
                        data = json.loads(response.read())
                        if 'events' in data:
                            all_events.extend(data['events'])
                except:
                    continue
            
            # Create response with all events
            response_data = {
                'events': all_events,
                'leagues': [{'id': 'mlb', 'name': 'Major League Baseball', 'abbreviation': 'MLB'}]
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            error = json.dumps({'error': str(e)}).encode()
            self.wfile.write(error)
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
