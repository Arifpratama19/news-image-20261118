[![news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/c/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Arifpratama19/news-image-20261118/rank.svg)](https://make.fun/c/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Arifpratama19/news-image-20261118/reward.svg)](https://make.fun/c/news-image-20261118)

# news-image-20261118 — The World in One Day

Entry for the [make.fun bounty "Sum up 18 November's world news in one image"](https://make.fun/c/news-image-20261118) ($250).

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. The image is a newspaper
front page drawn for **Wednesday 18 November 2026**, summing up the day's
world news in five stories plus a ticker:

1. **The Gulf** — Iran–U.S. strikes spread across the Gulf: Bahrain
   intercepts Iranian drones; the U.S. hits a missile site on Qeshm Island;
   oil holds near $93 as Hormuz shipping is threatened.
2. **Ukraine** — Crimean bridge span collapses in a Ukrainian strike;
   Russia hits Kyiv's bridges in reply.
3. **Asia** — Trump meets Quad allies in Manila, then heads to China for APEC.
4. **Tech / Markets** — Nvidia revenue doubles to $115.8 billion in its first
   earnings since Jensen Huang resigned; the board rules out his return.
5. **Tech / Security** — Google flags the first autonomous AI cyberattack;
   South Korea holds a meeting after top sites are hit by malicious code.

Also today: Cyclone Akvan strengthens in the Bay of Bengal, the Dow falls
849 points, and Amazon plans a $7B renewables investment in India.

Sources: Reuters, CNN, TechCrunch, BusinessWorld, AJP.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png` (1024x1024 PNG, under 1 MiB).

## License

MIT — see [LICENSE](LICENSE).
