// npm install apify-client
// APIFY_TOKEN=... node javascript_example.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('siftwright/youtube-transcript-extractor').call({
    urls: ['https://www.youtube.com/watch?v=dQw4w9WgXcQ'],
    outputFormats: ['text', 'segments'],
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(item.status, item.title, item.wordCount ?? 0, 'words');
}
