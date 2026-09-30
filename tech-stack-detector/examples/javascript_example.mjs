// npm install apify-client
// APIFY_TOKEN=... node javascript_example.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('siftwright/tech-stack-detector').call({ urls: ['vercel.com', 'shopify.com'] });
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(item.domain, item.status, item.technologyNames ?? item.error);
}
