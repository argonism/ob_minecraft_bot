from discord.ext import commands
import traceback

token = os.environ['DISCORD_BOT_TOKEN']

# 読み込むコグの名前を格納しておく。
INITIAL_EXTENSIONS = [
    'cogs.minecraft_cog'
]

# クラスの定義。ClientのサブクラスであるBotクラスを継承。
class MinecraftBot(commands.Bot):

    # MyBotのコンストラクタ。
    def __init__(self, command_prefix):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(command_prefix)

        # INITIAL_COGSに格納されている名前から、コグを読み込む。
        # エラーが発生した場合は、エラー内容を表示。
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    async def on_command_error(self, ctx, error):
        orig_error = getattr(error, "original", error)
        error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
        await ctx.send(error_msg)

    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print([user.name for user in self.users])
        print('-----')

if __name__ == '__main__':
    bot = MinecraftBot(command_prefix='/')
    bot.run(token)