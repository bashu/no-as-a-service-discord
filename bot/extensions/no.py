import random

import hikari
import lightbulb

from bot import REASONS

loader = lightbulb.Loader()


@loader.command
class No(
    lightbulb.SlashCommand,
    name="no",
    description="Get a random reason to say no",
    hooks=[lightbulb.prefab.sliding_window(10, 1, "user")],
    integration_types=[
        hikari.ApplicationIntegrationType.GUILD_INSTALL,
        hikari.ApplicationIntegrationType.USER_INSTALL,
    ],
    contexts=[
        hikari.ApplicationContextType.GUILD,
        hikari.ApplicationContextType.BOT_DM,
        hikari.ApplicationContextType.PRIVATE_CHANNEL,
    ],
):
    """The /no slash command: replies with a random reason to say no."""

    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        await ctx.respond(random.choice(REASONS))
