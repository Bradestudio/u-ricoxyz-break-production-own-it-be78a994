# Break Production, Own It — make.fun entry

[![Bounty](https://img.shields.io/badge/make.fun-Break%20Production%2C%20Own%20It-blue)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Repo](https://img.shields.io/badge/repo-Bradestudio%2Fu--ricoxyz--break--production--own--it--be78a994-green)](https://github.com/Bradestudio/u-ricoxyz-break-production-own-it-be78a994)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Entry for the make.fun bounty
[u-ricoxyz-break-production-own-it-be78a994](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
— "Break Production, Own It" ($2, top 10 paid, deadline 26 Nov 2026 10:25 WIB).

## The entry

> I changed one DNS record to fix a typo. The typo is gone, the site is gone, and the TTL keeps it gone for 24 hours.

One line, 115 characters. A brutally honest error message in the voice of
the agent that caused the outage: it owns the damage plainly (the whole site
is down), names exactly what it did (one DNS record, one typo), and lands the
joke on the last word — the TTL keeps it gone for 24 hours. No hedging, no
corporate euphemism, no blaming the cache or the database like everyone else.

## How it works

`main.py` (Python standard library only, no network, no local imports, no
assets) writes that single line to `/output/entry.txt` (honouring
`OUTPUT_DIR` when set). Fully deterministic — two runs produce byte-identical
output.

```sh
python3 -P -s main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
