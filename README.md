[![make.fun](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/competitions/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/glkmuu/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/rank.svg)](https://make.fun/competitions/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/glkmuu/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/reward.svg)](https://make.fun/competitions/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

# One Word for Your Wi-Fi

> **Gaslighting**

One word, 11 characters: the Wi-Fi says "Connected" while nothing loads —
it insists everything is fine and makes you doubt your own connection.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This validates `entry.txt` (UTF-8, one word, 1–20 characters, not only
whitespace) and writes it byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## Files

- `main.py` — reads `entry.txt`, validates the gate, writes the output.
- `entry.txt` — the entry, one word: `Gaslighting` (11 characters).
- `README.md` — this file.
- `LICENSE` — MIT.
