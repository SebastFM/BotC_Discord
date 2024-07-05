import random

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)



emodji = ["^^", "0_o", ":)", "¯\\_(ツ)_/¯", "(￢_￢)"]


@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')



@client.event
async def on_message(message):
    emodji = ["^^", "0_o", ":)", "¯\\_(ツ)_/¯", "(￢_￢)"]
    monde = ["Cara","Cruz"]
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$emoji'):
        await message.channel.send(random.choice(emodji))
    elif message.content.startswith('$moneda'):
        await message.channel.send(random.choice(monde))
