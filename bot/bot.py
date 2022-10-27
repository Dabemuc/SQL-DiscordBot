import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == client.user:
            return

        print(f'Message from {message.author}: {message.content}')
        await message.channel.send(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)


client.run("MTAzNTExMTQ0MzU1MDQ1NzkyNw.GoUUc2.oQYFm_yNzCb1X35BaXpFI8YWR2ietiibyhIHDM")
