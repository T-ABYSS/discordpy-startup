from discord.ext import commands
import os
import traceback
import boto3

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
instance = 'EC2_INCETANCE_ID'

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def stert_server(ctx):
#    client = boto3.client('ec2')
#    response = ec2_client().start_instances(instances=instance)
    await ctx.send('Accept.')


bot.run(token)
