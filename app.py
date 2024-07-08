import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound, CommandOnCooldown, MissingRequiredArgument, CheckFailure

# Define the bot and intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
intents.members = True  # Enable member intents for member management commands

# Create a bot instance with the necessary intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Command to mute all users in the current voice channel
@bot.command()
@commands.has_permissions(administrator=True)  # Requires administrator permissions
async def muteall(ctx):
    """Mutes all users in the voice channel."""
    if ctx.author.voice and ctx.author.voice.channel:
        for member in ctx.author.voice.channel.members:
            await member.edit(mute=True)
        await ctx.send("All users have been muted.")
    else:
        await ctx.send("You are not in a voice channel.")

# Command to unmute all users in the current voice channel
@bot.command()
@commands.has_permissions(administrator=True)  # Requires administrator permissions
async def unmuteall(ctx):
    """Unmutes all users in the voice channel."""
    if ctx.author.voice and ctx.author.voice.channel:
        for member in ctx.author.voice.channel.members:
            await member.edit(mute=False)
        await ctx.send("All users have been unmuted.")
    else:
        await ctx.send("You are not in a voice channel.")

# Command to list all available commands
@bot.command(name="commands", help="Lists all available commands.")
async def list_commands(ctx):
    """Lists all available commands."""
    commands_list = "**Available Commands:**\n"
    for command in bot.commands:
        commands_list += f"`!{command.name}`: {command.help}\n"
    await ctx.send(commands_list)

# Command to show developer information
@bot.command()
async def info(ctx):
    """Shows developer information."""
    info_message = """
    [ + ] Developer Name : Md. Shishir Ahmed
    [ + ] Website : https://www.shishir1337.com
    """
    await ctx.send(info_message)

# Enhanced error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Command not found. Please check the command and try again.")
    elif isinstance(error, CommandOnCooldown):
        await ctx.send(f'This command is on cooldown. Try again in {error.retry_after:.2f} seconds.')
    elif isinstance(error, MissingRequiredArgument):
        await ctx.send("Missing arguments for the command. Please provide the necessary arguments.")
    elif isinstance(error, CheckFailure):
        await ctx.send("You do not have permission to use this command.")
    else:
        await ctx.send(f"An error occurred: {error}")

# Run the bot
bot.run('bot_token')
