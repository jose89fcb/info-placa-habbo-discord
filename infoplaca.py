import requests, bs4
import re
import discord
from discord.ext import commands
import time
import asyncio



bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 


@bot.command()
async def infoplaca(ctx, *, placa):
    async with ctx.typing():
        await asyncio.sleep(3)
        habbo = requests.get(f"https://www.habbo-happy.net/placas/info/{placa}")
    
    
   
   

    infoplaca = bs4.BeautifulSoup(habbo.content, "html.parser")

    NombrePlaca = infoplaca.find("div", class_="headline").text

    DescripcionPlaca = infoplaca.find("div", class_="subheadline").text

    embed = discord.Embed(title="", description="•Nombre🡺 " + f"{NombrePlaca}" + "\n\n•Descripcion🡺 " + f"{DescripcionPlaca}" + "\n\n•Código🡺 " f"{placa.upper()}")
    embed.set_thumbnail(url="https://images.habbo.com/c_images/album1584/" f"{placa.upper()}.png")
    embed.set_author(name="información placa", icon_url="https://i.imgur.com/grmS8RH.png")
    
    await ctx.send("buscando...", delete_after=0)
    time.sleep(6)
    await ctx.message.delete()

    
   
    
    await ctx.send(embed=embed)

    
    
   
    
    
 
 
 
@bot.event
async def on_ready():
    activity = discord.Game(name="info placa", type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("BOT listo!")
    
 
    
bot.run('') #OBTEN UN TOKEN EN: https://discord.com/developers/applications
