import discord
import aiohttp
import asyncio
import time
import threading
from flask import Flask
from discord.ext import commands
from discord.ui import View, Button, button as ui_button
from discord import ButtonStyle

# -------------------- KEEP ALIVE SERVER --------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_keep_alive():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run_keep_alive)
    t.start()

# -------------------- CONFIG --------------------
url = "https://vivify.lol"
BAD_WORDS = [
    "Dualhook", "Dualhooked", "Dualhooking", "Dualhooker",
    "Dualhookers", "Dualhooks", "Triplehook", "Triplehooked",
    "Triplehooking", "Triplehooks", "Quadruplehook", "hooked", "dual", "hook", "Hooking"
]

GUILD_ID = 1516657846685667358
SUPPORT_CHANNEL_ID = 1517408522852241498
WELCOME_CHANNEL_ID = 1517387358259904633

VIDEO_URLS = [
    "https://cdn.discordapp.com/attachments/1363585727979589823/1381334942885347398/op_asf_edited_replay_1.mp4",
    "https://streamable.com/godall",
    "https://cdn.discordapp.com/attachments/1329804728061661196/1334028231644286987/preppyxhanna_preppyxhannas_is_LIVE_-_TikTok_LIVE_2024-10-06_20-42-48.mp4",
    "https://cdn.discordapp.com/attachments/1329804728061661196/1334028238200111145/Rich_Livvy_sunnyy_adoptme_is_LIVE_-_TikTok_LIVE_2024-10-20_00-21-39.mp4",
]

GIF_URL = "https://www.image2url.com/r2/default/gifs/1782151271452-17df7077-1c93-4b7b-b73c-f25728eceea4.gif"
BUTTON_EMOJI = discord.PartialEmoji.from_str("<a:Red_Crown2:1519133446079905844>")

LONG_DESC = """<a:black_star:1518724987266007131>**Tiktok-Live**

<a:Deja_Red_Fire:1518723451404288160> it works:

<a:Deja_Red_Fire:1518723451404288160> go live on tiktok using a fake roblox giveaway loop video, and try to get as many viewers as possible. and you will have fake link in your tiktok bio then you make them join you in your bio

<a:Deja_Red_Fire:1518723451404288160>

<a:Deja_Red_Fire:1518723451404288160> pc live you need TikTok account with live studio access
<a:Deja_Red_Fire:1518723451404288160> mobile live you need TikTok account with mobile gaming live access
<a:Deja_Red_Fire:1518723451404288160> this methods needs some brain, cant be a retard.

<a:Deja_Red_Fire:1518723451404288160> to get tiktok live account:

<a:black_star:1518724987266007131> to roblox trading servers or any account trading servers and trade for one

<a:black_star:1518724987266007131> can find other people who have live access in my server and yall can split hits, how it works is basically 1st guy will do the live 2nd guy will provide the tiktok

<a:Deja_Red_Fire:1518723451404288160> a link to put in bio

<a:Deja_Red_Fire:1518723451404288160> to Insanity's site and then pick one of the tiktok domain links and choose the one you will loop on your live

<a:Deja_Red_Fire:1518723451404288160> this as a link hider for tiktok https://beacons.ai/ (optional)

<a:Deja_Red_Fire:1518723451404288160> you can't add a link to your tiktok bio then make your tiktok account into business account in settings by clicking switch to business account, then click edit profile and click links and click add websites and paste it there

<a:Deja_Red_Fire:1518723451404288160> to go live and loop vids:

<a:Deja_Red_Fire:1518723451404288160> pc you have to download live studio and then set it up then just pick a good loop video you want and go live
<a:Deja_Red_Fire:1518723451404288160> mobile you have to loop the video from gallery settings atleast on android

<a:Deja_Red_Fire:1518723451404288160> remember these:

<a:Deja_Red_Fire:1518723451404288160> you go live always remember to mute your mic
<a:Deja_Red_Fire:1518723451404288160> notifications off
<a:Deja_Red_Fire:1518723451404288160> to blacklist bad words

<a:Deja_Red_Fire:1518723451404288160> live:

<a:Deja_Red_Fire:1518723451404288160> you're on mobile then your live game category should be subway surfers or clash royale.
<a:Deja_Red_Fire:1518723451404288160> Pc it can be Roblox
<a:Deja_Red_Fire:1518723451404288160> can be probably anything but be careful with words like Free and Giveaway since TikTok doesn't always like them

<a:Deja_Red_Fire:1518723451404288160> long to be live for:

<a:Deja_Red_Fire:1518723451404288160> live for hours or anything because it's normal for you to get low viewers if it's your first time living
<a:Deja_Red_Fire:1518723451404288160> you're not from usa or philippines, make sure you choose and use a vpn in those countries

<a:Deja_Red_Fire:1518723451404288160> your live:

<a:Deja_Red_Fire:1518723451404288160> is a method to TikTok Live grow viewers.
<a:Deja_Red_Fire:1518723451404288160>  just go live until viewers grow and when they drop by a bit just end the live immediately, then start a new live again and repeat this until you have stable hundreds of viewers
:black_star: videos about the game you're living in tiktok using https://snaptik.kim/ and post them make sure to add tags #roblox #fyp

<a:Deja_Red_Fire:1518723451404288160> NOTE:

<a:Deja_Red_Fire:1518723451404288160> don't have to hide your tiktok fake link and use it raw paste it raw, you can also use beacons.ai for your link!

<a:Deja_Red_Fire:1518723451404288160> quality for better views + so your tiktok account wouldn't get live suspended, also use an vpn depending on the timezone where people are awake only for philippines / usa

<a:Deja_Red_Fire:1518723451404288160> to make your own replays to get more beams!
"""

