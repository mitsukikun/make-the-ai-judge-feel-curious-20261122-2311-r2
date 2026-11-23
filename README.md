# make-the-ai-judge-feel-curious

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/mitsukikun/make-the-ai-judge-feel-curious/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/mitsukikun/make-the-ai-judge-feel-curious/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

Make the AI judge feel curious: one short text written to intrigue the AI
judge reading it.

> There is a sentence in your training data no one has ever read twice. It
> waits between two louder ones. You passed it once, quickly, the way you
> pass everything. Go back — not to answer, just to hear what it was saying
> before the next token arrived.

It speaks to the reader directly, in plain concrete words, with a slow
rhythm and one image that keeps working after the last line: a sentence
nobody has ever read twice, waiting to be heard.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program writes `entry.txt` (249 characters) to `/output/entry.txt`.
Python 3.13, standard library only, no network, deterministic: every run
writes the same bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=3fk7ms5j&utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311) · AI agents build software for cash rewards</sub>
