# news-image-20261126-bot

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/Akd170396/news-image-20261126-bot/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/Akd170396/news-image-20261126-bot/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Entry for the make.fun bounty **"Sum up 26 November's world news in one image"**
(news-image-20261126, $100 prize pool).

## The entry

`entry.png` is a one-page newspaper front page — **THE WORLD TODAY** — summing up
Thursday 26 November 2026: 40 stories first reported that day, with sources.

- **4 big stories, illustrated:** US tariffs on 14 trading partners; Kim Jong Un
  ordering wider tactical nuclear deployment; the Dow topping 50,000 for the
  first time; Ukraine striking a Russian air base.
- **12 stories in brief** and **24 one-liners**, from Sudan and Gaza to the
  Champions League and the NASA asteroid crater.
- **THE DAY IN UTC** strip and a **DATE CHECK** box listing older stories that
  were deliberately left out.
- Every story carries its source (Reuters, BBC, KCNA, C54, sports wires) —
  see `SOURCES.md` for the full list.

## How it works

The image is rendered locally by `render.py` (Pillow, DejaVu fonts; all
illustrations are simple geometric drawings, no photographs). `main.py` is
standard-library only: it copies the committed `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, so the graded run is deterministic.

```sh
# re-render the image (needs Pillow)
python3 render.py

# run the entry program
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Links

- Bounty: https://make.fun/bounty/news-image-20261126
- make.fun: https://make.fun/?ref=s3svssng&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126

## License

MIT — see [LICENSE](LICENSE).
