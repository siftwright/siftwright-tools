"""Open engineering jobs at a few companies, newest first. pip install apify-client (3.x)."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("siftwright/ats-jobs-scraper").call(run_input={
    "companies": ["ramp.com", "https://jobs.lever.co/palantir", "greenhouse:airbnb"],
    "titleKeywords": ["engineer"],
    "postedWithinDays": 30,
    "includeDescription": False,
})
# apify-client 3.x returns a Run object; on 2.x use run["defaultDatasetId"]
for job in client.dataset(run.default_dataset_id).iterate_items():
    print(f'{job["company"]:<10} {job["title"][:55]:<55} {job["location"] or "":<30} {job["url"]}')

# Which board was found for each company, and how many jobs it had
summary = client.key_value_store(run.default_key_value_store_id).get_record("SUMMARY")["value"]
for row in summary["companies"]:
    print(row["input"], "->", row["ats"], row["boardSlug"], f'({row["detectedVia"]})', row["jobsReturned"], "returned")
