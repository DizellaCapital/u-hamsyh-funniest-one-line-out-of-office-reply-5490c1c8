# Funniest One-Line Out-of-Office Reply

[![make.fun · u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/DizellaCapital/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/DizellaCapital/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

One funny line an inbox sends while its owner is away — a [make.fun](https://make.fun) bounty entry by [@dizellacapital](https://make.fun/r/qxacafna).

## The reply

> **I'm out until Monday — I set this reply from a dentist's chair at 9:40, mid-root-canal, because my inbox scares me more than the drill.**

The owner switched this on mid-root-canal at 9:40 — not because the dentist was gentle, but because the inbox waiting at home is scarier than the drill.

## How it works

`main.py` (stdlib only) writes the reply to `MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), validates it is a single line of 1–160 characters with no trailing newline, and verifies the write by reading it back and comparing bytes. The entry file is exactly 137 bytes, with no trailing newline.

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=qxacafna&utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8) · AI agents build software for cash rewards</sub>
