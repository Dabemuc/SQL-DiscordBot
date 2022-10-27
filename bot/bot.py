import json
import discord
import mariadb

con = mariadb.connect(user='root', password='password',
                              host='127.0.0.1',
                              port=3307,
                              database='dcBot')

cur = con.cursor()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == client.user:
            return

        print(f'Message from {message.author}: {message.content}')
        await message.channel.send(f'Message from {message.author}: {message.content}')

        if(message.content.__contains__("Query: ")):
            query = message.content.replace("Query: ", "")
            print(query)
            cur.execute(query)
            for data in cur:
                print({data})
                await message.channel.send("Data aus db: " + repr({data}));

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run("OTYyNDc1NjU2NzQ1MTkzNjEy.YlIFTg.6F0vrFOglCvXsXI7bNVjd4vsJuk")
#client.run("MTAzNTExMTQ0MzU1MDQ1NzkyNw.GoUUc2.oQYFm_yNzCb1X35BaXpFI8YWR2ietiibyhIHDM")
