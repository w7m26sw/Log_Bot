import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json


#另外存取setting.json
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Eevent(Cog_Extension):
    #成員加入公會
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f'{member} join!')

    #成員離開公會
    @commands.Cog.listener() 
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(f'{member} leave!')

    #回應文字
    @commands.Cog.listener() 
    async def on_message(self, msg):
        #如果是機器人自己發出的訊息跳開
        if msg.author == self.bot.user
            return

        if msg.content == '花花'
            await msg.channel.send('豬耳朵')
        if msg.content == '徐啟榮'
            await msg.channel.send('甘蔗')

def setup(bot):
    bot.add_cog(Eevent(bot))