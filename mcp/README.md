# Use Siftwright tools from AI agents (MCP)

Every Siftwright tool is a public Apify Actor, so any MCP-compatible client (Claude Desktop, Claude Code, Cursor, VS Code, ChatGPT connectors and others) can call it through **Apify's MCP server**. Your agent can then say "get the transcript of this video" or "screenshot this page as a PDF" and it just works.

You need a free Apify account and its API token (console.apify.com → Settings → API & Integrations). You pay only for successful results, at the prices listed in the main README.

## Option A: hosted (no install)

Add a remote MCP server with this URL and your token as a Bearer header:

```
https://mcp.apify.com/?tools=siftwright/youtube-transcript-extractor,siftwright/pageframe-screenshots,siftwright/google-news-scraper,siftwright/contact-details-extractor,siftwright/app-store-reviews-scraper,siftwright/tech-stack-detector,siftwright/ats-jobs-scraper
```

```
Authorization: Bearer YOUR_APIFY_TOKEN
```

## Option B: local (Claude Desktop / Cursor config)

```json
{
  "mcpServers": {
    "siftwright": {
      "command": "npx",
      "args": [
        "-y",
        "@apify/actors-mcp-server",
        "--actors",
        "siftwright/youtube-transcript-extractor,siftwright/pageframe-screenshots,siftwright/google-news-scraper,siftwright/contact-details-extractor,siftwright/app-store-reviews-scraper,siftwright/tech-stack-detector,siftwright/ats-jobs-scraper"
      ],
      "env": { "APIFY_TOKEN": "YOUR_APIFY_TOKEN" }
    }
  }
}
```

A ready-to-copy version of this is in [`claude_desktop_config.example.json`](claude_desktop_config.example.json).

## Example prompts

- "Get the English transcript of https://youtu.be/dQw4w9WgXcQ and summarize it in 5 bullets."
- "Pull transcripts for the 10 newest videos on @mkbhd and list the products mentioned."
- "Take a full-page retina screenshot of https://apify.com and save it."
- "Turn https://en.wikipedia.org/wiki/Web_scraping into an A4 PDF."
- "Find this week's Google News coverage of 'post-quantum cryptography' and list the publishers."
- "Get the public contact email, phone and LinkedIn page for basecamp.com and mailchimp.com."
- "Pull the latest 1- and 2-star App Store reviews for Notion in the US and UK and group the complaints by theme."
- "What CMS, analytics and email provider do stripe.com and notion.so use? Show the evidence."

## Tools exposed

| Actor | What the agent can do | Price |
|---|---|---|
| `siftwright/youtube-transcript-extractor` | Transcripts/subtitles for videos, playlists, channels | $0.003 per transcript |
| `siftwright/pageframe-screenshots` | PNG/JPEG screenshots and PDFs of URLs | $0.0015 per capture |
| `siftwright/google-news-scraper` | Google News results for a query | $0.0015 per article |
| `siftwright/contact-details-extractor` | Emails, phones, social links from company sites | $0.002 per website |
| `siftwright/app-store-reviews-scraper` | Apple App Store reviews by app name, country, stars | $0.0001 per review |
| `siftwright/tech-stack-detector,siftwright/ats-jobs-scraper` | What a website is built with, plus email/DNS provider, with evidence | $0.002 per website |

Failed items are never charged. Load only the tools your agent needs by trimming the `tools=` list.
