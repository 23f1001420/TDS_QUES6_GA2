import json
from http.server import BaseHTTPRequestHandler
import urllib.parse

def load_data():
    """ Load student marks from the JSON file """
    with open('q-vercel-python.json', 'r') as file:
        return json.load(file)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        names = query.get('name', [])  # Extract names from query parameters
        data = load_data()

        # Extract marks for given names
        marks = []
        for name in names:
            for entry in data:
                if entry["name"] == name:
                    marks.append(entry["marks"])

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
        self.end_headers()
        self.wfile.write(json.dumps({"marks": marks}).encode('utf-8'))

