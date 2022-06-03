import discord
from discord.ext import commands
from core.classes import Cog_Extension 
import math,sys,traceback

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == '哭':
            await msg.channel.send('不哭不哭 眼淚是珍珠 越哭越像豬')
            
        if msg.content == '謝謝':
            await msg.channel.send('不用謝 愛你喔~')

    @commands.Cog.listener()
    async def on_error(ctx, event, *args, **kwargs):
        """Error handler for all events."""
        s = traceback.format_exc()
        content = f'Ignoring exception in {event}\n{s}'
        print(content, file=sys.stderr)
        await ctx.send(f"Error 錯誤:\n{content}")
   
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # if command has local error handler, return
        if hasattr(ctx.command, 'on_error'):
            return

        # get the original exception
        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound):
            await ctx.send("沒這指令啦!(CommandNotFound)")
            return

        if isinstance(error, commands.BotMissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = '我需要 **{}** 的權限.(BotMissingPermissions)'.format(fmt)
            await ctx.send(_message)
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send('指令已停用(DisabledCommand)')
            return

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("這指令冷卻中, 在 {} 秒後重試.(CommandOnCooldown)".format(math.ceil(error.retry_after)))
            return

        if isinstance(error, commands.MissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = '你需要 **{}** 的權限來使用這項指令'.format(fmt)
            await ctx.send(_message)
            return

        if isinstance(error, commands.UserInputError):
            await ctx.send("無效的輸入.")
            return

        if isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send('這指令不能在 DM 中使用')
            except discord.Forbidden:
                pass
            return

        if isinstance(error, commands.CheckFailure):
            await ctx.send("你沒有使用這項指令的權限")
            return

        # ignore all other exception types, but print them to stderr
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)

        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(Event(bot))