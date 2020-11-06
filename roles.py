import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

Clientdiscord = discord.Client()

@client.event
async def on_ready():
	print('Bot is  online Now!!!')
	
@client.command()

@commands.has_permissions(mute_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
	await member.mute(reason=reason)
	await ctx.send('User '+member+' has been kicked for no reason')

client.run('NzYxOTUwNzkxMDQwMTA2NTc2.X3iD-A.Yj1BGdwL7mfGuXLQfp9rNg9vS9s')