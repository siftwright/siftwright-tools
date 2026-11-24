# Use Siftwright tools from AI agents (MCP)

Every Siftwright tool is a public Apify Actor, so any MCP-compatible client (Claude Desktop, Claude Code, Cursor, VS Code, ChatGPT connectors and others) can call it through **Apify's MCP server**. Your agent can then say "get the transcript of this video" or "screenshot this page as a PDF" and it just works.

You need a free Apify account and its API token (console.apify.com → Settings → API & Integrations). You pay only for successful results, at the prices listed in the main README.

## Try it free first: Siftwright's hosted MCP server (no account, no key)

Siftwright also runs its own remote MCP server at **`https://siftwright.com/mcp`** (streamable HTTP, listed in the official MCP Registry as `com.siftwright/web-data`). Two of its tools work **without any key or sign-up**, one domain per call, with a daily limit per network:

- `domain_whois`: registrar, created/expiry dates, age, nameservers, MX/SPF/DMARC for a domain
- `pqc_scan`: whether a site uses post-quantum TLS key exchange (X25519MLKEM768 / ML-KEM)

```json
{
  "mcpServers": {
    "siftwright": { "type": "http", "url": "https://siftwright.com/mcp" }
  }
}
```

Quick check from a terminal (real response shape, abbreviated):

```bash
curl -s https://siftwright.com/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"domain_whois","arguments":{"domains":["wikipedia.org"]}}}'
# {"mode":"free_trial","results":[{"domain":"wikipedia.org","registrar":"MarkMonitor Inc.","createdAt":"2001-01-13...","nameservers":[...],"dns":{"mx":[...],"spf":"v=spf1 ...","dmarc":"v=DMARC1; p=reject; ..."}}], ...}
```

The other 7 tools on that server (YouTube transcripts, screenshots, Google News, contact details, tech stack, App Store reviews, jobs) need a Siftwright API key sent as `Authorization: Bearer sw_live_...` ([plans](https://siftwright.com/pricing/), failed results are free; [docs](https://siftwright.com/docs/#mcp)). If you'd rather pay per result with no subscription, use the Apify options below.

## Option A: hosted via Apify (no install)

Add a remote MCP server with this URL and your token as a Bearer header:

```
https://mcp.apify.com/?tools=siftwright/youtube-transcript-extractor,siftwright/pageframe-screenshots,siftwright/google-news-scraper,siftwright/contact-details-extractor,siftwright/app-store-reviews-scraper,siftwright/tech-stack-detector,siftwright/ats-jobs-scraper,siftwright/domain-whois-dns-lookup,siftwright/email-validator-mx-disposable
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
        "siftwright/youtube-transcript-extractor,siftwright/pageframe-screenshots,siftwright/google-news-scraper,siftwright/contact-details-extractor,siftwright/app-store-reviews-scraper,siftwright/tech-stack-detector,siftwright/ats-jobs-scraper,siftwright/domain-whois-dns-lookup,siftwright/email-validator-mx-disposable"
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
| `siftwright/youtube-transcript-extractor` | Transcripts/subtitles for videos, playlists, channels | $0.0015 per transcript |
| `siftwright/pageframe-screenshots` | PNG/JPEG screenshots and PDFs of URLs | $0.0015 per capture |
| `siftwright/google-news-scraper` | Google News results for a query | $0.0015 per article |
| `siftwright/contact-details-extractor` | Emails, phones, social links from company sites | $0.002 per website |
| `siftwright/app-store-reviews-scraper` | Apple App Store reviews by app name, country, stars | $0.0001 per review |
| `siftwright/tech-stack-detector` | What a website is built with, plus email/DNS provider, with evidence | $0.002 per website |
| `siftwright/ats-jobs-scraper` | Open jobs from Greenhouse, Lever, Ashby, SmartRecruiters and Recruitee boards, filtered | $0.001 per job |
| `siftwright/domain-whois-dns-lookup` | Registrar, created/expiry dates, age, nameservers, MX/SPF/DMARC | $0.001 per domain |
| `siftwright/email-validator-mx-disposable` | Bulk email verdicts: syntax, MX, disposable domains, typo suggestions | $0.0008 per email |

Failed items are never charged. Load only the tools your agent needs by trimming the `tools=` list.
