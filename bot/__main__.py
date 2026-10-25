import random

import hikari

from bot import REASONS, bot


@bot.listen()
async def on_mention(event: hikari.MessageCreateEvent) -> None:
    """If a non-bot user mentions your bot, respond with a random reason to say no."""

    # Do not respond to bots nor webhooks pinging us, only user accounts
    if not event.is_human:
        return

    me = bot.get_me()
    if me is None:
        return

    if (event.message.guild_id is None) or me.id in event.message.user_mentions_ids:
        await event.message.respond(random.choice(REASONS), reply=True)


bot.run(
    propagate_interrupts=True,  # Any OS interrupts get rethrown as errors.
)
