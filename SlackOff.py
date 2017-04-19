import os
import time
from slackclient import SlackClient

# import imgur_setup

# starterbot's ID as an environment variable
BOT_ID = 'U44A6ND6Y'  # os.environ.get("BOT_ID")
# constants
# Commands are what the slack bot reads in when you @ it
AT_BOT = "<@" + str(BOT_ID) + ">"
EXAMPLE_COMMAND = "do"
COMMAND_1 = "channel name"
COMMAND_2 = "channel users"

# instantiate Slack & Twilio clients
slack_client = SlackClient('xoxb-140346761236-M4ZyKkmcZbM6OdRhMZxlu3gj')


def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    # response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
    #          "* command with numbers, delimited by spaces."
    var = slack_client.api_call("channels.info", channel=channel)
    response = " "
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
    elif command.startswith(COMMAND_1):
        response = "We are currently in : \"" + var["channel"]["name"] + "\""
    else:
        response = "I'm sorry, I don't understand that command"
        # elif command.startswith(COMMAND_2):
        # response = "There are: " + str(len(var["channel"]["members"])) + " in this channel. \n" \
        # "User Names:"
        # for i in range(len(var["channel"]["members"])):
        #   response += "\n"
        # userID = var["channel"]["members"][i]
        #  var3 = slack_client.api_call("users.list")
        # userID = var3["members"][0]["profile"]["first_name"]
        #   response += "" + str(userID)*/

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def handle_reaction(reaction):
    if reaction and len(reaction) > 0:
        for output in reaction:
            if 'reaction' in output:
                print("\n")
                print(reaction[0]['reaction'])
                print(reaction[0]['item']['type'])
                print('hello?')
                #temp = slack_client.api_call("file.info", timeout=5)
                #print(temp['file'])
    return None


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed

                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


def parse_reaction_output(slack_rtm_output):
    """
        if the reaction is correct return true and follow through with upload.
    :param slack_rtm_output:
    :return: None if no reaction, else if reaction is right True
    """
    output_list = slack_rtm_output
    print()
    return None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose
    print("hello???")
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        time.sleep(1)
        while True:
            print("beep")
            time.sleep(1)
            # reaction = parse_reaction_output(slack_client.rtm_read())
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            else:
                #print("boop")
                # handle_reaction(reaction)
                time.sleep(READ_WEBSOCKET_DELAY)
                handle_reaction(slack_client.rtm_read())
            #print(slack_client.rtm_read())


    else:
        print(BOT_ID)
        print(os.environ.get('SLACK_BOT_TOKEN'))
        print("Connection failed. Invalid Slack token or bot ID?")
