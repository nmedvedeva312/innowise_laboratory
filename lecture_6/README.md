# Lecture 6: Dockerized FastAPI Healthcheck App

This project demonstrates how to dockerize a minimal Python FastAPI application.

The application exposes a single endpoint used for health checking and is intended to verify basic Docker workflow: building an image, running a container, and querying an endpoint.

## Application Description

The FastAPI application provides one endpoint:

GET /healthcheck

Response:
```json
{"status": "ok"}

