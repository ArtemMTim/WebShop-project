from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
from config import HTML_DIR

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        with open(os.path.join(HTML_DIR, 'contacts.html'), mode='r', encoding='utf-8') as file:
            data = file.read()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        #self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(data, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(str(body))
        self.send_response(200)
        self.end_headers()


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped")
