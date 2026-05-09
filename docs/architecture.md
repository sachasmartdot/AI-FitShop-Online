
---
# Architecture

## Overview

The system is designed as a simple client-server application.

It is intentionally minimal but structured in a way that allows future extensions.

## Components

### Frontend

- Static HTML page
- Handles user interaction
- Sends requests to backend API

### Backend

- FastAPI service
- Exposes REST endpoints
- Contains business logic

### Fit Engine

- Isolated module
- Responsible for size recommendation
- Can evolve into a more advanced AI model

### Data Layer

- JSON file used as mock database
- Can be replaced with a real database later

## Data Flow

1. User selects a product
2. User inputs foot length
3. Frontend sends request to backend
4. Backend calls fit engine
5. Result is returned to frontend

## Design Choices

- Separation between logic and API
- Minimal dependencies
- Easy to extend toward AI-based system

## Future Evolution

- Replace rule-based logic with LLM agent
- Add conversation layer
- Integrate external APIs
- Move to database storage
