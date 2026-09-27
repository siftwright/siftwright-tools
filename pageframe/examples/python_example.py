"""Screenshot websites (PNG/JPEG) or save them as PDFs with Siftwright Pageframe.

pip install apify-client requests
export APIFY_TOKEN=...   # console.apify.com -> Settings -> API & Integrations
"""
import os
import requests
from apify_client import ApifyClient

token = os.environ["APIFY_TOKEN"]
client = ApifyClient(token)
run = client.actor("siftwright/pageframe-screenshots").call(run_input={
    "urls": ["https://apify.com", "https://en.wikipedia.org/wiki/Web_scraping"],
    "format": "png",          # or "jpeg" / "pdf"
    "fullPage": True,
    "deviceScaleFactor": 2,   # retina
    "blockCookieBanners": True,
})

for i, item in enumerate(client.dataset(run["defaultDatasetId"]).iterate_items()):
    if item["status"] != "ok":
        print("failed (not charged):", item["url"], item.get("error"))
        continue
    data = requests.get(item["fileUrl"], headers={"Authorization": f"Bearer {token}"}).content
    name = f"capture-{i}.{item['format']}"
    open(name, "wb").write(data)
    print("saved", name, item["sizeBytes"], "bytes")
