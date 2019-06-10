import discord
from discord.ext import commands
import random
import json
import dice
import PERSONALTOKEN

bot = commands.Bot(command_prefix = '>')

#with open("english-words/words_dictionary.json") as JSON:
#	english = json.load(JSON)


#print(len(english))
#@bot.listen_message(message):

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def epic(ctx):
	await ctx.send("no its not")

@bot.command()
async def lol(ctx):
	await ctx.send("fuck")


@bot.command()
async def ding(ctx):
	await ctx.send("DONG")

@bot.command()
async def roll(ctx,arg):
	""" roll a random die a number of times
	probably could parse the args better tbh"""	
	number,die = arg.split("d")
	value = dice.multiRoll(int(number),int(die))
	total = 0
	for i in value:
		total+=i
	result = "total is: "+str(total) #+"\nindividual results "+ str(value)
	await ctx.send(result)


@bot.command()
async def request(ctx, * ,arg):
	""" function for requesting new features"""
	f = open("requests.txt","a+")
	f.write(arg+" "+str(ctx.author)+"\n")
	f.close()
	await ctx.send("will take your request into account")

@bot.command()
async def stats(ctx):
	stats={
	    "str":dice.multiRoll(4,6),
	    "dex":dice.multiRoll(4,6),
	    "con":dice.multiRoll(4,6),
	    "int":dice.multiRoll(4,6),
	    "wis":dice.multiRoll(4,6),
	    "cha":dice.multiRoll(4,6)
	}
		
	for x,y in stats.items():
		y = y.remove(min(y))
	result = """Strenth:{0}:{1} \nDexterity:{2}:{3} \nConstitution:{4}:{5} \nIntelligence: {6},{7} \nWisdom:{8}:{9} \nCharisma:{10}:{11}
        """.format(stats["str"],sum(stats["str"]),stats["dex"],sum(stats["dex"]),stats["con"],
                sum(stats["con"]),stats["int"],sum(stats["int"]),stats["wis"],sum(stats["wis"]),stats["cha"],sum(stats["cha"]))
	await ctx.send(result)

@bot.command()
async def palegius(ctx):
	story = open("palegius.txt","r")	
	value = story.read()
	story.close	
	await ctx.send(value) 


bot.run(PERSONALTOKEN.TOKEN)
