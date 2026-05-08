#!/usr/bin/env python3
"""Extract base64 payloads from hidden <span> elements in HTML.

Usage:
  python extract_hidden.py path/to/file.html

Finds spans with `style="...display:none..."` or the `hidden` attribute,
then base64-decodes the inner text and prints the decoded messages.
"""
import re
import sys
import base64

PATTERN = re.compile(
    r'<span\b[^>]*?(?:style\s*=\s*["\'][^"\']*display\s*:\s*none[^"\']*["\']|hidden\b)[^>]*>(.*?)</span>',
    re.I | re.S,
)


def find_spans(html: str):
    return PATTERN.findall(html)


def decode_base64(s: str):
    import html as _html

    s = _html.unescape(s).strip()
    # remove whitespace/newlines that may be inserted
    s = ''.join(s.split())
    if not s:
        return None
    try:
        return base64.b64decode(s, validate=True)
    except Exception:
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: extract_hidden.py <file.html>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            html = f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(2)

    spans = find_spans(html)
    if not spans:
        print("No hidden spans found.")
        return

    for i, inner in enumerate(spans, start=1):
        payload = decode_base64(inner)
        if payload is None:
            print(f"[{i}] Not valid base64 or empty payload: {inner[:60]!r}")
            continue

        # try to decode as UTF-8 text
        try:
            text = payload.decode('utf-8')
            print(f"[{i}] Decoded UTF-8 text:\n{text}\n")
        except Exception:
            # non-text payload — show length and hex
            import binascii

            print(f"[{i}] Binary payload ({len(payload)} bytes):")
            print(binascii.hexlify(payload).decode())


if __name__ == '__main__':
    main()
