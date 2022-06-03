import discord
from discord.ext import commands, tasks
import datetime, keep_alive, json
from itertools import cycle
from discord_buttons_plugin import *
import os

intents = discord.Intents.all()

client = commands.Bot(command_prefix=commands.when_mentioned_or("["), intents=intents)
buttons = ButtonsClient(client)


with open('setting.json', 'r', encoding='utf8') as jFile:
    jdata = json.load(jFile)

status = cycle(["嗨嗨", "我的前綴是 [ "])


@tasks.loop(seconds=1)
async def status_swap():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_ready():
    print(">> Bot is online <<")
    for guild in client.guilds:
        for channel in guild.text_channels:
            #Send message to the channel ypu want
            if str(channel) == "channel's name":
                await channel.send('我... 醒來啦')
                await channel.send(f"在{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}(UTC+0)的時候甦醒了")
        print('Active in {}\n Member Count : {}'.format(guild.name, guild.member_count))
    status_swap.start()
      
#An invite of bot
#You need to put in the link of yours'
@client.command(name = "invite", description = "邀請指令\n邀請機器人到你的伺服器")
async def invite(ctx):
    embed = discord.Embed(
        title="邀請我",
        color=0xff0000,
        description=
        f"想要邀請我的話, 請按\nIf U want to invite me, please press..."
    )
    embed.add_field(name="from ...", value="hi I'm...", inline=False)
    await buttons.send(
        content=None,
        embed=embed,
        channel=ctx.channel.id,
        components=[
            ActionRow([
                Button(
                    style=ButtonType().Link,
                    label="Invite",                    
                    url=
                    jdata["invite_link"]
                    
                )
            ])
        ])

@client.command(name = "server", description = "伺服器指令\n前往赤井聯邦的連結")
async def server(ctx):
	await buttons.send(
		content="早安你好 來自赤井ベーコン的問候",
		channel = ctx.channel.id,
		components = [
			ActionRow([
                Button(
                    style=ButtonType().Link,
                    label="An invitaion of my server",                    
                    url=jdata["server_link"]
                )
            ])
		]
	)

#load之類的
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')
@client.command()
@client.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cmds.{extension}')
    await ctx.send(f'UnLoaded {extension} done.')
@client.command()
@client.is_owner()
async def reload(ctx, extension):
    client.reload_extension(f'cmds.{extension}')
    await ctx.send(f'ReLoaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        client.load_extension(f'cmds.{filename[:-3]}')

#運行
if __name__ == "__main__":
    #在replit上時需這個
    #keep_alive.keep_alive()      
    client.run(jdata["token"])
  