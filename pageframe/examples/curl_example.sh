#!/usr/bin/env bash
# One call, results back as JSON (each row has a fileUrl). Set APIFY_TOKEN first.
curl -s -X POST "https://api.apify.com/v2/acts/siftwright~pageframe-screenshots/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"urls":["https://apify.com"],"format":"png","fullPage":true,"deviceScaleFactor":2}'
