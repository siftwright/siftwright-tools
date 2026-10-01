// Registration dates for a few domains, as JSON. npm install apify-client
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('siftwright/domain-whois-dns-lookup').call({
    domains: ['stripe.com', 'notion.so', 'spiegel.de'],
    includeDns: false,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const d of items) console.log(d.domain, '|', d.registrar, '|', d.createdAt, '|', d.expiresAt, '|', d.source);
