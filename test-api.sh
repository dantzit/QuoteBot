#!/bin/bash
# Simple script to test the QuoteBot API

echo "Testing QuoteBot API..."
echo ""

# Test health check
echo "1. Testing health check endpoint..."
curl -s http://localhost:3000/ | jq .
echo ""

# Test chat endpoint with missing message
echo "2. Testing chat endpoint with missing message (should fail)..."
curl -s -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{}' | jq .
echo ""

# Test chat endpoint with message
echo "3. Testing chat endpoint with message..."
curl -s -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me a quote about coding"}' | jq .
echo ""

echo "Tests completed!"
