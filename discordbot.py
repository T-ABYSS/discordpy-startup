from discord.ext import commands
import os
import traceback
import boto3

InstanceId = 'EC2_INCETANCE_ID'

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


def start_instances():
    client = boto3.client('ec2')
    response = ec2_client().start_instances(
        InstanceIds=[
            InstanceId
        ]
    )


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def stert_server(ctx):
    await start_instances()
    await ctx.send('起動命令を受け付けました')


bot.run(token)
