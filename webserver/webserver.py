import socketserver
import os

import http.server

PORT = 8000
DIRECTORY = os.path.join(os.path.dirname(__file__), '..')

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = super().translate_path(path)
        relpath = os.path.relpath(path, os.getcwd())
        return os.path.join(DIRECTORY, relpath)

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()