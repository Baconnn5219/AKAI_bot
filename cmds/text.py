import discord
from discord.ext import commands 
from core.classes import Cog_Extension
import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Special_react(Cog_Extension):

    @commands.command(aliases=["repeat"])
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command(aliases=["tiwls","tonight",""])
    async def tonight_i_would_like_some(self, ctx):
        random_wafu = random.choice(jdata['Hololive_wafus'])
        await ctx.send(random_wafu)
        
    @commands.command(aliases=["avatar","ava"])
    async def 頭貼(self,ctx, member : discord.Member = None):
        if member == None:
            member = ctx.author
        memberAvatar = member.avatar_url
        avaEmbed = discord.embed(title = f"{member.name}'s avatar!")
        avaEmbed.set_image(url = memberAvatar)
        await ctx.send(embed = avaEmbed)

def setup(bot):
    bot.add_cog(Special_react(bot))