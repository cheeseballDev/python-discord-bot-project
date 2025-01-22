import discord
import os
from dotenv import load_dotenv

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
    intents = discord.Intents.default()
    intents.message_content = True
    load_dotenv()

    TOKEN = os.getenv('DISCORD_TOKEN')
    client = Client(intents=intents)
    client.run(TOKEN)

if __name__ == "__main__":
    main()