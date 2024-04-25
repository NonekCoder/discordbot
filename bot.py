from typing import Literal, Optional
import discord
from discord.ext.commands import Greedy, Context
from discord import app_commands
from discord.ext import commands
from genpass import *
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix = 'b?')
bot.remove_command('help')

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user}') #Bot Name
    print(bot.user.id) #Bot ID

#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
#    if message.content.startswith('$hello'):
#        await message.channel.send("Cześć!")
#    elif message.content.startswith('$bye'):
#        await message.channel.send("\\U0001f642")
#    else:
#        return

guild = discord.Object(id='1228380318273245184')

@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(
  ctx: Context, guilds: Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

@bot.tree.command(name="test",description="A test command cause yes")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello Cruel World!")

@bot.tree.command(name="say",description="Tell me what to type")
async def slash_command(interaction:discord.Interaction, message: str):
    await interaction.response.send_message(message)

@bot.command()
async def say(ctx, *, text=None):
    if text == None:
        await ctx.send('Please provide a message to send: b?say (message)')
    else:
        await ctx.send(text)

@bot.command()
async def genpass(ctx, lenght=None):
    if lenght== None:
        await ctx.send('Please provide the password lenght')
    else:
        try:
            passw = gen_pass(int(lenght))
            await ctx.send(f"Your password: {passw}")
        except:
            await ctx.send('Please use a number, not a letter')

@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title = f"{ctx.guild.name} Info", description = "Information of this Server", color = discord.Colour.blue())
    embed.add_field(name = '🆔Server ID', value = f"{ctx.guild.id}", inline = True)
    embed.add_field(name = '📆Created On', value = ctx.guild.created_at.strftime("%b %d %Y"), inline = True)
    embed.add_field(name = '👑Owner', value = f"{ctx.guild.owner}", inline = True)
    embed.add_field(name = '👥Members', value = f'{ctx.guild.member_count} Members', inline = True)
    
    # Calculate the number of text and voice channels
    text_channels = len([channel for channel in ctx.guild.channels if isinstance(channel, discord.TextChannel)])
    voice_channels = len([channel for channel in ctx.guild.channels if isinstance(channel, discord.VoiceChannel)])
    embed.add_field(name = '💬Channels', value = f'{text_channels} Text | {voice_channels} Voice', inline = True)
    
    # Use 'icon.url' attribute to get the guild's icon URL
    embed.set_thumbnail(url = str(ctx.guild.icon.url))
    embed.set_footer(text = "⭐ • Best bot ever cause nonek created")    
    # Removed the url parameter from set_author
    embed.set_author(name = f'{ctx.guild.name}', icon_url = str(ctx.guild.icon.url))
    await ctx.send(embed=embed)

@bot.command()
async def emoji(ctx):
    emoji = gen_emodji()
    await ctx.send(emoji)

@bot.command()
async def coin(ctx):
    coin = flip_coin()
    await ctx.send(coin)

@bot.command()
async def gif(ctx):
    chosen = gifsend()
    await ctx.send(chosen)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = f"{ctx.guild.name} bot commands", description = "All the commands of this bot", color = discord.Colour.blue())
    embed.add_field(name = 'b?help', value = "Displays the bot commands", inline = True)
    embed.add_field(name = 'b?serverinfo', value = "Displays the server info", inline = True)
    embed.add_field(name = 'b?say (message)', value = "Say a message as the bot", inline = True)
    embed.add_field(name = 'b?genpass (count)', value = "Generates a random password", inline = True)
    embed.add_field(name = 'b?emoji', value = "Generates a random emoji", inline = True)
    embed.add_field(name = 'b?coin', value = "Flips a coin", inline = True)
    embed.add_field(name = 'b?gif', value = "Sends a gif idk (random)", inline = True)
    
    # Use 'icon.url' attribute to get the guild's icon URL
    embed.set_thumbnail(url = str(ctx.guild.icon.url))
    embed.set_footer(text = "⭐ • Best bot ever cause nonek created")    
    # Removed the url parameter from set_author
    embed.set_author(name = f'{ctx.guild.name}', icon_url = str(ctx.guild.icon.url))
    await ctx.send(embed=embed)

bot.run(str(TOKEN))