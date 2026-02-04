import discord
from discord import app_commands
from moderation.ban import BanButton


def setup_userinfo(client):

    @client.tree.command(
        name="userinfo",
        description="Mostra informações do usuário"
    )
    @app_commands.describe(user="Usuário que você quer ver as informações")
    async def userinfo(interaction: discord.Interaction, user: discord.Member):

        nickname = user.nick or user.name
        cargos = [r.mention for r in user.roles if r.name != "@everyone"]
        cargos_texto = ", ".join(cargos) if cargos else "Nenhum cargo"

        embed = discord.Embed(
            title="📌 Informações do Usuário",
            color=discord.Color.red()
        )
        embed.add_field(name="👤 Nome / Apelido", value=nickname, inline=False)
        embed.add_field(name="🆔 ID", value=user.id, inline=False)
        embed.add_field(name="🎭 Cargos", value=cargos_texto, inline=False)
        embed.set_thumbnail(url=user.display_avatar.url)

        await interaction.response.send_message(
            embed=embed,
            view=BanButton(user)
        )
