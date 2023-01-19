import discord
import time
import os

bot = discord.Bot() # Create a bot object

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.defer() # Defer the interaction
        print("sleeping...")
        time.sleep(20) # Sleep for 20 seconds
        print("done sleeping")
        embed = discord.Embed(title="Button clicked!", description="You clicked the button!") # Create an embed
        await interaction.followup.send(embed=embed) # Send an embed as a followup message

@bot.slash_command(debug_guilds = [1008274700494979072]) # Create a slash command
async def button(ctx):
    await ctx.respond("This is a button!", view=MyView()) # Send a message with our View class that contains the button

bot.run() # Run the bot