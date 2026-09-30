// npm install apify-client
// APIFY_TOKEN=... node javascript_example.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('siftwright/contact-details-extractor').call({
    startUrls: ['https://basecamp.com', 'https://www.mailchimp.com'],
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(item.status, item.domain, item.emails ?? [], item.phones ?? []);
}
