import discord
from discord import app_commands


def setup_amistoso(client):

    @client.tree.command(
        name="amistoso",
        description="Enviar informações do amistoso"
    )
    @app_commands.describe(
        libero="Libero",
        setter="Setter",
        oposto="Oposto",
        ponteiro="Ponteiro",
        central="Central",
        link="Link do amistoso",
        imagem="Imagem do amistoso"
    )
    async def amistoso(
        interaction: discord.Interaction,
        libero: discord.Member,
        setter: discord.Member,
        oposto: discord.Member,
        ponteiro: discord.Member,
        central: discord.Member,
        link: str,
        imagem: discord.Attachment
    ):

        embed = discord.Embed(
            title="🏐 Amistoso",
            color=discord.Color.blue()
        )

        embed.add_field(name="LIBERO", value=libero.mention, inline=False)
        embed.add_field(name="SETTER", value=setter.mention, inline=False)
        embed.add_field(name="OPOSTO", value=oposto.mention, inline=False)
        embed.add_field(name="PONTEIRO", value=ponteiro.mention, inline=False)
        embed.add_field(name="CENTRAL", value=central.mention, inline=False)

        embed.add_field(
            name="LINK AMISTOSO",
            value=link,
            inline=False
        )

        await interaction.response.send_message(embed=embed)
