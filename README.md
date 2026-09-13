# DevOps Foundations Lab

A small, reproducible service used to practice the foundations of DevOps: Git, Python services, Docker, health checks, CI, and later networking and monitoring.

## What this demonstrates

- A minimal HTTP service with `/` and `/health` endpoints
- Automated tests with Python's standard library
- A non-root Docker container
- Docker Compose with a health check
- GitHub Actions for tests and image builds

## Run locally

```bash
python3 -m unittest discover -s tests -v
python3 app/main.py
```

Then visit http://localhost:8080/health.

## Run with Docker

```bash
docker compose up --build
```

Then test it:

```bash
curl http://localhost:8080/health
```

Stop it with `Ctrl-C`, or run `docker compose down` in another terminal.

## Learning notes

- A container packages the application and its runtime, but it is not a virtual machine.
- `EXPOSE` documents the container port; publishing with `-p` or Compose makes it reachable from the host.
- The health check gives an orchestrator a machine-readable way to detect failure.
- CI should fail fast when tests or the image build fail.

## Next improvements

1. Add a reverse proxy and a private Docker network.
2. Add Prometheus metrics and Grafana dashboards.
3. Add image scanning and publishing to GitHub Container Registry.
4. Deploy the service to Kubernetes.
