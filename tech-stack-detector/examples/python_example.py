"""What is a website built with? Siftwright Tech Stack Detector.

pip install apify-client   # examples use apify-client 3.x; on 2.x use run["defaultDatasetId"]
export APIFY_TOKEN=...     # console.apify.com -> Settings -> API & Integrations
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("siftwright/tech-stack-detector").call(run_input={
    "urls": ["vercel.com", "wordpress.org", "shopify.com"],
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    if item["status"] != "ok":
        print("failed (not charged):", item.get("domain") or item["input"], item["error"])
        continue
    print(item["domain"])
    for category, names in item["byCategory"].items():
        print(f"  {category:<22} {', '.join(names)}")
