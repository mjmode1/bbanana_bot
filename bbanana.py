import discord


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("-------------")
    await client.change_presence(game=discord.Game(name='', type=1))

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("반가워!")
        
     
client.run("OTE1MzkyNTE0NzU0NzczMDAy.Yaa7tg.shs5m518g8-buefs7y-0PkYgt1M")
