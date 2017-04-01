# SlackOFF
Slack bot and server that upload images to Imgur 


Despite the fact the tutorial I followed goes over this in it, this is the simple way to set up the bot you want using slackOFF.
You can also use this as a way of setting up your own version of a similar bot.


1) Go to this page https://api.slack.com/bot-users

2) It tells you all about bots, and then you need to go down to the Custom Bots and click the 'creating a new bot user' link
  -Make sure you're in the right slack channel when doing this, some channels require you have permission to create bots. 
  
3) Get your api key! Don't tell or show other's it as it can create security vulrabilities if others have it.

4) Now that you have your key you need to set it up as an enviomental variable, this means that your computer stores it and allows it to be more secure and private. How you store it depends on how you want to run the program:

  From a Bash Shell:
   $export SLACK_BOT_TOKEN='api key goes here'
    
  For script in Rasbian (check out launcher.sh for the rest):
    SLACK_BOT_TOKEN='api key goes here'
    sudo -E python Name_of_program.py 
 
 5) Next you should run the print_bot_id.py program and get the value returned. This is your bot's ID, and this is how your program knows that it's the one being called when you @ it. Follow the same set up at 4) only this time the enviomental variable is BOT_ID. You also only need the sudo once if you're doing the script version.
 
6) Alright, time to run! You should only need to run the launcher script, or if you're manually starting it from a bash shell type: 
python name_of_program.py and you're done! Your bot should be running in your slack channel, and be ready to answer all the burning questions you might have such as 'What channel is this?'
