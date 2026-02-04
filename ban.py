import discord

LOG_CHANNEL_ID = "Channel Id / Id do canal"


class BanReasonModal(discord.ui.Modal, title="🚫 Motivo do Ban"):
    motivo = discord.ui.TextInput(
        label="Qual o motivo do ban?",
        style=discord.TextStyle.paragraph,
        required=True,
        max_length=500
    )

    def __init__(self, target: discord.Member):
        super().__init__()
        self.target = target

    async def on_submit(self, interaction: discord.Interaction):
        log_channel = interaction.guild.get_channel(LOG_CHANNEL_ID)

        await self.target.ban(
            reason=f"{self.motivo.value} | Banido por {interaction.user}"
        )

        embed = discord.Embed(
            title="🚫 Usuário Banido",
            color=discord.Color.dark_red()
        )

        embed.set_thumbnail(url=self.target.display_avatar.url)
        embed.set_footer(
            text=f"Banido por {interaction.user}",
            icon_url=interaction.user.display_avatar.url
        )

        embed.add_field(name="👤 Usuário", value=self.target.mention, inline=False)
        embed.add_field(name="🆔 ID", value=self.target.id, inline=False)
        embed.add_field(name="📝 Motivo", value=self.motivo.value, inline=False)

        if log_channel:
            await log_channel.send(embed=embed)

        await interaction.response.send_message(
            "✅ Usuário banido com sucesso.",
            ephemeral=True
        )


class BanButton(discord.ui.View):
    def __init__(self, target: discord.Member):
        super().__init__(timeout=None)
        self.target = target

    @discord.ui.button(label="🚫 Banir", style=discord.ButtonStyle.danger)
    async def ban_button(self, interaction: discord.Interaction, _):
        if not interaction.user.guild_permissions.ban_members:
            return await interaction.response.send_message(
                "❌ Você não tem permissão.",
                ephemeral=True
            )

        await interaction.response.send_modal(
            BanReasonModal(self.target)
        )
