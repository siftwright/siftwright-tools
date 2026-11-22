import { ApifyClient } from "apify-client";

const client = new ApifyClient({ token: "YOUR_APIFY_TOKEN" });
const run = await client.actor("siftwright/google-news-scraper").call({ query: "post-quantum cryptography", maxItems: 10 });
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) console.log(item.title, "-", item.source);
