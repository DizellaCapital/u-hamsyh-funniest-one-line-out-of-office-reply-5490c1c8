"""Out-of-office auto-reply entry for make.fun.

Writes one funny one-line out-of-office reply to entry.txt and checks
the stored file byte-for-byte against the reply before finishing.
"""

import hashlib
import os
import sys

REPLY = (
    "I'm away until the 30th. Urgent matters go to Priya \u2014 she has my "
    "password, my calendar, and strict orders to pretend she never met me."
)

CHAR_LIMIT = 160


def abort(reason):
    print("entry rejected: " + reason, file=sys.stderr)
    raise SystemExit(1)


def main():
    reply = REPLY
    if not reply.strip():
        abort("reply is blank")
    if any(mark in reply for mark in ("\n", "\r", "\t")):
        abort("reply must be exactly one line")
    if len(reply) > CHAR_LIMIT:
        abort("reply is %d chars, limit is %d" % (len(reply), CHAR_LIMIT))
    blob = reply.encode("utf-8")
    if blob.endswith(b"\n"):
        abort("reply must not end with a newline")
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(directory, exist_ok=True)
    destination = os.path.join(directory, "entry.txt")
    with open(destination, "wb") as writer:
        writer.write(blob)
    with open(destination, "rb") as reader:
        kept = reader.read()
    if kept != blob:
        abort("stored bytes differ from the reply")
    print("entry.txt: %d chars, %d bytes, sha256 %s"
          % (len(reply), len(blob), hashlib.sha256(kept).hexdigest()))


if __name__ == "__main__":
    main()
