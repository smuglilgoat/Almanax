# Almanax

A Discord bot that shows the Almanax of the day for DOFUS.

## What it does

- `$day` — posts an embed with today's Almanax: type, effect, quest, offering and item image, linking to the Krosmoz page for the date.
- `$ping` — replies with the bot latency.

The daily data is read from `almanax.json`, keyed by `DD/MM`, with `itemImage`, `quest`, `type`, `effect` and `offering` fields. The bot uses the `$` command prefix.

## Stack

- Python 3.8+
- `discord.py` 1.0
- Flask (keep-alive endpoint)
- Poetry for dependencies

## Getting started

```bash
poetry install
export TOKEN="<discord bot token>"
poetry run python main.py
```

The token is read from the `TOKEN` environment variable. `almanax.json` must be in the working directory.

`keep_alive.py` starts a small Flask server on port 8080 in a background thread; it exists for hosts that require an open web port and is not needed to run the bot locally.

## Roadmap

- [x] Today's Almanax as an embed
- [x] Keep-alive for hosting
- [ ] Help command
- [ ] Week view
- [ ] Automatic daily post
- [ ] Automatic data fetching
