from http.server import BaseHTTPRequestHandler
import json
import urllib.request
import urllib.error

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            url = 'https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard'
            with urllib.request.urlopen(url) as response:
                data = response.read()
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            self.wfile.write(data)
            
        except urllib.error.URLError as e:
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
