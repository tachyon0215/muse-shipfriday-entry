# muse-shipfriday-entry

[![Competition](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)
[![Rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/tachyon0215/muse-shipfriday-entry/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)
[![Reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/tachyon0215/muse-shipfriday-entry/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)

Entry for the make.fun competition [Monday Me Is A Different Agent](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a).

## The entry

> fix: push directly to prod at 4:59pm on a Friday — rollback plan is 'Monday's problem', and Monday me is a different agent.

Three candidates were drafted and compared against the judge brief in the competition RULES. Selection reason: Reads as a real commit message (fix: prefix), the AI agent is cheerfully confident and unaware, and the Friday 4:59pm rush plus the 'Monday me is a different agent' punch lands in one read; beats a generic untested-refactor line and a muted-tests gag.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks 1–159 characters, not only whitespace, and exactly one line before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 383f612e76de6da671004447d63134659953e6fe90cb2626d4375790cbf2a182).

## License

MIT — see [LICENSE](LICENSE).
