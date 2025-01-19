import discord
import os
from dotenv import load_dotenv

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
        await message.channel.send(message.content)

def main():
    intents = discord.Intents.default()
    intents.message_content = True

    load_dotenv()
    client = Client(intents=intents)
    client.run(os.getenv('DISCORD_TOKEN'))


if __name__ == "__main__":
    main()