# By Nelson Dane
# Discord bot to download PDFs, mp3's, and MIDI's

import os
import sys
import subprocess
import glob
import validators
import discord
from dotenv import load_dotenv
from discord.ext import commands

# Load .env
load_dotenv()

# Exit if no token is found
if not os.environ["DISCORD_TOKEN"]:
    print('Please set the DISCORD_TOKEN environment variable.')
    exit(1)

# Get the bot's token from the .env
TOKEN = os.getenv('DISCORD_TOKEN')
# If token is empty, then exit
if not TOKEN:
    print('Please set the DISCORD_TOKEN environment variable.')
    sys.exit(1)

# Path to save files
save_path = "./downloads/"

# Bot command prefix
bot = commands.Bot(command_prefix='!')
print('Musecord bot is started...')

# Bot ping-pong
@bot.command(name='ping')
async def ping(ctx):
    print('ponged')
    await ctx.send('pong')

# Massive command for file downloads
@bot.command(name='musecord')
async def pdf(ctx,URL,TYPE):

        # Valide user input
        if not validators.url(URL):
            print('Invalid URL')
            await ctx.send('Invalid URL')
        elif "musescore.com" not in URL:
            print('Invalid musescore URL. Please use a url from musescore.com')
            await ctx.send('Invalid musescore URL. Please use a url from musescore.com')
        elif TYPE not in ['pdf','mp3','midi']:
            print('Invalid file type. Please use pdf, mp3, or midi')
            await ctx.send('Invalid file type. Please use pdf, mp3, or midi')
        else:
            # Send start message
            await ctx.send('Processing request...')

            # Count downloaded files before
            before = (len([entry for entry in os.listdir(save_path) if os.path.isfile(os.path.join(save_path, entry))]))
            # Download file with external script since idk how else to do it
            subprocess.check_call(['./LibreScore.sh %s %s %s' % (URL, TYPE, save_path)], shell=True)        
            # Count downloaded files after to see if anything was downloaded
            after = (len([entry for entry in os.listdir(save_path) if os.path.isfile(os.path.join(save_path, entry))]))

            # If there is a difference of 1, then a file was downloaded
            if (before + 1) == after:
                response = 'Request Succeeded!'
                await ctx.send(response)

                # Search files with wanted extensions in source directory
                pattern = "/*.pdf"
                pattern2 = "/*.mp3"
                pattern3 = "/*.mid"
                pattern4 = "/*.midi"
                files = glob.glob(save_path + pattern) + glob.glob(save_path + pattern2) + glob.glob(save_path + pattern3) + glob.glob(save_path + pattern4)

                # Send files to discord and then remove them
                for file in files:
                    await ctx.send(file=discord.File(file))
                    print('Sent file in Discord!')
                    os.remove(file)
                    print('Removed file')
                    await ctx.send('Process complete!')
                    print('Process complete!')
            # Else if there was no difference, then send an error
            else:
                print('Request failed. Sadge.')
                await ctx.send('Request failed. Sadge.')

bot.run(TOKEN)
