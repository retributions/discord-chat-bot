import discord
import random
import requests

client = discord.Client()

BOT_TOKEN = ""

@client.event
async def on_message(message):
    if message.author.id != client.user.id and message.author != message.author.bot:
        r = requests.get(f"https://api.monkedev.com/fun/chat?msg={message.content}&uid={message.author.id}")
        if r.status_code == 200:
            em = discord.Embed(
                description=r.json()['response'],
                color=random.randint(0, 0xFFFFFF) #random colors 
            )
            await message.channel.send(embed=em)
        elif r.status_code == 400:
            await message.channel.send("Hmm seems like the api is down")

client.run(str(BOT_TOKEN), reconnect=True)
