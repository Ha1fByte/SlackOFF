import os
import time
from slackclient import SlackClient
import webbrowser
import glob
from imgurpython import ImgurClient

client_id = 'YOURS GOES HERE'
client_secret = 'YOURS GOES HERE'

imgur_client = ImgurClient(client_id, client_secret)

BOT_ID = 'YOURS GOES HERE'  # os.environ.get("BOT_ID")

EXAMPLE_COMMAND = "do"
COMMAND_1 = "channel name"
COMMAND_2 = "channel users"

# instantiate Slack & Twilio clients
slack_client = SlackClient('YOURS GOES HERE')



def handle_reaction(reaction):
    if reaction and len(reaction) > 0:
        for output in reaction:
            if 'reaction' in output:
                #print("\n")
                print(reaction)
                var1 = reaction[0]['item']
                #print(var1['type'])
                #print("\n")
                if var1['type'] == 'file' and reaction[0]['reaction'] == 'white_check_mark':
                    #print(var1['file'])
                    #print('hello?')
                    temp = slack_client.api_call("files.info", timeout=5, file=var1['file'])
                    #print(temp)
                    if (temp['file']['pretty_type'] == 'JPEG' or temp['file']['pretty_type'] == 'PNG') and \
                            reaction[0]['user'] == temp['file']['user']:
                        var3 = temp['file']['url_private']
                        var2 = temp['file']['url_private_download']
                        webbrowser.open(var2)
                        time.sleep(2)
                        list_of_files = glob.glob('C:\\Users\\Natalie\\Downloads\\*.jpg')
                        list_of_files2 = glob.glob('C:\\Users\\Natalie\\Downloads\\*.png')# * means all if need specific format then *.csv
                        latest_file = max(list_of_files, key=os.path.getctime)
                        latest_file2 = max(list_of_files2, key=os.path.getctime)

                        file_list = [latest_file, latest_file2]
                        newest = max(file_list, key=os.path.getctime)
                        image = imgur_client.upload_from_path(newest, anon=False)
                        user_dm = slack_client.api_call('im.open', user=reaction[0]['user'])
                        #print(user_dm)
                        response = "You can find it here: {0}".format(image['link'])
                        slack_client.api_call("chat.postMessage", channel=user_dm['channel']['id'],text=response, as_user=True)

                        time.sleep(5)
                        os.remove(latest_file)

    return None



if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose
    print("hello???")
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        time.sleep(1)
        while True:
            time.sleep(1)
            handle_reaction(slack_client.rtm_read())
    else:
        print(BOT_ID)
        print(os.environ.get('SLACK_BOT_TOKEN'))
        print("Connection failed. Invalid Slack token or bot ID?")
