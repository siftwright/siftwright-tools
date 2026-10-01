"""Domains expiring within 90 days, and domains missing DMARC. pip install apify-client (3.x)."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("siftwright/domain-whois-dns-lookup").call(run_input={
    "domains": ["stripe.com", "github.io", "https://www.bbc.co.uk/news", "ramp.dev"],
})
# apify-client 3.x returns a Run object; on 2.x use run["defaultDatasetId"]
for d in client.dataset(run.default_dataset_id).iterate_items():
    if not d["registered"]:
        print(f'{d["domain"]:<14} not registered')
        continue
    soon = d["daysUntilExpiry"] is not None and d["daysUntilExpiry"] < 90
    no_dmarc = not (d.get("dns") or {}).get("dmarc")
    print(f'{d["domain"]:<14} {d["registrar"] or "?":<34} age {d["ageDays"]} days'
          f'{"  EXPIRES < 90 DAYS" if soon else ""}{"  NO DMARC" if no_dmarc else ""}')
