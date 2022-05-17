# Nelson Dane

import os
import subprocess
import shutil, glob
import discord
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from dotenv import load_dotenv
from discord.ext import commands

URL = 'blank'
TYPE = 'blank'
SAVE_PATH = './saves/'

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.GetFlow()
    gauth.flow.params.update({'access_type': 'offline'})
    gauth.flow.params.update({'approval_prompt': 'force'})
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='ping')
async def ping(ctx):
    print('ponged')
    await ctx.send('pong')

@bot.command(name='musescore')
async def pdf(ctx,URL,TYPE):
        response = 'Processing request...'
        await ctx.send(response)
        temp_path = './temp/'

        # Count downloaded files before
        before = (len([entry for entry in os.listdir(temp_path) if os.path.isfile(os.path.join(temp_path, entry))]))
        subprocess.check_call(['./LibreScore.sh %s %s %s' % (URL, TYPE, temp_path)],shell=True)        
        after = (len([entry for entry in os.listdir(temp_path) if os.path.isfile(os.path.join(temp_path, entry))]))

        if (before + 1) == after:
            response = 'Request Succeeded!'
            await ctx.send(response)

            source_folder = temp_path
            destination_folder = SAVE_PATH

            # Search files with .pdf or mp3 extension in source directory
            pattern = "/*.pdf"
            pattern2 = "/*.mp3"
            files = glob.glob(source_folder + pattern) + glob.glob(source_folder + pattern2)
            # move the files with txt extension
            for file in files:
                gfile = drive.CreateFile({'title': str(file.replace(temp_path,'')),'parents': [{'id': '1muG_CH4zH_ACY2CtX2A3A-b1RGhZEei_'}]})
                # Read file and set it as the content of this instance.
                gfile.SetContentFile(file)
                gfile.Upload() # Upload the file.

                print('Uploaded files!')
                response = 'Uploaded files!'
                await ctx.send(response)

                await ctx.send(file=discord.File(file))

                # extract file name form file path
                file_name = os.path.basename(file)
                shutil.move(file, destination_folder + file_name)
                print('Moved:', file)

                response = 'Moved file to saves!'
                await ctx.send(response)
            
        else:
            response = 'Request failed. Sadge.'
            await ctx.send(response)

bot.run(TOKEN)