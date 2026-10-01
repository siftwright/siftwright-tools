// Remote jobs in two departments, as JSON. npm install apify-client
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('siftwright/ats-jobs-scraper').call({
    companies: ['notion.so', 'Figma'],
    departments: ['Engineering', 'Sales'],
    remoteOnly: true,
    includeDescription: false,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const job of items) console.log(job.company, '|', job.title, '|', job.location, '|', job.url);
console.log(`${items.length} jobs`);
