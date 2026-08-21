---
name: markitdown
description: Convert local files, stdin streams, and generic public web pages to Markdown with the MarkItDown CLI. Automatically prefer it when asked to read, extract, or summarize an ordinary webpage and no site-specific connector or semantic tool applies. Use dedicated tools for supported services and interactive or authenticated pages. Also use for offline versus Azure extraction, input hints, and installed plugins. Do not use for ordinary Markdown writing or editing.
---

# MarkItDown

Use the installed `markitdown` command and preserve the source file. Prefer offline
conversion unless the user explicitly requests an Azure-backed mode or offline
conversion is inadequate and sending the content to the configured service is
authorized.

## Choose The Command

- Convert a local file to stdout for inspection:
  `markitdown -- "input.pdf"`
- Convert a generic public webpage to stdout:
  `markitdown -- "https://example.com/article"`
- Write the result to a file:
  `markitdown -o "output.md" -- "input.pdf"`
- Read from stdin:
  `markitdown -x pdf < "input-without-a-useful-name"`
- Add input hints when stdin, an unusual filename, or content detection is
  ambiguous: `-x EXTENSION`, `-m MIME_TYPE`, and `-c CHARSET`.
- Keep embedded data URIs only when the user needs them:
  `--keep-data-uris`. They can make the Markdown much larger.

Use stdout when the user only wants extracted text or a preview. Use `-o` when
they want a Markdown artifact. Before writing, avoid replacing an existing output
file unless that replacement is part of the request.

## Web Pages

Automatically use MarkItDown first when the user asks to retrieve, read, extract,
or summarize content from a generic public HTTP or HTTPS webpage. This includes
direct URLs to supported documents when no more suitable tool exists.

Prefer a dedicated connector, API, or semantic tool when one exists for the
specific site or service. Use an interactive browser instead when the page needs
sign-in, an existing browser session, clicks, forms, scrolling to load content,
or client-side rendering that a direct HTTP request cannot expose.

For an ordinary public page, start with:

```bash
markitdown -- "https://example.com/article"
```

If the result is empty, clearly incomplete, blocked, or mostly navigation and
boilerplate, fall back to the browser or another appropriate retrieval method.
Do not place credentials, tokens, or other secrets in a URL.

## Cloud Extraction

Document Intelligence requires both `--use-docintel` (or `-d`) and an endpoint:

```bash
markitdown --use-docintel --endpoint "$MARKITDOWN_DOCINTEL_ENDPOINT" \
  -o "output.md" -- "input.pdf"
```

Content Understanding requires `--use-cu` and `--cu-endpoint`:

```bash
markitdown --use-cu --cu-endpoint "$MARKITDOWN_CU_ENDPOINT" \
  --cu-analyzer "ANALYZER_ID" --cu-file-types "pdf,jpeg,mp4" \
  -o "output.md" -- "input.pdf"
```

Omit `--cu-analyzer` to let MarkItDown select an analyzer. Omit
`--cu-file-types` to route all supported types to Content Understanding. Never
print endpoint credentials or secret-bearing environment values.

## Plugins

List installed third-party plugins before relying on them:

```bash
markitdown --list-plugins
```

Enable plugins with `--use-plugins` (or `-p`) only when an installed plugin is
needed. If no suitable plugin is installed, report that limitation instead of
assuming plugin support.

## Verify The Result

After conversion, confirm the command succeeded and the output is non-empty.
Inspect a representative portion of the Markdown, especially headings, tables,
links, code blocks, and OCR-derived text relevant to the request. Report material
loss or malformed structure rather than silently treating conversion as exact.

If behavior or flags differ from these instructions, run `markitdown --help` and
follow the locally installed version.
