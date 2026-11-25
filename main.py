"""Out-of-office auto-reply entry for make.fun.

Writes one funny one-line out-of-office reply to entry.txt, then proves
by reading it back that the file holds exactly that reply.
"""

import hashlib
import os
import sys

REPLY = (
    "I'm out until Monday \u2014 I set this reply from a dentist's chair at "
    "9:40, mid-root-canal, because my inbox scares me more than the drill."
)

MAX = 160


def die(note):
    print("entry rejected: " + note, file=sys.stderr)
    raise SystemExit(1)


def main():
    reply = REPLY
    if not reply.strip():
        die("reply is blank")
    if "\n" in reply or "\r" in reply or "\t" in reply:
        die("reply must be exactly one line")
    if len(reply) > MAX:
        die("reply is %d chars, over the %d limit" % (len(reply), MAX))
    blob = reply.encode("utf-8")
    if blob.endswith(b"\n"):
        die("reply must not end with a newline")
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target_dir, exist_ok=True)
    entry_path = os.path.join(target_dir, "entry.txt")
    with open(entry_path, "wb") as handle:
        handle.write(blob)
    with open(entry_path, "rb") as handle:
        check = handle.read()
    if check != blob:
        die("read-back does not match the reply")
    print("entry.txt: %d chars, %d bytes, sha256 %s"
          % (len(reply), len(blob), hashlib.sha256(check).hexdigest()))


if __name__ == "__main__":
    main()
