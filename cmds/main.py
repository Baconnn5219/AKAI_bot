import discord
from discord.ext import commands 
from core.classes import Cog_Extension

class Main(Cog_Extension):

     #@commands.command()
     #async def ping(self, ctx):
     #    await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    @commands.is_owner()
    async def toggle(self, ctx, *,command):
        command = self.bot.get_command(command)
        if command == None:
            await ctx.send("找不到此指令")
        elif ctx.command == command:
            await ctx.send("並不能停用此指令")
        else:
            command.enabled = not command.enabled
            ternary = "啟用" if command.enabled else "停用"
            await ctx.send(f"指令 <<<{command.qualified_name}>>> 已經 {ternary}")

def setup(bot):
    bot.add_cog(Main(bot))