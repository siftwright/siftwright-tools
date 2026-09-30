<p align="center">
  <img src="assets/siftwright-logo.png" alt="Siftwright" width="120">
</p>

<h1 align="center">Siftwright tools</h1>

<p align="center">
  <b>Reliable, fairly priced data tools and APIs. You only pay for successful results.</b><br>
  Run them in the cloud, with no servers and no setup, from Python, JavaScript, Make, Zapier, n8n or your AI agent.
</p>

---

## The tools

| | Tool | What it does | Price |
|---|---|---|---|
| <img src="assets/icon-youtube-transcript.png" width="48"> | **[YouTube Transcript Extractor](youtube-transcript-extractor/)** | Transcripts and subtitles from videos, Shorts, playlists and whole channels, as text, timestamped JSON, **SRT** or **VTT**, in any language, with auto-translate | **$3 per 1,000 transcripts**. Caption-less videos are free |
| <img src="assets/icon-pageframe.png" width="48"> | **[Pageframe](pageframe/)** | Screenshot any URL to **PNG/JPEG** or a print-ready **PDF**: full-page, retina 2x/3x, cookie banners removed automatically | **$1.50 per 1,000 captures**. Failed pages are free |
| 📰 | **[Google News Scraper](https://apify.com/siftwright/google-news-scraper)** | Google News results for any keyword, brand or topic as JSON: title, link, source, publish time, snippet; any language and country edition | **$1.50 per 1,000 articles**. Empty searches are free |
| 📇 | **[Contact Details Extractor](contact-details-extractor/)** | Emails, phone numbers and official social links from a list of company websites; finds the contact/about pages itself | **$2 per 1,000 websites**. Sites that fail to load are free |
| ⭐ | **[App Store Reviews Scraper](app-store-reviews-scraper/)** | Apple App Store reviews by app **name**, link or id, across many countries, with star/keyword/date filters applied before you pay | **$0.10 per 1,000 reviews**. Filtered-out reviews are free |
| 🧱 | **[Tech Stack Detector](tech-stack-detector/)** | CMS, ecommerce platform, frameworks, analytics, hosting, **email and DNS provider** of any website, with the evidence for every detection | **$2 per 1,000 websites**. Failed sites are free |

**▶ Try them:** [all Siftwright tools on the Apify Store](https://apify.com/siftwright) · product pages and guides at [siftwright.com](https://siftwright.com)
New Apify accounts get free monthly credit, so you can test without paying.

## Why Siftwright

- 🛡️ **Pay only for success.** Failed, empty or blocked items are never charged.
- 💵 **Simple per-result pricing.** No subscriptions, no monthly rental, no minimums.
- ⚡ **Runs in the cloud.** Call it once or a million times, from any language or no-code tool.
- 🤖 **AI-agent ready.** Claude, ChatGPT, Cursor and other MCP clients can call every tool directly (see [`mcp/`](mcp/)).

## 60-second quick start (Python)

```bash
pip install apify-client   # examples use apify-client 3.x
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")  # free at console.apify.com → Settings → API & Integrations

run = client.actor("siftwright/youtube-transcript-extractor").call(
    run_input={"urls": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"], "outputFormats": ["text"]}
)
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["title"], "-", item["wordCount"], "words")
```

More examples, in Python, JavaScript and curl, are in each tool's `examples/` folder.

## Use with AI agents (MCP)

Add Siftwright tools to Claude Desktop, Cursor or any MCP client through Apify's MCP server. See **[mcp/README.md](mcp/README.md)**.

## Support

Found a bug or want a feature? [Open an issue](../../issues) or email support@siftwright.com. We read every one.

---

<sub>This repository holds documentation and usage examples. The tools run on the Apify platform, where billing is handled per result.</sub>
