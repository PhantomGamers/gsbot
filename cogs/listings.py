import discord
from discord.ext import commands
from tabulate import tabulate

from models import Member
from utils import *


class Listing:
    """All the listing commands."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def list(self,ctx,num=100):
        """List all the members and their gear score with optional limit. 
        Example. gsbot list returns first 100 by default  and gsbot list 5 first 5 sorted by
        gear score"""
        try:
            members = Member.objects(server=ctx.message.server.id)
            rows = get_row(members, True, num)

            data = tabulate(rows,
                            headers,
                           'simple',)
            
            for page in paginate(data):
                await self.bot.say(page)
        except Exception as e:
            await self.bot.say("Something went horribly wrong")
            print(e)

    @commands.command(pass_context=True)
    async def over(self, ctx, num=400):
        """List all the members over a certain gear score"""
        try:
            members = Member.objects(gear_score__gte = num)(server=ctx.message.server.id)
            rows = get_row(members,False)

            data = tabulate(rows,
                            headers,
                           'simple',)

            for page in paginate(data):
                await self.bot.say(page)

        except Exception as e:
            print(e)
            await self.bot.say("Something went horribly wrong")

    @commands.command(pass_context=True)
    async def under(self, ctx, num=400):
        """List all the members under a certain gear score"""
        try:
            members = Member.objects(gear_score__lte = num)(server=ctx.message.server.id)
            rows = get_row(members, False)
            data = tabulate(rows,
                            headers,
                           'simple',)

            for page in paginate(data):
                await self.bot.say(page)
        except:
            await self.bot.say("Something went horribly wrong")


def setup(bot):
    bot.add_cog(Listing(bot))