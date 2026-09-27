#!/usr/bin/env bash
# One call, results back as JSON. Set APIFY_TOKEN first.
curl -s -X POST "https://api.apify.com/v2/acts/siftwright~youtube-transcript-extractor/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"urls":["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],"outputFormats":["text"]}'
