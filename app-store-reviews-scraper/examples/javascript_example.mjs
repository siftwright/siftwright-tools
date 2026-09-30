// npm install apify-client
// APIFY_TOKEN=... node javascript_example.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('siftwright/app-store-reviews-scraper').call({
    apps: ['Notion'],
    countries: ['us'],
    maxReviewsPerApp: 50,
    maxRating: 2,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`${items.length} reviews`);
for (const r of items.slice(0, 5)) console.log(`[${r.country} ${r.rating}*] ${r.title}`);
