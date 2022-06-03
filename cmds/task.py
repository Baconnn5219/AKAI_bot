import discord
from discord.ext import commands 
from core.classes import Cog_Extension
import json, asyncio, datetime, random

class Task(Cog_Extension):   
    
    @commands.command(aliases=["time"])
    async def now(self, ctx):
      def gettime():
        x = datetime.datetime.now()
        err = datetime.timedelta(hours=8)
        x += err
        y = x.year
        m = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'][x.month - 1]
        d = x.day
        h = x.hour
        mi = x.minute
        s = x.second
        w = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][(x.weekday() + 1) % 7]
        res = f"{y} / {m} / {d} , {h} : {mi} : {s} , {w}"
        return res
      await ctx.send(gettime())
      #取自其他大佬 感謝他

    @commands.command(aliases=["cd"])
    async def countdown(self, ctx, num : int):
      await ctx.send("let's countdown!")
      msg = await ctx.send(num)
      num = num-1
      for t in range(num,0,-1):
        await asyncio.sleep(1)
        await msg.edit(content=f"{t}")        
      await msg.delete()
      await ctx.send("finish")

def setup(bot):
    bot.add_cog(Task(bot))