import asyncio
import discord
import os
from dotenv import load_dotenv
import yt_dlp

# TO TELL IF BOT RAN SUCCESSFULLY
class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        print(f'{self.user} is now playing music')

    async def on_message(self, message):
        voice_clients = {}
        yt_dl_options = {"format": "bestaudio/best"}
        ytdl = yt_dlp.YoutubeDL(yt_dl_options)

        ffmpeg_options = {'options': '-vn'}

        if message.content.startswith("?play"):
            try:
                voice_client = await message.author.voice.channel.connect()
                voice_clients[voice_client.guild.id] = voice_client
            except Exception as e:
                print(e)

            try:
                url = message.content.split()[1]

                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

                song = data['url']
                player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

                voice_clients[message.guild.id].play(player)

            except Exception as e:
                print(e)

        print(f'Message from {message.author}: {message.content}')
        if (not message.author.bot and message.content == 'hi'):
            await message.channel.send('hi')


## STARTING THE BOT
def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    client.run(TOKEN)


if __name__ == "__main__":
    main()