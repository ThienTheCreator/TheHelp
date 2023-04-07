import hikari
import lightbulb
from .goat import Goat

plugin = lightbulb.Plugin("goatgpt")
goat: Goat = Goat()

def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)

# -- COMMANDS -- 

# ASK GOATGPT
@plugin.command
@lightbulb.option("prompt", "prompt goatgpt", type=str)
@lightbulb.command("ask", "Ask GoatGPT anything!")
@lightbulb.implements(lightbulb.SlashCommand)
async def goatgpt_ask(ctx: lightbulb.Context) -> None:
    prompt = ctx.options.prompt
    result = goat.ask(prompt)
    embed = hikari.Embed(
        title="Question",
        description=prompt,
        color=hikari.Color.from_rgb(255, 165, 0)
    )
    embed.add_field(name="Answer", value=result)
    
    await ctx.respond(embed=embed)
    # await ctx.respond("Prompt: " + prompt + "\n" + result)
    
