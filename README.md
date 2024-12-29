# discord-emoji-counter
This python script will tally the usage of a guild's custom emoji within that guild using discord.py.
It goes through all channels and threads it has access to and counts how many times each of the guild's emojis and stickers were used.

## Requirements
- Python 3.7+
- [discord.py](https://discordpy.readthedocs.io/en/stable/)

## Usage
This script takes 3 whitespace-separated arguments, in this order. 
1. **Bot Token**: A discord bot token. The bot user must be added to the discord guild you wish to tally the emoji for
2. **Guild ID**: The ID of the Discord Guild you wish to tally the emoji usage for
3. *Message fetch limit*: A limit for how many messages to fetch per channel. This argument is **optional**. If not provided, the script will fetch **ALL** messages in a channel,
which may take an incredibly long time.

### Example
`python3 emotecounter.py Totally.Real.Bot.Token 123123123123 5000`

### Output
The script will print a list of server emoji and stickers, as well ashow many times they have been used(including reactions), in descending order of usage count like so:
```
========= EMOJI COUNTS =========
Emoji Name 1: 63
Emoji Name 2: 23
Emoji Name 3: 5
Emoji Name 4: 0
========= STICKER COUNTS =========
Sticker Name 1: 10
Sticker Name 2: 4
Sticker Name 3: 2
Sticker Name 4: 0
```
