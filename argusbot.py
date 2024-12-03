import os
import discord
from discord.ext import commands



# allows for intents
intents = discord.Intents.default()

# allows messages to be recognized and responded too
intents.messages = True # Required for processing message-based commands
intents.message_content = True   # Required for processing message-based commands

intents.members = True

client = commands.Bot(command_prefix='!argus ', intents=intents)





# starts the console strings so I can later modify this
@client.event
async def on_ready():
    print("Hello I am Argus-Bot")
    print("---------------------------------")



# looks for a command in this case hello
@client.command()
async def hello(ctx):
    #awaits comand to send a string
    await ctx.send("Hi") 
    
    

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Try again!")
    else:
        print(f"Error: {error}")
        

@client.command(pass_context = True)
async def join(ctx):
    #based on what the user is doing .author.
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        #awaits comand to send a string for not being in a channel
        await ctx.send("You need to be in a voice channel")
      
      
  
@client.command(pass_context = True)
async def leave(ctx):
    #based purley on the state of the bot
    #voice client is the voice the bot is in
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        #awaits comand to send a string
        await ctx.send("Away I go")
        
    else:
        await ctx.send("I am not in a voice channel")


@client.event
async def on_member_join(member):
    await member.send("Hello New User")
    print("hello")
    
    channel = client.get_channel(1313367872453742626)
    await channel.send("Check your dms")
    
    

    
    





client.run(BOTKEY)




