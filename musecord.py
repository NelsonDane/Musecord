# By Nelson Dane
# Discord bot to download PDFs and mp3's from musescore and send in discord chat

import os
import subprocess
import glob
import discord
from dotenv import load_dotenv
from discord.ext import commands

# Add exceptions later for incorrectly typed commands
URL = 'blank'
TYPE = 'blank'
temp_path = "./temp/"

# Load .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot prefix
bot = commands.Bot(command_prefix='!')
print('Musecord bot is started...')

# Bot ping-pong
@bot.command(name='ping')
async def ping(ctx):
    print('ponged')
    await ctx.send('pong')

# Massive command
@bot.command(name='musecord')
async def pdf(ctx,URL,TYPE):
        response = 'Processing request...'
        await ctx.send(response)

        # Count downloaded files before and after download to see if anything downloaded
        before = (len([entry for entry in os.listdir(temp_path) if os.path.isfile(os.path.join(temp_path, entry))]))
        subprocess.check_call(['./LibreScore.sh %s %s %s' % (URL, TYPE, temp_path)],shell=True)        
        after = (len([entry for entry in os.listdir(temp_path) if os.path.isfile(os.path.join(temp_path, entry))]))

        if (before + 1) == after:
            response = 'Request Succeeded!'
            await ctx.send(response)

            # Search files with .pdf or mp3 extension in source directory
            pattern = "/*.pdf"
            pattern2 = "/*.mp3"
            files = glob.glob(temp_path + pattern) + glob.glob(temp_path + pattern2)

            for file in files:
                # Send file to discord
                await ctx.send(file=discord.File(file))
                print('Sent file in Discord!')
                os.remove(file)
                print('Removed file')
                await ctx.send('Process complete!')
                print('Process complete!')
        else:
            response = 'Request failed. Sadge.'
            await ctx.send(response)

bot.run(TOKEN)
