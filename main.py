import os
from keep_alive import keep_alive
import leet_rank_calculator

client = leet_rank_calculator.get_discord_client()
keep_alive()
leetcode = os.environ['TOKEN']
client.run(leetcode)