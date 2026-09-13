# Docker networking lab

The reverse proxy is the only service published to the host. The application is reachable by the proxy over the private `frontend` network and is not directly published.

## Request path

`host:8080 -> proxy:80 -> app:8080`

## Concepts demonstrated

- Port publishing exposes a service outside Docker.
- A user-defined bridge network provides service-name DNS (`app`).
- The proxy and app share `frontend`; the app has no host port mapping.
- The proxy forwards the original host and client headers.

## Try it

```bash
docker compose up --build -d
curl http://localhost:8080/health
docker compose ps
docker compose down
```

Inspect the network:

```bash
docker network ls
docker network inspect devops-foundations-lab_frontend
```
