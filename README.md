# discord-emoji-counter
This python script will tally the usage of a guild's custom emoji within that guild using discord.py

## Requirements
- Python 3.7+
- [discord.py](https://discordpy.readthedocs.io/en/stable/)

## Usage
This script takes 3 whitespace-separated arguments, in this order. 
1. **Bot Token**: A discord bot token
2. **Guild ID**: The ID of the Discord Guild you wish to tally the emoji usage for
3. *Message fetch limit*: A limit for how many messages to fetch per channel. This argument is **optional**. If not provided, the script will fetch **ALL** messages in a channel,
which may take an incredibly long time.

### Example
`python3 emotecounter.py Totally.Real.Bot.Token 123123123123 5000`

### Output
The script will print a list of server emotes and how many times they have been used(including reactions), like so:
```
<:emoji1:123123123123> : 352
<:emoji2:234234234234> : 40
<:emoji3:345345345345> : 5
<:emojinooneuses:456456456456> : 0
```
