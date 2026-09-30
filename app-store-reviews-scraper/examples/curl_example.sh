#!/usr/bin/env bash
# One call, results back as JSON. Set APIFY_TOKEN first.
curl -s -X POST "https://api.apify.com/v2/acts/siftwright~app-store-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"apps":["Notion"],"countries":["us"],"maxReviewsPerApp":50,"maxRating":2}'
