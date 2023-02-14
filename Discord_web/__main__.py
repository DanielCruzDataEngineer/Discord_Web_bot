import discord
from discord.ext import commands,tasks
from discord.ext.commands import Bot
import os
import pandas as pd
import time
import os
from dotenv import load_dotenv,find_dotenv
import openpyxl
load_dotenv(find_dotenv())

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# hostname = socket.gethostname()
# ip = socket.gethostbyname(hostname)

intents = discord.Intents().all()
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$run'):
        a = str(message.content).strip('$run')
        await message.channel.send("Contando....")

        i=0
        print(i)
# Carregue a planilha existente
        workbook = openpyxl.load_workbook('Baby_testes.xlsx')
        worksheet = workbook.active
        # Adicione alguns dados na planilha
        worksheet['A1'] = 'Quantidade de contrações'
        worksheet['A2'] = int(worksheet['A2'].value) + 1

        # Salve a planilha atualizada
        workbook.save('Baby_testes.xlsx')

if __name__ == "__main__" :
    client.run(DISCORD_TOKEN)

