import discord
import os 

command_prefix = '!'
client = discord.Client


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        
        if message.author.bot:
          return
      
        if message.author != message.author.bot:
          await message.channel.send("Hello From Bot")
          
        if message.content.startswith(command_prefix):
           await message.channel.send("Enter Command")
          
        if message.content == "ping":
            await message.channel.send("PONG!")
client = MyClient()
TOKEN = os.environ['TOKEN']
client.run(TOKEN)

### Episod 2  : https://www.youtube.com/watch?v=xxWo2GXS0AY&list=PLESMQx4LeD3NmTZ8D1qwQwwSp67kznl-K&index=4