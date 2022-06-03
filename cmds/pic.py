import discord
from discord.ext import commands
from core.classes import Cog_Extension 
import json
import random
import asyncio

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Pic(Cog_Extension):

   @commands.command()
   async def 單抽(self, ctx):
      random_pic = random.choice(jdata['url_pic'])
      await ctx.send('恭喜你獲得一張香圖')
      await ctx.send(random_pic)
      await ctx.send('香吧 :sweat_drops: :sweat_drops: :sweat_drops:')

   @commands.command()
   async def 超絕十連(self, ctx):
      await ctx.send('恭喜你獲得十張香圖')
      for i in range(10):
         random_pic = random.choice(jdata['url_pic'])
         await ctx.send(random_pic)
      
      await ctx.send('香吧 :sweat_drops: :sweat_drops: :sweat_drops:')

   @commands.command()
   async def 究極百連(self, ctx):
      await ctx.send('封印解開')
      await ctx.send('倒數十秒 非戰鬥人員另先行撤離')
      num = 10
      msg = await ctx.send(num)
      num = num-1
      for t in range(num,0,-1):
        await asyncio.sleep(1)
        await msg.edit(content=f"{t}")  
      await msg.purge()
      await ctx.send('https://youtu.be/dQw4w9WgXcQ')

      #for i in range(100):
      #   random_pic = random.choice(jdata['url_pic'])
      #   await ctx.send(random_pic)
      #await ctx.send('香吧 :sweat_drops: :sweat_drops: :sweat_drops:')

def setup(bot):
    bot.add_cog(Pic(bot))