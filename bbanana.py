
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("빠나나봇")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("반가워!")
        
client.run("OTE1MzkyNTE0NzU0NzczMDAy.Yaa7tg.shs5m518g8-buefs7y-0PkYgt1M")