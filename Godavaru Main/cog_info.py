import discord
from discord.ext import commands

class Info():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def about(self, ctx):
        server_count = 0
        for server in self.bot.servers:
            server_count += 1
        if ctx.message.content[8:] == "credits":
            embed = discord.Embed(title='Credits!', description='Here are some very honorable mentions for the creation, support, and overall community of the bot!',color=0x9B59B6).add_field(name='First Donator',value='MrLar#8117').add_field(name='Developers',value='Desiree#3658, Instance#2513, Yuvira#7842, and Jonas B.#9089').set_footer(text='Hope you enjoy the bot!').set_thumbnail(url='https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png')
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)
        else:
            embed = discord.Embed(title='About Godavaru!', description = "Hello! My name is Godavaru! I am Desiree#3658's very first bot, very much in production still. I hope you enjoy the bot so far!", color=0x9B59B6).add_field(name='Version Number', value='0.3.1', inline=False).add_field(name='Servers', value=str(server_count)+ '\n\n[Invite me](https://goo.gl/chLxM9)\n[Support guild](https://discord.gg/ewvvKHM)\n[Patreon page](https://www.patreon.com/godavaru)', inline=False).set_footer(text="Made with love <3 | Do --about credits for credits!").set_thumbnail(url="https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png")
            await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

    @commands.command(pass_context = True)
    async def invite(self, ctx):
        embed = discord.Embed(description='Here are some useful links for the Godavaru bot. If you have any questions at all, feel free to join the support guild and tag Desiree#3658 with your questions!\nBelow you can also find the links to the support guild itself and the Patreon URL. Thanks for using the bot!', color=0x9B59B6).set_author(name='Useful Links for Godavaru!', icon_url='https://cdn.discordapp.com/avatars/311810096336470017/fa4daf0662e13f25bdbd09fd18bdc36d.png').add_field(name='Invite URL', value='http://polr.me/godavaru').add_field(name='Support Guild', value='https://discord.gg/ewvvKHM').add_field(name="Patreon URL", value='https://patreon.com/godavaru')
        await self.bot.send_message(ctx.message.channel, content=None, embed=embed)

    @commands.command(pass_context = True)
    async def request(self, ctx):
        request_channel = discord.Object('316674935898636289')
        if ctx.message.content[13:] != "":
            await self.bot.send_message(request_channel, '**Request from ' + ctx.message.author.name + '#' + ctx.message.author.discriminator + ':** ' + ctx.message.content[10:])
            await self.bot.say ("Your request has been received! :slight_smile:")
        else:
            await self.bot.say ("Please specify something to request or make the request longer!")

def setup(bot):
    bot.add_cog(Info(bot))
