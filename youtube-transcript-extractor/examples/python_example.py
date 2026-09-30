"""Get YouTube transcripts with the Siftwright YouTube Transcript Extractor.

pip install apify-client   # apify-client 3.x; on 2.x use run["defaultDatasetId"]
export APIFY_TOKEN=...   # console.apify.com -> Settings -> API & Integrations
"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("siftwright/youtube-transcript-extractor").call(run_input={
    "urls": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/@mkbhd",          # channels and playlists work too
    ],
    "language": "en",
    "outputFormats": ["text", "srt"],
    "maxVideosPerSource": 5,
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    if item["status"] != "ok":
        print("skipped (not charged):", item["url"], item.get("error"))
        continue
    print(f'{item["title"]} ({item["wordCount"]} words)')
    with open(f'{item["videoId"]}.srt', "w", encoding="utf-8") as f:
        f.write(item["srt"])
