import http.server
import socketserver
import threading
import http.client
import urllib.parse
from urllib.parse import parse_qs
from urllib.parse import quote
import os
import sys
import html

class MyHandler(http.server.SimpleHTTPRequestHandler):
    TOKEN = os.environ['TOKEN']
    PORT = int(os.environ['PORT'])
    BOT_TOKEN = os.environ['BOT_TOKEN']
    BOT_CHAT_ID = os.environ['BOT_CHAT_ID']


    def do_POST(self):
        if self.path == '/notify':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            params = parse_qs(post_data.decode('utf-8'))

            token = params.get('token', [''])[0]
            msg = params.get('msg', [''])[0]

            # Print the request content
            print("Received POST request:")
            print(f"Token: {token}")
            print(f"Message: {msg}")

            if token == self.TOKEN:
                self.process_notification(msg)
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(('Your message has been sent: ' + html.unescape(msg)).encode('utf-8'))
            else:
                self.send_response(403)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Invalid token')

    def do_GET(self):
        if self.path == '/web':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('./form.html', 'r') as file:
                html_content = file.read()
            self.wfile.write(html_content.encode('utf-8'))

    def process_notification(self, msg):
        chat_id = self.BOT_CHAT_ID
        url = self.BOT_TOKEN + "/sendMessage"
        params = urllib.parse.urlencode({'chat_id': chat_id, 'text': html.unescape(msg)})
        headers = {'Content-type': 'application/x-www-form-urlencoded'}

        conn = http.client.HTTPSConnection("api.telegram.org")
        conn.request("POST", url, params.encode('utf-8'), headers)
        response = conn.getresponse()

        if response.status == 200:
            print("Notification sent successfully.")
        else:
            print("Failed to send notification.")

        conn.close()

Handler = MyHandler

with socketserver.TCPServer(("", MyHandler.PORT), Handler) as httpd:
    print(f"Serving at port {MyHandler.PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(f"Server stopped. Port {MyHandler.PORT} released.")
