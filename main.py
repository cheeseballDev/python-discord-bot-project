import discord
import os
from dotenv import load_dotenv
import yt_dlp

# TO TELL IF BOT RAN SUCCESSFULLY
class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if (not message.author.bot and message.content == 'hi'):
            await message.channel.send('hi')

    


## STARTING THE BOT
def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents)
    client.run(TOKEN)

    run_bot(client)

def run_bot(client):
    voice_clients = {}
    yt_dl_options = {"format": "bestaudio/best"}
    ytdl = yt_dlp.YoutubeDL(yt_dl_options)

    ffmpeg = {'options': '-vn'}

    @client.event
    async def on_ready():
        print(f'{client.user} is now playing music')

    @client.event
    async def on_message(message):
        pass

if __name__ == "__main__":
    main()