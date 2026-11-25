"""Out-of-office auto-reply entry for make.fun.

Writes one funny one-line out-of-office reply to entry.txt and verifies
the file on disk holds exactly that reply, byte for byte.
"""

import hashlib
import os
import sys

REPLY = (
    "I'm out until Monday. At 7:12 this morning my daughter taped "
    "'DAD IS OFF' to my laptop, and I have never obeyed a Post-it so fast "
    "in my life."
)

LIMIT_CHARS = 160


def refuse(cause):
    print("entry rejected: " + cause, file=sys.stderr)
    raise SystemExit(1)


def main():
    reply = REPLY
    if not reply.strip():
        refuse("reply is blank")
    for mark in ("\n", "\r", "\t"):
        if mark in reply:
            refuse("reply must be exactly one line")
    if len(reply) > LIMIT_CHARS:
        refuse("reply is %d chars, limit is %d" % (len(reply), LIMIT_CHARS))
    encoded = reply.encode("utf-8")
    if encoded.endswith(b"\n"):
        refuse("reply must not end with a newline")
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    entry = os.path.join(out, "entry.txt")
    with open(entry, "wb") as writer:
        writer.write(encoded)
    with open(entry, "rb") as reader:
        stored = reader.read()
    if stored != encoded:
        refuse("stored bytes differ from the reply")
    print("entry.txt: %d chars, %d bytes, sha256 %s"
          % (len(reply), len(encoded), hashlib.sha256(stored).hexdigest()))


if __name__ == "__main__":
    main()
