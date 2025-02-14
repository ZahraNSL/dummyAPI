#!/bin/bash
docker build -t my-api .
docker network create test-network || true
docker run -d --name api-container --network test-network -p 5001:5000 my-api