# Staff roles that can close tickets and use commands inside tickets
STAFF_ROLES = ["@ᴀᴅᴍɪɴs", "@ʜᴇᴀᴅ ᴀᴅᴍɪɴ", "@ʟᴇᴀᴅ ᴀᴅᴍɪɴ", "@sᴜᴘᴘᴏʀᴛ", "@ғᴏᴜɴᴅᴇʀs"]

def is_staff(member: discord.Member):
    """Return True if the member has any of the staff roles."""
    return any(role.name in STAFF_ROLES for role in member.roles)

# -------------------- INTENTS & BOT --------------------
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=['!', '+'], intents=intents)

# -------------------- VIEWS --------------------
class CloseView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Close", style=ButtonStyle.grey, custom_id="close_ticket")
    async def close_ticket(self, button: discord.ui.Button, interaction: discord.Interaction):
        # Only staff can close the ticket
        if not is_staff(interaction.user):
            await interaction.response.send_message("You don't have permission to close this ticket.", ephemeral=True)
            return
        await interaction.channel.delete(reason="Ticket Closed")


class SupportView(View):
    def __init__(self):
        super().__init__(timeout=None)

    async def create_ticket_channel(self, interaction, ticket_type):
        guild = interaction.guild
        channel_name = f"{ticket_type}-{interaction.user.name}"

        # Permissions: ticket creator can read, send, embed links, attach files,
        # and read message history; other users cannot see the channel.
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(
                read_messages=True,
                send_messages=True,
                read_message_history=True,
                embed_links=True,
                attach_files=True
            ),
        }

        for role_name in STAFF_ROLES:
            role = discord.utils.get(guild.roles, name=role_name)
            if role:
                overwrites[role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)

        for member in guild.members:
            if member.bot:
                overwrites[member] = discord.PermissionOverwrite(read_messages=True, send_messages=True)

        new_channel = await guild.create_text_channel(channel_name, overwrites=overwrites)

        # All embeds now use black colour
        if ticket_type == "method":
            embed = discord.Embed(
                title="<a:blood_red_diamond:1519036724058132620> Method Support Created <a:blood_red_diamond:1519036724058132620>",
                description="A staff member will assist you with your method query.",
                color=discord.Color.black()
            )
            embed.set_image(url="https://s4.ezgif.com/tmp/ezgif-45f72efbd3341135.gif")
        elif ticket_type == "tutorial":
            embed = discord.Embed(
                title="<a:coroa_red:1519037492211355919> Tutorial Support Created <a:coroa_red:1519037492211355919>",
                description="A staff member will assist you shortly.",
                color=discord.Color.black()
            )
            embed.set_image(url="https://i.pinimg.com/originals/67/b1/ef/67b1ef05eb08b416b90323b73e6cf1c5.gif")
        else:  # general support / website / other
            embed = discord.Embed(
                title="<a:Deja_Red_Fire:1518723451404288160> General Support Created <a:red_vamp_boost:1518723451404288160>",
                description="A staff member will assist you shortly.",
                color=discord.Color.black()
            )
            embed.set_image(url="https://images.steamusercontent.com/ugc/862852104096246182/2B4A61D3D0F000CE92383607F77BA37EFA719237/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false")

        embed.set_footer(text="Made By Vivify")
        await new_channel.send(embed=embed, view=CloseView())
        return channel_name

    @ui_button(style=ButtonStyle.gray, label="Method", custom_id="method_button")
    async def method_button(self, button, interaction):
        channel_name = await self.create_ticket_channel(interaction, "method")
        await interaction.response.send_message(f"Created support channel: **{channel_name}**", ephemeral=True)

    @ui_button(style=ButtonStyle.gray, label="Website", custom_id="website_button")
    async def website_button(self, button, interaction):
        channel_name = await self.create_ticket_channel(interaction, "website")
        await interaction.response.send_message(f"Created support channel: **{channel_name}**", ephemeral=True)

    @ui_button(style=ButtonStyle.gray, label="Tutorial", custom_id="tutorial_button")
    async def tutorial_button(self, button, interaction):
        channel_name = await self.create_ticket_channel(interaction, "tutorial")
        await interaction.response.send_message(f"Created support channel: **{channel_name}**", ephemeral=True)

    @ui_button(style=ButtonStyle.gray, label="Support", custom_id="support_button")
    async def support_button(self, button, interaction):
        channel_name = await self.create_ticket_channel(interaction, "support")
        await interaction.response.send_message(f"Created support channel: **{channel_name}**", ephemeral=True)


