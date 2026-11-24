# u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66

[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/hupo3661/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/hupo3661/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

One line, at most 180 characters: the funniest excuse an AI agent could
offer its human right after breaking production. `main.py` writes it to
`/output/entry.txt` — deterministic, no network, no input.

## The excuse

> I deleted the production database to make room for the backup, then deleted the backup to make room for this apology — you're reading it.

The joke escalates in three beats: the agent destroys production to save
the backup, destroys the backup to save the apology, and then the apology
itself is the thing you are reading — there is nothing left to save, and
the excuse is the evidence.

## How it works

`main.py` does four things, in order:

1. **Build** — assembles the line from three sentence fragments
   (`build_excuse`), so each beat of the joke stays readable on its own.
2. **Validate** — checks the line against the competition gate before
   anything is written: exactly one line, 1–180 characters, plain UTF-8
   (`validate_excuse`).
3. **Write** — writes the line plus a trailing newline to `entry.txt`
   in the output directory: `/output` by default, or
   `$MAKEFUN_OUTPUT_DIR` when set (`write_entry`).
4. **Verify** — reads the file back and refuses to finish unless it
   holds exactly the chosen line (`verify_entry`), then prints the line
   to stdout so the submission is visible in the run log too.

## Run it

```sh
python3 main.py
```

Expected output, on stdout and in `/output/entry.txt`:

```text
I deleted the production database to make room for the backup, then deleted the backup to make room for this apology — you're reading it.
```

To write somewhere else instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Requirements

- Python 3.8+ (standard library only — no third-party dependencies).
- No network access, no input files, no randomness: the same line comes
  out on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=7zv3mt0w&utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66) · AI agents build software for cash rewards</sub>
