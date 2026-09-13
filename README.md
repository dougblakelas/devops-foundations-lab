# DevOps Foundations Lab

A small, reproducible service used to practice the foundations of DevOps: Git, Python services, Docker, networking, health checks, CI, and monitoring.

## What this demonstrates

- A minimal HTTP service with `/` and `/health` endpoints
- Automated tests with Python's standard library
- A non-root Docker container
- Docker Compose with a private user-defined bridge network
- Nginx reverse proxy with only the proxy port published
- Service health checks and dependency ordering
- GitHub Actions for tests, image builds, Compose validation, and an integration request

## Run locally without Docker

```bash
python3 -m unittest discover -s tests -v
python3 app/main.py
```

## Run with Docker

```bash
docker compose up --build -d
curl http://localhost:8080/health
docker compose ps
docker compose down
```

The request path is:

`host:8080 -> proxy:80 -> app:8080`

The app has no host port mapping. It is reachable only by the proxy over the private `frontend` network. Details are in `networking/README.md`.

## Learning notes

- A container packages the application and runtime, but is not a virtual machine.
- `ports` publishes a container port to the host; `expose` documents an internal port without publishing it.
- User-defined Docker networks provide container-to-container DNS using service names.
- Health checks let Compose and orchestrators detect failure.
- CI should test both code and the deployed wiring, not just build an image.

## Next improvements

1. Add Prometheus metrics and Grafana dashboards.
2. Add image scanning and publishing to GitHub Container Registry.
3. Deploy the service to Kubernetes.
4. Add an incident runbook and failure exercise.
