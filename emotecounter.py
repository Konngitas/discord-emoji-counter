import sys
import re
import discord
from discord import Forbidden

bot_token = sys.argv[1]

try:
    guild_id = int(sys.argv[2])
except ValueError:
    print("The guild ID must be a decimal integer")
    exit()

try:
    message_limit = int(sys.argv[3])
except ValueError:
    print("The message limit must be a decimal integer")
    exit()
except IndexError:
    message_limit = None

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    guild = client.get_guild(guild_id)
    if(guild is not None):
        print('Fetching non-animated emojis')
        emojis = [emoji for emoji in guild.emojis if emoji.animated==False]
        emoji_count = {}
        for emoji in emojis:
            emoji_count[str(emoji)]=0

        print("Fetching emoji counts")

        for channel in guild.text_channels:
            print(f"Fetching emoji counts for channel {channel.name}")
            try:
                async for message in channel.history(limit=message_limit):
                    for reaction in message.reactions:
                        if reaction.emoji in emojis:
                            emoji = str(reaction.emoji)
                            emoji_count[emoji] = emoji_count[emoji] + reaction.count

                    message_emojis = re.findall("<:\w+:\d+>", message.content)
                    for emoji in message_emojis:
                        if emoji in emoji_count:
                            emoji_count[emoji] = emoji_count[emoji] + 1
            except Forbidden:
                print(f"Bot does not have access to fetch message history for channel {channel.name}. Skipping.") 
                
        print("Counts:")
        for emoji, count in sorted(emoji_count.items(), key=lambda item: item[1], reverse=True):
            print(f"{emoji} : {count}")

    else:
        print("Failed to get guild")

    await client.close()


client.run(bot_token)