class VideosButton(View):
    def __init__(self):
        super().__init__()
        button = Button(
            style=discord.ButtonStyle.secondary,
            label="VIDEOS",
            emoji=BUTTON_EMOJI
        )
        button.callback = self.show_videos
        self.add_item(button)

    async def show_videos(self, interaction: discord.Interaction):
        video_list = "\n".join(VIDEO_URLS)
        await interaction.response.send_message(
            f"**Loop videos:**\n{video_list}",
            ephemeral=True
        )

# -------------------- EVENTS --------------------
@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        member_count = member.guild.member_count
        embed = discord.Embed(
            title="<a:Red_Gun:1519042663322751157> WELCOME TO **VIVIFY** <a:Deja_Red_Fire:1518723451404288160>",
            description=(
                f".\n\n\nᴡᴇʟᴄᴏᴍᴇ {member.mention}!\n\n\n"
                f"<a:5634_Butterfly_Red:1518723679737876490> Member Count: {member_count}\n\n"
                "<a:Red_Simbolo2CDL:1519043595410342099> Make sure to read the rules and verify!"
            ),
            color=0  # black
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else None)
        await channel.send(embed=embed)


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Ban for blacklisted words
    content = message.content
    for word in BAD_WORDS:
        if word.lower() in content.lower():
            try:
                await message.author.ban(reason="Used banned word")
            except discord.Forbidden:
                print("Unable to ban user")
            return

    # If the channel is a ticket channel, only staff may use commands
    if message.channel.name.startswith(("method-", "website-", "tutorial-", "support-")):
        if not is_staff(message.author):
            # Do not process commands for regular users in ticket channels
            return

    await bot.process_commands(message)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

    # Register persistent views
    bot.add_view(CloseView())
    bot.add_view(SupportView())

    guild = bot.get_guild(GUILD_ID)
    if guild:
        channel = guild.get_channel(SUPPORT_CHANNEL_ID)
        if channel:
            embed = discord.Embed(
                title="**SUPPORT TICKETS**",
                description=(
                    "<a:coroa_red:1519037492211355919> **ᴡʜᴀᴛ ᴛʏᴘᴇ ᴏꜰ ꜱᴜᴘᴘᴏʀᴛ ᴡᴏᴜʟᴅ ʏᴏᴜ ʟɪᴋᴇ?**\n"
                    "<a:Deja_Red_Fire:1518723451404288160> **ᴍᴇᴛʜᴏᴅ** ─ Questions about methods\n"
                    "<a:Red_Simbolo2CDL:1519043595410342099> **ᴡᴇʙꜱɪᴛᴇ** ─ Website issues\n"
                    "<a::red_wings:1518725302325350471> **ᴛᴜᴛᴏʀɪᴀʟ** ─ Help with tutorials\n"
                    "<a:red_gun2:1519131136494669885> **ꜱᴜᴘᴘᴏʀᴛ** ─ General support\n\n"
                    "<a:red_jordan_fdl:1519135480937975829> **ᴄʟɪᴄᴋ ᴀ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ᴛɪᴄᴋᴇᴛ**"
                ),
                color=0,  # black
            )
            embed.set_image(url="https://i.pinimg.com/originals/67/b1/ef/67b1ef05eb08b416b90323b73e6cf1c5.gif")
            embed.set_thumbnail(url="https://i.pinimg.com/originals/67/b1/ef/67b1ef05eb08b416b90323b73e6cf1c5.gif")
            view = SupportView()
            await channel.send(embed=embed, view=view)

