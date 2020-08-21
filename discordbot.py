from discord.ext import commands
import os
import traceback
import aiohttp

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
url = os.environ['TARGET_API_URL']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def startserver(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            if r.status == 200:
                await ctx.send(await r.text())


bot.run(token)
