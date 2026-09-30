"""Apple App Store reviews by app name with the Siftwright App Store Reviews Scraper.

pip install apify-client   # examples use apify-client 3.x; on 2.x use run["defaultDatasetId"]
export APIFY_TOKEN=...     # console.apify.com -> Settings -> API & Integrations
"""
import os
from collections import Counter
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("siftwright/app-store-reviews-scraper").call(run_input={
    "apps": ["Notion"],              # name, App Store link or numeric id
    "countries": ["us", "gb"],
    "maxReviewsPerApp": 100,
    "maxRating": 2,                  # only 1-2 star reviews are returned (and billed)
})

reviews = list(client.dataset(run.default_dataset_id).iterate_items())
print(len(reviews), "low-star reviews")
print("by app version:", Counter(r["appVersionReviewed"] for r in reviews).most_common(5))
for r in reviews[:5]:
    print(f'[{r["country"]} {r["rating"]}*] {r["title"]}')
