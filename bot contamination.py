import discord
from discord.ext import commands, tasks
import random
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

mensajes = [
    "sabias que la contaminacion deja infertil 1 de cada 6 personas",
    "sabias que la contaminacion nos puede matar en el futuro por el aire contaminado",
    " casi 9 millones de personas anueles mueren por la contaminacion",
    "deberias extender la informacion de la contaminacion porque si no tu podrias morir muy prematuramente",
    "la energia limpia es algo muy interesante.sirve para que no se mueran los seres vivos por el calentamiento global",
    "sabias que una de las energias limpias mas veneficiosa es la energia solar",
    "como crees que tu puedas detener el calentamiento global"
]

ultimo_mensaje = time.time()

@bot.event
async def on_message(message):
    global ultimo_mensaje
    if not message.author.bot:
        ultimo_mensaje = time.time()
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print("Bot conectado")
    hablar.start()

@tasks.loop(minutes=1)
async def hablar():
    if time.time() - ultimo_mensaje < 600:
        for guild in bot.guilds:
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).send_messages:
                    await channel.send(random.choice(mensajes))
                    break
bot.run("toquen")
