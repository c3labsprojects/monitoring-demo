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
# from project root
docker compose up -d --build

# URLs
# App:          http://localhost:8000
# Metrics:      http://localhost:8000/metrics
# Prometheus:   http://localhost:9090
# Grafana:      http://localhost:3000  (admin/admin)
# Alertmanager: http://localhost:9093
```

## 🎭 Simulate Incident

### 1. Trigger Incident
```bash
# Edit docker-compose.yml and set:
# ERROR_RATE=0.3
# SLEEP_MS=800
docker compose up -d --build app
```

### 2. Monitor Alerts
- **Check Prometheus "Alerts" tab**: http://localhost:9090/alerts
- **View Grafana dashboard**: http://localhost:3000
- **Check Alertmanager**: http://localhost:9093

### 3. Resolve Incident
```bash
# Revert values in docker-compose.yml:
# ERROR_RATE=0.0
# SLEEP_MS=0
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