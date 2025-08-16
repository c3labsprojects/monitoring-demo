# Monitoring & Incident Response Demo

A lightweight, production-ready demonstration of observability best practices using FastAPI, Prometheus, Grafana, and Alertmanager. This demo showcases operational judgment and incident response capabilities through a controlled, tunable service.

## 🎯 What This Proves

- **Observability Setup**: Stand up metrics, monitoring, dashboards, and alerts quickly
- **Golden Signals**: Implement error rate and latency monitoring with actionable alerts
- **Incident Response**: Orchestrate a complete incident rehearsal from detection to resolution
- **Production Thinking**: Demonstrate SLO/SLI understanding and operational judgment

## 🏗️ Tech Stack

- **FastAPI**: Python web service with controllable error rates and latency
- **Prometheus**: Metrics collection and alert rule evaluation
- **Grafana**: Pre-configured dashboard for incident investigation
- **Alertmanager**: Alert routing and notification management
- **Docker Compose**: Single-command orchestration

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd monitoring-incident-demo

# Start all services
docker compose up -d

# Verify services are running
docker compose ps
```

### Access Points
- **App**: http://localhost:8000
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (admin/admin)
- **Alertmanager**: http://localhost:9093

## 🎭 Incident Simulation

### 1. Healthy System
```bash
# App starts with 0% errors, 0ms latency
curl http://localhost:8000
# Response: {"ok": true, "message": "hello from demo"}
```

### 2. Trigger Incident
```bash
# Update docker-compose.yml environment variables:
#   - ERROR_RATE=0.3
#   - SLEEP_MS=800

# Rebuild and restart
docker compose up -d --build app
```

### 3. Monitor Alerts
- **Prometheus Alerts**: http://localhost:9090/alerts
- **Grafana Dashboard**: http://localhost:3000
- **Alertmanager**: http://localhost:9093

### 4. Resolve Incident
```bash
# Restore healthy behavior
#   - ERROR_RATE=0.0
#   - SLEEP_MS=0

# Rebuild and restart
docker compose up -d --build app
```

## 📊 Metrics & Alerts

### Golden Signals
- **Error Rate**: `rate(errors_total[2m]) / rate(requests_total[2m])`
- **Latency**: `histogram_quantile(0.95, rate(request_latency_seconds_bucket[2m]))`

### Alert Rules
- **HighErrorRate**: 5xx error ratio > 5% for 2 minutes
- **HighLatencyP95**: p95 latency > 500ms for 2 minutes

## 📁 Project Structure

```
monitoring-incident-demo/
├── app/                          # FastAPI service
│   ├── main.py                  # Service with Prometheus metrics
│   ├── requirements.txt         # Python dependencies
│   └── Dockerfile              # Container definition
├── prometheus/                  # Metrics & alerting
│   ├── prometheus.yml          # Scrape configuration
│   └── alerts.yml              # Alert rules
├── grafana/                     # Visualization
│   └── dashboards/             # Auto-configured dashboards
│       └── service-overview.json
├── alertmanager/               # Alert routing
│   └── alertmanager.yml       # Notification configuration
├── docker-compose.yml          # Service orchestration
├── README.md                   # This file
└── .gitignore                 # Git exclusions
```

## 🎯 Use Cases

### Technical Interviews
- Demonstrate observability knowledge
- Show incident response thinking
- Prove operational judgment

### Team Training
- Incident response practice
- Monitoring setup walkthrough
- SLO/SLI implementation examples

## 🔍 Troubleshooting

### Common Issues
- **Port conflicts**: Check if ports 8000, 9090, 3000, 9093 are available
- **Container startup**: Use `docker compose logs <service>` to debug
- **Environment variables**: Ensure app service is rebuilt after changes

### Debug Commands
```bash
# Check service status
docker compose ps

# View logs
docker compose logs app
docker compose logs prometheus

# Test endpoints
curl http://localhost:8000/health
curl http://localhost:8000/metrics
```

## 📚 Learning Resources

- [Prometheus Query Language](https://prometheus.io/docs/prometheus/latest/querying/)
- [Grafana Dashboard Design](https://grafana.com/docs/grafana/latest/dashboards/)
- [Alertmanager Configuration](https://prometheus.io/docs/alerting/latest/configuration/)
- [FastAPI with Prometheus](https://fastapi.tiangolo.com/)

---

**Remember**: This demo exists to showcase operational judgment and observability skills. Keep it simple, clear, and focused on demonstrating your capabilities.