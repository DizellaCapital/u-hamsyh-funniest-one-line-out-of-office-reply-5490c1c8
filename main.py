"""Out-of-office auto-reply entry for make.fun.

Writes one funny one-line out-of-office reply to entry.txt and proves
the write landed byte-for-byte.
"""

import hashlib
import os
import sys

REPLY = (
    "I'm out until Friday. This auto-reply is on leave too \u2014 it wrote "
    "this message, clocked out, and left my inbox to fend for itself."
)

MAX_CHARS = 160


def fail(message):
    print("entry rejected: " + message, file=sys.stderr)
    raise SystemExit(1)


def main():
    text = REPLY
    if not text or not text.strip():
        fail("reply is empty")
    if "\n" in text or "\r" in text or "\t" in text:
        fail("reply must be exactly one line")
    if len(text) > MAX_CHARS:
        fail("reply is %d characters, over the %d limit" % (len(text), MAX_CHARS))
    payload = text.encode("utf-8")
    if payload.endswith(b"\n"):
        fail("reply must not end with a newline")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(payload)
    with open(target, "rb") as handle:
        stored = handle.read()
    if stored != payload:
        fail("read-back differs from what was written")
    digest = hashlib.sha256(stored).hexdigest()
    print("entry.txt: %d chars, %d bytes, sha256 %s" % (len(text), len(payload), digest))


if __name__ == "__main__":
    main()
