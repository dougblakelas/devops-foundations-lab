# Monitoring stack

This milestone adds application metrics, Prometheus, Grafana, and an alert rule.

## Components

- The app exposes Prometheus-compatible metrics at `/metrics`.
- Prometheus scrapes `app:8080` over the private `metrics` network.
- Grafana uses Prometheus as a provisioned data source.
- A dashboard is provisioned automatically from `grafana/dashboards`.
- Prometheus alerts when the app scrape target is down for 30 seconds.

## Start

```bash
docker compose up --build -d
```

Open:

- App: http://localhost:8080/health
- Metrics: http://localhost:8080/metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

Check Prometheus targets at http://localhost:9090/targets. The app target should be UP.

Grafana's default login is `admin` / `admin` on a new local instance; change it immediately in a real deployment. This lab is for local learning only and does not publish Grafana credentials or expose it to the internet.

Stop the stack:

```bash
docker compose down
```

To remove the Grafana learning data as well:

```bash
docker compose down -v
```
