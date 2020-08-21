from discord.ext import commands
import os
import traceback
import urllib.request

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def startserver(ctx):
    req = urllib.request.Request('API_URL')
    with urllib.request.urlopen(req) as res:
    await ctx.send(res.read())


bot.run(token)
