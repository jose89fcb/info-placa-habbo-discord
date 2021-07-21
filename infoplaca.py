import requests, bs4
import re
import discord
from discord.ext import commands



bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 
 
@bot.command()
async def infoplaca(ctx, *, placa): #Comando a decir
    habbo = requests.get(f"https://www.habbo-happy.net/placas/info/{placa}")

    infoplaca = bs4.BeautifulSoup(habbo.content, "html.parser")

    NombrePlaca = infoplaca.find("div", class_="headline").text

    DescripcionPlaca = infoplaca.find("div", class_="subheadline").text

    embed = discord.Embed(title="", description="•Nombre🡺 " + f"{NombrePlaca}" + "\n•Descripcion🡺 " + f"{DescripcionPlaca}" + "\n•Código🡺 " f"{placa.upper()}")
    embed.set_thumbnail(url="https://images.habbo.com/c_images/album1584/" f"{placa.upper()}.png")
    embed.set_author(name="información placa", icon_url="https://i.imgur.com/grmS8RH.png")



    await ctx.send(embed=embed)
 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run('') #OBTEN UN TOKEN EN: https://discord.com/developers/applications
