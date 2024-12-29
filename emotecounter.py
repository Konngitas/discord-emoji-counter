import sys
import re
from typing import Union
import discord
from discord import Forbidden, Intents, TextChannel, Thread

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

intents = Intents(messages=True, guilds=True, guild_reactions=True, message_content=True, emojis_and_stickers=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    emoji_count = {}
    sticker_count = {}
    
    print(f'We have logged in as {client.user}')

    guild = client.get_guild(guild_id)
    if (guild is not None):
        print('Fetching emojis')
        emojis = dict((str(emoji), emoji) for emoji in guild.emojis)

        for emoji in emojis:
            emoji_count[emoji] = 0
            
        print(f"Loaded emojis: {','.join(emoji_count)}")

        print("Fetching stickers")
        stickers = dict((sticker.id, sticker) for sticker in guild.stickers)

        for sticker_id in stickers:
            sticker_count[sticker_id] = 0
            
        print(f"Loaded stickers: {','.join(str(s) for s in sticker_count)}")

        print("Fetching counts")
        print(f"Message limit: {message_limit}")

        for channel in guild.text_channels:
            print(
                f"Fetching emoji and sticker counts for channel {channel.name}")
            await fetch_messages(channel, emoji_count, sticker_count)
            
            for thread in channel.threads:
                print(
                    f"Fetching emoji and sticker counts for thread {thread.name} in channel {channel.name}")
                await fetch_messages(thread, emoji_count, sticker_count)

        print("========= EMOJI COUNTS =========")
        for emoji, count in sorted(emoji_count.items(), key=lambda item: item[1], reverse=True):
            print(f"{emojis[emoji].name}: {count}")

        print("========= STICKER COUNTS =========")
        for sticker_id, count in sorted(sticker_count.items(), key=lambda item: item[1], reverse=True):
            print(f"{stickers[sticker_id].name}: {count}")
        print

    else:
        print("Failed to get guild")

    await client.close()


async def fetch_messages(channel_or_thread: Union[TextChannel, Thread], emoji_count, sticker_count):
    try:
        async for message in channel_or_thread.history(limit=message_limit):
            for reaction in message.reactions:
                emoji_str = str(reaction.emoji)
                if emoji_str in emoji_count:
                    #print(f"DEBUG: Reaction found: {emoji_str}")
                    emoji_count[emoji_str] += reaction.count

            message_emojis = re.findall("<:\w+:\d+>", message.content)
            for emoji in message_emojis:
                if emoji in emoji_count:
                    #print(f"DEBUG: Emoji found {emoji}")
                    emoji_count[emoji] += 1

            for sticker in message.stickers:
                if sticker.id in sticker_count:
                    #print(f"DEBUG: Sticker found: {sticker}")
                    sticker_count[sticker.id] += 1
    except Forbidden:
        print(f"Bot does not have access to fetch message history for channel {channel_or_thread.name}. Skipping.") 


client.run(bot_token)