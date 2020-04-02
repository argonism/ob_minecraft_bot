from discord.ext import commands
# import discord
import os
import traceback
import re
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん:cat:')

@bot.command()
async def search(ctx, arg): 
    for msg in await ctx.pins():
        if re.search(arg, msg.content):
            await channel.send(msg.content)

@bot.command()
async def help(ctx):
    template = """
    おいらはマイクラで便利に使えそうなボットだぜ
    追加して欲しい機能とかあったら言ってくれれば気分で追加するだぜ

    :::: 命令一覧 ::::
    /neko
            にゃーん

    /search (検索文字列)
            例: /search ネザー 
                    ピン留めされたメッセージの中から、
                    検索文字列を含むメッセージを表示する。
                    :warning:   /search   と   (検索文字列)   との間の半角空白に注意
    
    /pin
            これをメッセージのどこかにつけてメッセージを送ると、
            自動的にピン留めされる。
    """
    await ctx.send(template)

bot.run(token)
