import discord
from discord.ext import commands
import datetime
import calendar
import asyncio

cli = commands.Bot(command_prefix='.')

@cli.event
async def on_ready():
    print('Online')

#time
@cli.command()
async def time(ctx):
    tt = datetime.datetime.now()
    await ctx.send(tt.strftime("%H:%M:%S"))

#date
@cli.command()
async def date(ctx):
    tt2 = datetime.datetime.now()
    await ctx.send(tt2.strftime("%d/%m/%Y"))

#day
@cli.command()
async def day(ctx):
    tt3 = datetime.date.today()
    await ctx.send(tt3.strftime('%A'))

#full calender
@cli.command()
async def calender(ctx, year: int, month: int):
    await ctx.send(f'```{calendar.month(year, month, w=3)}```')

#timer
@cli.command()
async def timer(ctx, seconds):
    try:
        secondint = int(seconds)
        if secondint > 900:
            await ctx.send("u cannot go above 900")
            raise BaseException
        if secondint < 0 or secondint == 0:
            await ctx.send("I do not do anything that is 0 or below 0")
            raise BaseException
        message = await ctx.send("Timer: " + seconds)
        while True:
            secondint = secondint - 1
            if secondint == 0:
                await message.edit(new_content=("Ended!"))
                break
            await message.edit(new_content=("Timer: {0}".format(secondint)))
            await asyncio.sleep(1)
        await ctx.send(ctx.message.author.mention + " time is up.")
    except ValueError:
        await ctx.send("Must be a number!")

cli.run('TOKEN')
