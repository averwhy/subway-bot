import discord
import aiohttp
import time
import sqlite3
import re, os, sys
from discord.ext import commands
print("discord.py, version",discord.__version__)
print(sys.version_info)

TOKEN = ''
userid = ''
version = 'v1.3'
client = discord.Client()

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
    ts = time.localtime()
    
    c.execute('SELECT * FROM subwaybot')
    data = c.fetchall()
    data = str(data)
    timesordered = int(re.search(r'\d+', data).group())
    conn.commit()

    # We don't want the bot to reply to itself
    if message.author == client.user:
        return
    #or other bots
    if message.author.bot:
        return
    #Message Settings
    if message.content.startswith('!getsub italianbmt'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://www.subway.com/ns/images/menu/PAK/ENG/menu-category-sandwich-italianBMT_B.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a Italian BMT sub.")

    if message.content.startswith('!getsub bfh'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://www.subway.com/ns/images/menu/USA/ENG/Category_767x767_BlackForestHam_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a Black Forest Ham sub.")
        
    if message.content.startswith('!getsub c&b'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_ChickenBaconRanchMelt_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a chicken and bacon ranch melt.")

    if message.content.startswith('!getsub coldcutcombo'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_ColdCutCombo_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a coldcut combo.")

    if message.content.startswith('!getsub meatball'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_MeatballMarinara_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a meatball sub.")
    
    if message.content.startswith('!getsub orchicken'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_OvenRoastedChicken_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a orchicken sub.")

    if message.content.startswith('!getsub roastbeef'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_RoastBeef_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a roast beef sub.")

    if message.content.startswith('!getsub rschicken'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_RotisserieChicken_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a rschicken sub.")
    
    if message.content.startswith('!getsub spicyitalian'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_SpicyItalian_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a spicy italian sub.")

    if message.content.startswith('!getsub steak&cheese'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_SteakCheese_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]{0.author.mention} got a steak and cheese sub.")
    
    if message.content.startswith('!getsub subwayclub'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_SubClub_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a subway club.")

    if message.content.startswith('!getsub scot'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_SweetOnionChickenTeriyaki_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a scot sub.")
    
    if message.content.startswith('!getsub tuna'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_Tuna_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a tuna sub.(ew lol)")

    if message.content.startswith('!getsub turkey'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_TurkeyBreast_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a turkey breast sub.")

    if message.content.startswith('!getsub veggie'):
        base_title = (f"Order #{timesordered}")
        base_desc = (f"Submitted by {message.author.mention}")
        sql_update_query = "Update subwaybot set timesordered = " + str(timesordered + 1) + " where timesordered = " + str(timesordered)
        c.execute(sql_update_query)
        timesordered += 1
        conn.commit() # Save changes
        
        embed = discord.Embed(title=base_title, description=base_desc, colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="Heres your sub!", value="\u200b", inline=False)
        embed.set_image(url="https://subway.com/ns/images/menu/USA/ENG/Category_767x767_VeggieDelite_Sandwiches_@1x.jpg")
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a veggie delight.")

    if message.content.startswith('!getsub chipotle_cs'):
        await message.channel.send("That sub is no longer avaliable, sorry.\nFor more subs, try `!sublist`")
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"tried to get a chipotle cheesesteak.")

    if message.content.startswith('!getsub pizzasub'):
        await message.channel.send("That sub is no longer avaliable, sorry.\nFor more subs, try `!sublist`")
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a pizza sub.")
    
    if message.content.startswith('!getsub ccmelt'):
        await message.channel.send("That sub is no longer avaliable, sorry.\nFor more subs, try `!sublist`")
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a chicken caesar melt.")
    
    if message.content.startswith('!getsub italian_t'):
        await message.channel.send("That sub is no longer avaliable, sorry.\nFor more subs, try `!sublist`")
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"got a italiano turkey melt.")

    if message.content == ('!getsub'):
        msg = 'Usage: `!getsub <sub name>`. To see a list of subs, try `!sublist`.'
        await message.channel.send(msg)

    if message.content.startswith('!getinvite'):
        msg = '{0.author.mention}, the invite is https://discordapp.com/api/oauth2/authorize?client_id=517421670726762520&permissions=51200&scope=bot'.format(message)
        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"used !getinvite.")

    if message.content.startswith('!sublist'):
        msg = """**List of subs avaliable, and their usage.**\n`Sub name : Sub usage`\n```md
1. Italian BMT : italianbmt
2. Black Forest Ham : bfh
3. Chicken and Bacon Ranch Melt : c&b
4. Meatball Marinara : meatball
5. Oven Roasted Chicken : orchicken
6. Roast Beef : roastbeef
7. Rotisserie Style Chicken : rschicken
8. Spicy Italian : spicyitalian
9. Steak and Cheese : s&c
10. Subway Club : subwayclub
11. Sweet Onion Chicken Teriyaki : scot
12. Tuna : tuna
13. Turkey Breast : turkey
14. Veggie Delite : veggie
```
**Deprecated subs: subs that are no longer on the menu.**```md
1. Turkey Italiano : italian_t
2. Pizza Sub : pizzasub
3. Chipotle Cheesesteak : chipotle_cs
4. Chicken Caesar Melt : ccmelt
```
"""

        await message.channel.send(msg)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"used !sublist.")
    
    if message.content.startswith('!sbcmds'):
        embed = discord.Embed(title="**List of commands**", description="List of commands to use.", colour=discord.Colour(0x00ff11))
        embed.set_author(name="SubwayBot")
        embed.set_footer(text="SubwayBot v1.3")
        embed.add_field(name="!getsub <sub>", value="Get yourself an somewhat-official Subway sandwich.", inline=False)
        embed.add_field(name="!sublist", value="View all possible subs to obtain.", inline=False)
        embed.add_field(name="!getinvite", value="Get an invite code to the offical SubwayBot server.", inline=False)
        embed.add_field(name="!sbcmds", value="View commands", inline=False)
        await message.channel.send(embed=embed)
        print("[",time.strftime("%Y-%m-%d %H:%M:%S",ts),"]",message.author,"viewed the list of commands.")


#this thing
@client.event
async def on_ready():
    print('------------------------------------------------')
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------------------------------------------------')
    print(f"SubwayBot", version,"is connected and running!")
    print('------------------------------------------------')
client.run(TOKEN)
