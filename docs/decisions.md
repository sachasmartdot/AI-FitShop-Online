# Technical Decisions

## Why FastAPI

FastAPI was chosen for its simplicity and speed of development. It allows building APIs quickly while keeping the code clean.

## Why a separate fit engine

The sizing logic is isolated in its own module to make it easier to upgrade later.

This makes it possible to:
- Replace rules with ML model
- Add more complex logic without touching API

## Why JSON for data

Using a JSON file keeps the system simple for the MVP phase.

It avoids database setup and allows fast iteration.

## Why simple frontend

The goal is not UI complexity at this stage, but validating the core idea.

A lightweight frontend helps focus on functionality.

## Evolution strategy

The system is designed to evolve in layers:

1. Static product display
2. Rule-based recommendation
3. AI-driven assistant
4. Full immersive experience
