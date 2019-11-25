import discord
import aiohttp
import time
import sqlite3
import re, os
from discord.ext import commands

TOKEN = ''
userid = ''
version = 'v1.1'
client = discord.Client()
ts = time.gmtime()

if os.path.isfile('subwaybot.db'):
    db_exists = True
    conn = sqlite3.connect('subwaybot.db')
    c = conn.cursor()
else:
    conn = sqlite3.connect('subwaybot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE subwaybot
             (timesordered text)''')
    c.execute("INSERT INTO subwaybot VALUES ('0')")
conn.commit()
c.execute('SELECT * FROM subwaybot')
data = c.fetchall()
data = str(data)
timesordered = int(re.search(r'\d+', data).group())
conn.commit()

@client.event
async def on_message(message):
    global timesordered
    # We don't want the bot to reply to itself
    if message.author == client.user:
        return
    #or other bots
    if message.author.bot:
        return
    #Message Settings
    if message.content.startswith('!getsub italianbmt'):
        base_title = ("**Order #",timesordered,"**")
        base_desc = ("Order made by",message.author)
        timesordered += 1
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x7a19fd))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.1")
        embed.add_field(name="Heres your sub, {0.author.mention}", value="", inline=False)
        embed.set_image(url="https://www.subway.com/ns/images/menu/PAK/ENG/menu-category-sandwich-italianBMT_B.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author," got a Italian BMT sub.")

    if message.content.startswith('!getsub bfh'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3002.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a Black Forest Ham sub.")
        
    if message.content.startswith('!getsub c&b'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3004.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a chicken and bacon ranch melt.")

    if message.content.startswith('!getsub coldcutcombo'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3005.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a coldcut combo.")

    if message.content.startswith('!getsub meatball'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3007.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a meatball sub.")
    
    if message.content.startswith('!getsub orchicken'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3008.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a orchicken sub.")

    if message.content.startswith('!getsub roastbeef'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3009.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a roast beef sub.")

    if message.content.startswith('!getsub rschicken'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3143.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a rschicken sub.")
    
    if message.content.startswith('!getsub spicyitalian'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3010.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a spicy italian sub.")

    if message.content.startswith('!getsub steak&cheese'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3011.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]{0.author.mention} got a steak and cheese sub.")
    
    if message.content.startswith('!getsub subwayclub'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3012.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a subway club.")

    if message.content.startswith('!getsub scot'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3015.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a scot sub.")
    
    if message.content.startswith('!getsub tuna'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3017.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a tuna sub.(ew lol)")

    if message.content.startswith('!getsub turkey'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3018.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a turkey breast sub.")

    if message.content.startswith('!getsub veggie'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3020.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a veggie delight.")

    if message.content.startswith('!getsub chipotle_cs'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/10003.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a chipotle cheesesteak.")

    if message.content.startswith('!getsub pizzasub'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3082.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a pizza sub.")
    
    if message.content.startswith('!getsub ccmelt'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3181.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a chicken caesar melt.")
    
    if message.content.startswith('!getsub italian_t'):
        msg = 'Heres your sub, {0.author.mention}. [https://order.subway.com/Images/Subway/en-us/ProductClassLink/3092.png] '.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone got a italiano turkey melt.")

    if message.content == '!getsub':
        msg = 'Usage: `!getsub <sub name>`. To see a list of subs, try `!sublist`.'
        await message.channel.send(msg)

    if message.content.startswith('!getinvite'):
        msg = '{0.author.mention}, the invite code is https://discord.gg/WQJ7hRF'.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone used !getinvite.")

    if message.content.startswith('!sublist'):
        embed = discord.Embed(title="**List of subs**", description="List of sandwiches to use for !getsub.", colour=discord.Colour(0x7a19fd))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v0.6")
        embed.add_field(name="Italian BMT", value="Usage: `italianbmt`", inline=False)
        embed.add_field(name="Black Forest Ham", value="Usage: `bfh`", inline=False)
        embed.add_field(name="Chicken and Bacon Ranch Melt", value="Usage: `c&b`", inline=False)
        embed.add_field(name="Meatball Marinara", value="Usage: `meatball`", inline=False)
        embed.add_field(name="Oven Roasted Chicken", value="Usage: `orchicken`", inline=False)
        embed.add_field(name="Roast Beef", value="Usage: `roastbeef`", inline=False)
        embed.add_field(name="Rotisserie Style Chicken", value="Usage: `rschicken`", inline=False)
        embed.add_field(name="Spicy Italian", value="Usage: `spicyitalian`", inline=False)
        embed.add_field(name="Steak and Cheese", value="Usage: `s&c`", inline=False)
        embed.add_field(name="Subway Club", value="Usage: `subwayclub`", inline=False)
        embed.add_field(name="Sweet Onion Chicken Teriyaki", value="Usage: `scot`", inline=False)
        embed.add_field(name="Tuna", value="Usage: `tuna`", inline=False)
        embed.add_field(name="Turkey Breast", value="Usage: `turkey`", inline=False)
        embed.add_field(name="Veggie Delite", value="Usage: `veggie`", inline=False)
        embed.add_field(name="Turkey Italiano Melt", value="Usage: `italian_t`", inline=False)
        embed.add_field(name="Pizza Sub", value="Usage: `pizzasub`", inline=False)
        embed.add_field(name="Chipotle Cheesesteak", value="Usage: `chipotle_cs`", inline=False)
        embed.add_field(name="Chicken Caesar Melt", value="Usage: `ccmelt`", inline=False)

        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone used !sublist.")
    
    if message.content.startswith('!sbcmds'):
        embed = discord.Embed(title="**List of commands**", description="List of commands to use.", colour=discord.Colour(0x7a19fd))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v0.6")
        embed.add_field(name="!getsub <sub>", value="Get yourself an official Subway sandwich.", inline=False)
        embed.add_field(name="!sublist", value="View all possible subs to obtain.", inline=False)
        embed.add_field(name="!getinvite", value="Get an invite code to the offical SubwayBot server.", inline=False)
        embed.add_field(name="!sbcmds", value="View commands", inline=False)
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]Someone viewed the list of commands.")


#this thing
@client.event
async def on_ready():
    print('------------------------------------------------')
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------------------------------------------------')
    print("SubwayBot", version,"is connected and running!")
    print('------------------------------------------------')
client.run(TOKEN)
