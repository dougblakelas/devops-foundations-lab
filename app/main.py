from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = {"status": "ok", "service": "devops-foundations-lab"}
            self.send_response(200)
        elif self.path == "/":
            body = {"message": "DevOps foundations lab", "version": os.getenv("APP_VERSION", "dev")}
            self.send_response(200)
        else:
            body = {"error": "not found"}
            self.send_response(404)
        payload = json.dumps(body).encode()
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
