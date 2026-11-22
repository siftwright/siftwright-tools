// npm i apify-client
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('siftwright/email-validator-mx-disposable').call({
  emails: ['jane@github.com', 'someone@gmial.com', 'test@mailinator.com'],
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const r of items) console.log(r.email, r.verdict, r.reason ?? '', r.suggestion ?? '');
