"""Flag undeliverable, disposable and typo'd addresses. pip install apify-client."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("siftwright/email-validator-mx-disposable").call(run_input={
    "emails": ["jane@github.com", "someone@gmial.com", "test@mailinator.com", "bad@@x"],
})
ds = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
for row in client.dataset(ds).iterate_items():
    extra = f' -> {row["suggestion"]}' if row.get("suggestion") else ""
    print(f'{row["email"]:<24} {row["verdict"]:<14} {row.get("reason") or ""}{extra}')
