import http.server
import socketserver

PORT = 5000

class HealthHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Healthy')
        else:
            self.send_response(404)
            self.end_headers()

with socketserver.TCPServer(("", PORT), HealthHandler) as httpd:
    print(f"Servindo na porta {PORT}")
    httpd.serve_forever()

