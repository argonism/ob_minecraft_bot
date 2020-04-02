from discord.ext import commands
import re
import random

class MinecraftCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')

    @commands.command()
    async def neko(self, ctx):
        await ctx.send('にゃーん:cat:')

    @commands.command()
    async def search(self, ctx, arg): 
        for msg in await ctx.pins():
            if re.search(arg, msg.content):
                await ctx.send(msg.content)

    @commands.command()
    async def pin(self, ctx):
        new_text = ctx.message.content.replace("/pin ", "")
        new_msg = await ctx.send(new_text)
        await new_msg.pin()

    @commands.command()
    async def help(self, ctx):
        template = """
        おいらはマイクラで便利に使えそうなボットだぜ
        追加して欲しい機能とかあったら言ってくれれば気分で追加するだぜ

        :::: 命令一覧 ::::
        /ping   応答確認
        /neko   にゃーん

        /search (検索文字列)
                例: /search ネザー 
                ピン留めされたメッセージの中から、
                検索文字列を含むメッセージを表示する。
                :warning:   /search   と   (検索文字列)   との間の半角空白に注意

        /pin
                例; /pin -2251/150/-35  経験値トラップ
                これをメッセージの先頭につけてメッセージを送ると、
                先頭の /pin を消したメッセージが新たに投稿され、
                そのメッセージが自動的にピン留めされる。
        """
        await ctx.send(template)

def setup(bot):
    bot.add_cog(MinecraftCog(bot))