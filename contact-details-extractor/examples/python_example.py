"""Emails, phones and social links from company websites with the Siftwright Contact Details Extractor.

pip install apify-client   # examples use apify-client 3.x; on 2.x use run["defaultDatasetId"]
export APIFY_TOKEN=...     # console.apify.com -> Settings -> API & Integrations
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("siftwright/contact-details-extractor").call(run_input={
    "startUrls": ["https://basecamp.com", "https://www.mailchimp.com"],
    "maxPagesPerDomain": 6,
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    if item["status"] != "ok":
        print("failed to load (not charged):", item["domain"], item.get("error"))
        continue
    print(item["domain"], "| emails:", item["emails"], "| phones:", item["phones"], "| linkedin:", item["linkedin"])
