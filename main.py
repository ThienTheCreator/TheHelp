import os
import hikari 
import lightbulb
from goatgpt.goatgpt import plugin


from dotenv import load_dotenv
load_dotenv()

bot = lightbulb.BotApp(token=os.getenv("DISCORD_TOKEN"), default_enabled_guilds=(811140759356964865))

@bot.listen(hikari.StartedEvent)
async def on_started(event):    
    print("Bot is ready!")

bot.add_plugin(plugin)

bot.run()