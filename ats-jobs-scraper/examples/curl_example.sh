#!/usr/bin/env bash
# One call, jobs back as JSON. Set APIFY_TOKEN first.
curl -s -X POST "https://api.apify.com/v2/acts/siftwright~ats-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"companies":["greenhouse:airbnb"],"titleKeywords":["data"],"includeDescription":false}'