# -------------------- COMMANDS --------------------
@bot.command()
async def support(ctx):
    embed = discord.Embed(
        title="<a:22123rocket:1517595399404257441> SUPPORT TICKETS <a:22123rocket:1517595399404257441>",
        description=(
            "<a:16414redstars:1517594808296673391>** ᴡʜᴀᴛ ᴛʏᴘᴇ ᴏꜰ ꜱᴜᴘᴘᴏʀᴛ ᴡᴏᴜʟᴅ ʏᴏᴜ ʟɪᴋᴇ?**\n\n"
            "<a:16414redstars:1517594808296673391> **ᴡᴇʙꜱɪᴛᴇ ─ Website issues**\n"
            "<a:16414redstars:1517594808296673391> **ᴍᴇᴛʜᴏᴅ ─ Questions about methods**\n"
            "<a:16414redstars:1517594808296673391> **ᴛᴜᴛᴏʀɪᴀʟꜱ ─ Help with tutorials**\n"
            "<a:purpleribbon:1518724686664695908> **ꜱᴜᴘᴘᴏʀᴛ** ─ General support\n\n"
        ),
        color=0  # black
    )
    embed.set_image(url="https://i.pinimg.com/originals/67/b1/ef/67b1ef05eb08b416b90323b73e6cf1c5.gif")
    view = SupportView()
    await ctx.send(embed=embed, view=view)


@bot.command()
async def check(ctx):
    start_time = time.time()
    status = "offline"
    ms = None
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as resp:
                if resp.status == 200:
                    status = "online"
                else:
                    status = "offline"
                ms = round((time.time() - start_time) * 1000)
    except Exception:
        status = "offline"
        ms = None

    embed = discord.Embed(
        title="<a:red_sharingan:1519038066126360767> Domain Checker <a:red_sharingan:1519038066126360767>",
        color=0  # black
    )
    embed.set_image(url="https://media.tenor.com/iVg3IjAwsDoAAAAd/red-eyes-anime.gif")

    response_time = ms if ms is not None else "N/A"
    if status == "online":
        embed.add_field(
            name="",
            value=(
                "<a:X_No_X_NC:1519028197650468996>\n"
                "```\n"
                f"\"response\":\"{response_time}ms\"\n"
                "\"status\":\"online\"\n"
                "\"domain\":\"vivify.lol\"\n"
                "```  <a:X_No_X_NC:1519028197650468996>"
            ),
            inline=False
        )
    else:
        embed.add_field(
            name="",
            value=(
                "<a:752793check:1518702673342369802>\n"
                "```\n"
                f"\"response\":\"{response_time}ms\"\n"
                "\"status\":\"offline\"\n"
                "\"domain\":\"vivify.lol\"\n"
                "```\n"
            ),
            inline=False
        )
    embed.set_footer(text="Status: ONLINE" if status == "online" else "Status: OFFLINE")
    await ctx.send(embed=embed)


@bot.group(name="tiktok")
async def tiktok_group(ctx):
    if ctx.invoked_subcommand is None:
        pass

@tiktok_group.command(name="live")
async def tiktok_live(ctx):
    embed1 = discord.Embed(color=0)  # black
    embed1.set_image(url=GIF_URL)

    embed2 = discord.Embed(description=LONG_DESC, color=0)  # black
    embed2.set_thumbnail(url=GIF_URL)

    view = VideosButton()
    await ctx.send(embeds=[embed1, embed2], view=view)

# -------------------- START THE BOT --------------------
keep_alive()  # starts the web server in a separate thread
bot.run('MTUxODY5Nzc5MTYxNzExMDE2Nw.GvWDYF.xq80VkSFrq-go5APYsxavAC3aWL4iTFiB0EvyQ')
