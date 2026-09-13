import json
import os
import sys
import unittest
from http.client import HTTPConnection
from threading import Thread
from http.server import HTTPServer

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app.main import Handler


class AppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def get(self, path):
        conn = HTTPConnection("127.0.0.1", self.server.server_port)
        conn.request("GET", path)
        response = conn.getresponse()
        raw = response.read()
        conn.close()
        return response.status, raw

    def test_health(self):
        status, raw = self.get("/health")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(raw)["status"], "ok")

    def test_metrics(self):
        status, raw = self.get("/metrics")
        self.assertEqual(status, 200)
        self.assertIn(b"app_requests_total", raw)
        self.assertIn(b"app_uptime_seconds", raw)

    def test_not_found(self):
        status, _ = self.get("/missing")
        self.assertEqual(status, 404)


if __name__ == "__main__":
    unittest.main()
