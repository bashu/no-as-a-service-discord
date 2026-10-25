import json
import math
from pathlib import Path

import hikari
import lightbulb
from environs import Env

from bot import extensions

env = Env()
env.read_env()  # .env is optional; real environment variables take precedence

REASONS = tuple(
    json.loads((Path(__file__).parent / "reasons.json").read_text(encoding="utf-8"))
)

bot = hikari.GatewayBot(
    token=env.str("DISCORD_TOKEN"),
    logs="INFO",
)

client = lightbulb.client_from_app(bot)


@client.error_handler
async def on_error(exc: lightbulb.exceptions.ExecutionPipelineFailedException) -> bool:
    """Tell users when a command is on cooldown; leave every other error to lightbulb."""
    if isinstance(cause := exc.causes[0], lightbulb.prefab.OnCooldown):
        await exc.context.respond(
            f"No. Try again in {math.ceil(cause.remaining)}s.",
            flags=hikari.MessageFlag.EPHEMERAL,
        )
        return True
    return False


@bot.listen(hikari.StartingEvent)
async def on_starting(_: hikari.StartingEvent) -> None:
    """Load command extensions, then start the client so it syncs commands with Discord.

    hikari only logs exceptions raised by event listeners, so without the shutdown below a
    failure here would leave the bot online with no slash commands.
    """
    try:
        await client.load_extensions_from_package(extensions)
        await client.start()
    except Exception:  # noqa: BLE001
        await bot.close()
