import asyncio
import os
# import sys
from datetime import date

# import discord
from discord.ext import tasks, commands

# from functions import embed
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
  from index import Friday as Bot


original_image = "assets\\friday-logo.png"


class DatedEvents(commands.Cog):
  def __init__(self, bot: "Bot"):
    self.bot = bot
    self.dated_events.start()
    # self.events = bot.loop.create_task(self.dated_events(),name="Dated events")

  @tasks.loop(hours=1.0)
  async def dated_events(self):
    if not self.bot.prod:
      return
    today = date.today()
    month = today.strftime("%m")
    day = today.strftime("%d")
    guild = self.bot.get_guild(707441352367013899)
    user = self.bot.user
    thispath = os.getcwd()
    if "\\" in thispath:
      seperator = "\\\\"
    else:
      seperator = "/"
    if int(month) == 4 and int(day) == 1:
      print("april fools")
      self.bot.logger.info("april fools")
      with open(f"{thispath}{seperator}assets{seperator}friday_april_fools.png", "rb") as image:
        f = image.read()
        await user.edit(avatar=f)
        await guild.edit(icon=f, reason="April Fools")
        image.close()
      await asyncio.sleep(43200.0)
    elif int(month) == 4 and int(day) == 2:
      print("post-april fools")
      self.bot.logger.info("post-april fools")
      with open(f"{thispath}{seperator}assets{seperator}friday-logo.png", "rb") as image:
        f = image.read()
        await guild.edit(icon=f, reason="Post-april fools")
        await user.edit(avatar=f)
        image.close()
      await asyncio.sleep(43200.0)

  @dated_events.before_loop
  async def before_dated_events(self):
    await self.bot.wait_until_ready()

  def cog_unload(self):
    self.dated_events.cancel()


def setup(bot):
  bot.add_cog(DatedEvents(bot))
