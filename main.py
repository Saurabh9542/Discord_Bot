import discord
import os
from config import config
from openai import OpenAI

oi = OpenAI()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):

        if self.user != message.author:
            if self.user in message.mentions:
                response = oi.chat.completions.create(
                model="text-davinci-003",
                messages=[
                    {
                    "role": "user",
                    "content": message.content
                    }
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
        
                messageToSend = response.choices[0].text
                await message.channel.send(messageToSend)



intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(config['Token'])