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
            members = Member.objects()
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
            members = Member.objects(gear_score__gte = num)
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
            members = Member.objects(gear_score__lte = num)
            rows = get_row(members, False)
            data = tabulate(rows,
                            headers,
                           'simple',)

            for page in paginate(data):
                await self.bot.say(page)
        except:
            await self.bot.say("Something went horribly wrong")

    @commands.group(pass_context=True)
    async def sort_by(self, ctx):
        """Group of sorting commands"""

        # Checks if no sub-commands are invoked
        if ctx.invoked_subcommand is None:
            await self.bot.say(codify("Sort by any category available(lvl, ap, dp, gs). Try gsbot help sort_by"))

    @sort_by.command()
    async def lvl(self, num=100):
        """ - Sorts list by level and progress with optional limiter"""
        try:
            members = Member.objects().order_by('-level', '-progress')
            rows = get_row(members, True, num)

            data = tabulate(rows,
                            headers,
                            'simple',)

            for page in paginate(data):
                await self.bot.say(page)
        except Exception as e:
            await self.bot.say("Could not retrieve list")
            print(e)

    @sort_by.command()
    async def ap(self, num=100):
        """ - Sorts list by AP with optional limit"""
        try:
            members = Member.objects().order_by('-ap')
            rows = get_row(members, True, num)

            data = tabulate(rows,
                            headers,
                            'simple',)

            for page in paginate(data):
                await self.bot.say(page)
        except Exception as e:
            await self.bot.say("Could not retrieve list")
            print(e)

    @sort_by.command()
    async def dp(self, num=100):
        """ - Sorts list by DP with optional limit"""
        try:
            members = Member.objects().order_by('-dp')
            rows = get_row(members, True, num)

            data = tabulate(rows,
                            headers,
                            'simple',)

            for page in paginate(data):
                await self.bot.say(page)
        except Exception as e:
            await self.bot.say("Could not retrieve list")
            print(e)


def setup(bot):
    bot.add_cog(Listing(bot))
