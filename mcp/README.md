# Use Siftwright tools from AI agents (MCP)

Every Siftwright tool is a public Apify Actor, so any MCP-compatible client (Claude Desktop, Claude Code, Cursor, VS Code, ChatGPT connectors and others) can call it through **Apify's MCP server**. Your agent can then say "get the transcript of this video" or "screenshot this page as a PDF" and it just works.

You need a free Apify account and its API token (console.apify.com → Settings → API & Integrations). You pay only for successful results, at the prices listed in the main README.

## Option A: hosted (no install)

Add a remote MCP server with this URL and your token as a Bearer header:

```
https://mcp.apify.com/?actors=siftwright/youtube-transcript-extractor,siftwright/pageframe-screenshots
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
        "siftwright/youtube-transcript-extractor,siftwright/pageframe-screenshots"
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
