# Python Operating System Library
import os

# Application Config File
import config

# Discord Bot Library
import discord

# Python Import Library
import importlib

# Datetime library for timestamp
from datetime import datetime

# Discord Bot Client Class
class Client(discord.client):

  # Initialiser Function
  def __init__(self):
    
    pass

  # Client connected to Discord, log event
  async def on_connect(self): self.log("Connected to Discord!")

  # Client disconnected from Discord, log event
  async def on_disconnect(self): self.log("Disconnected from Discord.")

  # Client done preparing data, log event
  async def on_ready(self): self.log("Bot client is ready")

  # Client session has been resumed, log event
  async def on_resumed(self): self.log("Bot session has resumed.")

  # Bot error has occured, log error to terminal
  async def on_error(self, event, *args, **kwargs): self.log("Bot Error: " + event)

  # Message is sent to a channel, detect event
  async def on_message(self, message):

    # If the first character of the message is in
    # the list of accepted command prefixes
    if message[0] in config.COMMAND_PREFIX:

      pass

  # Logging Function
  def log(self, message):

    # Log line which will be sent
    line = '[' + str(datetime.now()) + ']: ' + message

    # If a log file is provided
    if config.LOG_FILE:

      try:
        # Attempt to open the log file
        with open(config.LOG_FILE,"a+") as file:

          # Write the line to the file
          file.write(line + "\n")

        # Successfully wrote to file
        # Exit before logging to terminal
        return

      except Exception as e:
        print("Failed to write to '" + config.LOG_FILE + "'! Reason: " + e)

    # Print the given message with a timestamp
    print(line)

# Deref. Discord API Token
TOKEN = config.DISCORD_TOKEN

# Create a discord client connection
client = discord.Client()

# Run the discord bot
Client.run(TOKEN)