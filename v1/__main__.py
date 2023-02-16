"""Main module."""
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import os
import time
import os
from dotenv import load_dotenv, find_dotenv
import openpyxl
import threading
from pyairtable import Table

load_dotenv(find_dotenv())

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents().all()
client = discord.Client(intents=intents)


def run_client():
    client.run(DISCORD_TOKEN)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$run'):
        await message.channel.send("Contando....")
        table = Table(api_key="patBNbJ2WW5isGveG.4a51cb0ff4b878fba92ec086283bd1846e51552ee8de22404722d11b96b79071", base_id='appEPWrzVyjn6mrWl', table_name='Teste')
        records = table.all()
        print(records[0])
        a = records[0]['fields']['Testes']
        table.update('rec2SloJLOniuYR1c', {"Testes": f"{int(a)+int(1)}"})

    # listar registros
    # table.create({"Foo": f"{i+1}"})


if __name__ == "__main__":
    client.run(DISCORD_TOKEN)

    # aqui você pode executar outras tarefas enquanto o client.run() está em execução em segundo plano

    # para aguardar o término do thread do client.run(), você pode usar o método join()
