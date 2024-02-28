from instabot import Bot
 
bot = Bot()
bot.login(username="", 
          password="")
 
# Count number of followers
followers = bot.get_user_followers("")
print("Total number of followers:")
print(len(followers))