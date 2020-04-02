from discord.ext import commands
# import discord
import os
import traceback
import re
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
bot.remove_command('help')

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
            await ctx.send(msg.content)

@bot.command()
async def pin(ctx):
    new_text = ctx.message.content.replace("/pin ", "")
    new_msg = await ctx.send(new_text)
    await new_msg.pin()

@bot.command()
async def help(ctx):
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

# @client.event
# async def on_message(message):

bot.run(token)
