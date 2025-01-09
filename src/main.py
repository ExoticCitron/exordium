import os
import discord
from discord.ext import commands
from exordium import get_logger

# Set up Exordium logger
logger = get_logger(__name__)

# Set up Discord bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logger.success(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    logger.info(f'Message from {message.author}: {message.content}')

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
        logger.debug('Responded to !hello command')

    await bot.process_commands(message)

@bot.command(name='ping')
async def ping(ctx):
    logger.debug('Received ping command')
    await ctx.send('Pong!')
    logger.info('Responded to ping command')

@bot.event
async def on_error(event, *args, **kwargs):
    logger.error(f'An error occurred in event: {event}')

@bot.event
async def on_command_error(ctx, error):
    logger.error(f'Command error: {str(error)}')

if __name__ == '__main__':
    token = "MTI0OTcwNDg3MzUzNzA0NDYwMA.G3ekVm.esgDmKAGNudE2_5MrtiR-rbwuYUKr82dY6sZYU"
    if not token:
        logger.critical('No Discord token found. Please set the DISCORD_TOKEN environment variable.')
    else:
        bot.run(token)