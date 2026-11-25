"""Out-of-office auto-reply entry for make.fun.

Writes one funny one-line out-of-office reply to entry.txt, then reads
it back to prove the stored bytes match the reply exactly.
"""

import hashlib
import os
import sys

REPLY = (
    "I'm out until Monday. If you're reading this on Tuesday, I extended "
    "my leave \u2014 and this auto-reply is now the only one of us still working."
)

LIMIT = 160


def reject(why):
    print("entry rejected: " + why, file=sys.stderr)
    raise SystemExit(1)


def main():
    line = REPLY
    if not line.strip():
        reject("reply is blank")
    for bad in ("\n", "\r", "\t"):
        if bad in line:
            reject("reply must be a single line")
    if len(line) > LIMIT:
        reject("reply is %d chars, limit is %d" % (len(line), LIMIT))
    data = line.encode("utf-8")
    if data.endswith(b"\n"):
        reject("reply must not end with a newline")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "wb") as out:
        out.write(data)
    with open(path, "rb") as back:
        saved = back.read()
    if saved != data:
        reject("read-back bytes differ from the reply")
    print("entry.txt: %d chars, %d bytes, sha256 %s"
          % (len(line), len(data), hashlib.sha256(saved).hexdigest()))


if __name__ == "__main__":
    main()
