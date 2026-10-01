#!/usr/bin/env bash
# One call, results back as JSON. Set APIFY_TOKEN first.
curl -s -X POST "https://api.apify.com/v2/acts/siftwright~domain-whois-dns-lookup/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"domains":["stripe.com","github.io"],"includeDns":false}'
