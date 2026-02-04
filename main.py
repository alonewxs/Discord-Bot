import discord
from discord import app_commands

from moderation.ban import BanButton
from user_e_ban.userinfo import setup_userinfo
from amistoso.amistoso import setup_amistoso


GUILD_ID = "Guild Id / Id da Guilda"

intents = discord.Intents.default()
intents.members = True


class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        guild = discord.Object(id=GUILD_ID)

        setup_userinfo(self)
        setup_amistoso(self)

        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

        print("Slash commands sincronizados")


client = MyClient()
client.run("Your bot token / Token do bot")
