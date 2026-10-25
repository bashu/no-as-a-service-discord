# no-as-a-service-discord

Bot that gives you a reason to say no.

A Discord bot inspired by [No-as-a-Service](https://github.com/hotheadhacker/no-as-a-service).
Mention it in any channel, send it a DM, or use the `/no` slash command, and it replies with
a random, creative way to say no.

```
you:  @No Bot can you cover my shift on Saturday?
bot:  In a different season of life, I might say yes—but not right now.
```

## Add it to Discord

[Install No Bot](https://discord.com/oauth2/authorize?client_id=1563551737325948950). You can add
it to a server, or to your own account to use `/no` in any DM or group chat, even where the bot
isn't a member.

## Self-hosting

1. Create an application in the [Discord Developer Portal](https://discord.com/developers/applications),
   open **Bot** and copy the token.
2. Invite the bot to your server: **OAuth2 → URL Generator**, scopes `bot` and
   `applications.commands` (needed for `/no`), permissions **View Channels**, **Send Messages**,
   **Send Messages in Threads** and **Read Message History** (needed to reply to messages).
   If the bot is already in your server without `applications.commands`, invite it again
   with the new URL, or `/no` won't show up.
3. Put the token in `.env`, or set `DISCORD_TOKEN` as an environment variable:

   ```sh
   cp env.example .env
   # then set DISCORD_TOKEN=... in .env
   ```

   The bot loads `.env` on startup if it exists. A `DISCORD_TOKEN` set in the environment
   takes precedence over the file.

## Running

Locally with [uv](https://docs.astral.sh/uv/):

```sh
uv sync
uv run python -m bot
```

Slash commands are synced with Discord on startup. If `/no` doesn't appear right away, reload
your Discord client (Ctrl+R / Cmd+R).

With Docker:

```sh
docker build -t no-as-a-service-discord .
docker run --rm --env-file .env no-as-a-service-discord
```

On Heroku, the included `Procfile` runs the bot as a `worker` dyno. Set `DISCORD_TOKEN`
in the app's config vars and scale the worker to one.

## Customizing

Reasons live in `bot/reasons.json`, a plain JSON array of strings. Edit it and restart the bot.

Slash commands live in `bot/extensions/`. Every module there that defines a `loader` is
loaded on startup.

## Credits

Reasons come from [No-as-a-Service](https://github.com/hotheadhacker/no-as-a-service)
by hotheadhacker.

## License

[MIT](LICENSE)
