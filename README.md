# Musecord
A discord bot to download music PDFs, MP3's, and MIDI's from musescore.com

Made possible using the Command-line tool of [dl-librescore](https://github.com/LibreScore/dl-librescore). Go give them a ⭐

## Installation
### Docker
1. Just run `docker run -e DISCORD_TOKEN="YourBotToken" -it --restart unless-stopped --name musecord nelsondane/musecord`, inserting your discord bot token.
2. The bot should send a starting message. Upon receiving this, just enter CTRL-p then CTRL-q to exit gracefully, letting the bot run in the background

### Python Script
Make sure python3-pip is installed
1. Clone this repository and cd into it
2. Run `pip install -r requirements.txt`
3. Add `DISCORD_TOKEN=YourBotToken` to your .env file
4. Run 'python musecord.py

## Usage
Once the bot is invited to your server, you can check that it's running by sending `!ping`, to which the bot should respond with `pong`

To download your desired files, just send a message of this format in discord:
`!musecord <musescore.com url> <filetype>`

For example, to download the PDF of this [piano cover](https://musescore.com/user/5345596/scores/2796891), you'd run:
`!musecord https://musescore.com/user/5345596/scores/2796891 pdf`

After a few seconds, the bot will send the PDF in the discord chat!
Note: the first run may take a few seconds since the bot needs to download the initial program. After that it should be a lot faster!

Supported filetypes:
- pdf
- mp3
- midi
