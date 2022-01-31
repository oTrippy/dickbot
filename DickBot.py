import discord
import random
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound

client = commands.Bot(command_prefix= '.')
token = 'ODkxNzYzNTY5NTU5OTk0NDI5.YVDFiw.trUCYf5Ax4vHPdX-EidfrwOgN0w'

@client.event
async def on_ready():
    print("Bot is prepared to bully.")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Please don't use uppercase letters")



@client.command()
async def dm(ctx):
    message = random.randint(1,14)
    if message == 1:
        dm = "Who the fuck you think you are talking to, you bilbo baggins lookin mother fucker."
    elif message == 2:
        dm = "You no life having, incest loving, dumb virgin."
    elif message == 3:
        dm = "You should touch grass before your mom leaves you."
    elif message == 4:
        dm = "Dumb dildo fucking, 47 chromosome having bitch."
    elif message == 5:
        dm = "Man's so far in the closet, his mailing address is Narnia."
    elif message == 6:
        dm = "I hope you stub your toe well walking around your house at 3am looking for a snack."
    elif message == 7:
        dm = "I hope when you turn on the shower the cold part doesn't stop comming."
    elif message == 8:
        dm = "I hope you step on lego."
    elif message == 9:
        dm = "I hope both sides of your pillow are warm."
    elif message == 10:
        dm = "Seriously? You were the sperm that won?"
    elif message == 11:
        dm = "Light travels faster than sound, which is why you seemed bright until you spoke."
    elif message == 12:
        dm = "Somewhere out there a tree is producing oxygen for you, go apologize"
    elif message == 13:
        dm = "If you are ever feeling down, remember out there is someone that probably masturbates to your image, and that's awesome, except for you you're ugly"
    await ctx.message.author.send(dm)

client.run(token)
