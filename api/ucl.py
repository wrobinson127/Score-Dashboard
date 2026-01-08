from http.server import BaseHTTPRequestHandler
import json
import urllib.request
import urllib.error
from datetime import datetime, timedelta

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Get dates for the next 3 days of Champions League games
            dates = []
            for i in range(-1, 4):  # Yesterday through 3 days ahead
                date = (datetime.now() + timedelta(days=i)).strftime('%Y%m%d')
                dates.append(date)
            
            all_events = []
            
            # Fetch games for each date (uefa.2 is UEFA Champions League)
            for date in dates:
                url = f'https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.2/scoreboard?dates={date}'
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
                'leagues': [{'id': 'uefa.2', 'name': 'UEFA Champions League', 'abbreviation': 'UCL'}]
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
