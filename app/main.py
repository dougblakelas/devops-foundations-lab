from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import time

START_TIME = time.monotonic()
REQUESTS_TOTAL = 0


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, status, body):
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        global REQUESTS_TOTAL
        REQUESTS_TOTAL += 1

        if self.path == "/health":
            self._send_json(200, {"status": "ok", "service": "devops-foundations-lab"})
        elif self.path == "/metrics":
            uptime = time.monotonic() - START_TIME
            body = (
                "# HELP app_requests_total Total HTTP requests received\\n"
                "# TYPE app_requests_total counter\\n"
                f"app_requests_total {REQUESTS_TOTAL}\\n"
                "# HELP app_uptime_seconds Process uptime in seconds\\n"
                "# TYPE app_uptime_seconds gauge\\n"
                f"app_uptime_seconds {uptime:.3f}\\n"
            )
            payload = body.encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
        elif self.path == "/":
            self._send_json(200, {"message": "DevOps foundations lab", "version": os.getenv("APP_VERSION", "dev")})
        else:
            self._send_json(404, {"error": "not found"})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
