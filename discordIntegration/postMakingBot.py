import sqlite3
import disnake
from disnake.ext import commands
import asyncio

#-------------[DATABASE SETUP]------------
database = sqlite3.connect('posts.db')
database.execute('''CREATE TABLE IF NOT EXISTS POSTS
         (ID INTEGER PRIMARY KEY AUTOINCREMENT    NOT NULL,
         TITLE           TEXT    NOT NULL,
         BLURB           TEXT,
         BODY            TEXT    NOT NULL,
         IMAGE           TEXT);''')
database.close()
#------[COMMAND LINE ARGUMENT SETUP]------
import sys
import argparse
parser = argparse.ArgumentParser(description="A Discord Bot designed by Katte.")
parser.add_argument("--token", "-t", help="Supply a token for a bot account to connect under.", default="", type=str)
args = parser.parse_args()
token = args.token
if token == "": sys.exit("No Token, Cannot Connect")
#-----------------------------------------
client = commands.Bot(command_prefix="b|", test_guilds=[951923779859271711], intents=disnake.Intents.default())

@client.event
async def on_ready():
  print(f'Ready to help you make Posts.')

@client.slash_command(
    name='create-new-post',
    description='A Handy API interface for creating a new blog post on katte.ca'
)
async def create_post(ctx, title : str, body : str, blurb : str ="", image: str =""):
    global database
    await ctx.send(content='Initializing Post API...')
    message = await ctx.original_message()
    await asyncio.sleep(1)
    try:
        await message.edit(content='Connecting...')
        database = sqlite3.connect('posts.db')
        cursor = database.cursor()
        await message.edit(content='Connected to Database')
        blog_fields = """INSERT INTO POSTS
            (TITLE,BODY,BLURB,IMAGE)
            VALUES (?,?,?,?)"""
        blog_content = (title, body, blurb, image)
        cursor.execute(blog_fields, blog_content)
        database.commit()
        await message.edit(content='Data Inserted')
        cursor.close()
        await message.edit(content='Creating your Post...')
    except sqlite3.Error as error:
       await ctx.send(content='Failed to Create Post' + str(error))
    finally:
        if database:
            database.close()
            await message.edit(content='Post Complete!')

client.run(token)