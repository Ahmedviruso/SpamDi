# SpamD Library v0.1 By AhmedViruso

import random,string,random,time,os,sys

Lib = ("")

try:
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
except:
    Lib = ("False")

if (Lib == "False"):
    print("Trying to install requests library.")
    Response = os.system('{} -m pip install -U '.format(sys.executable) + "requests" + " -q")

    if (Response != 0):
        sys.exit("Couldn't Install The Library.")
    else:
        print("Done.")
        import requests
        from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

Domain = ("https://discordapp.com")

def Headers(Pr):
    return {'Authorization':Pr,'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36'}

def Join(Invite,Token):
    try:
        R = requests.post("https://discordapp.com/api/v6/invites/{}".format(Invite),headers=Headers(Token) ,verify=False)
        if(R.status_code == 200):
            print("Ok ({})".format(R.status_code))
        else:
            print("Not Ok [Server Response {}]".format(R.status_code) )
            time.sleep(3)
    except:
        print("An error occurred during function execution")
        exit()

def Spam_M(Channel,Token):
    try:
        Random = random.randint(10, 80)
        
        Chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        Chars = ''.join( random.sample(Chars*Random, Random) )

        R = requests.post(Domain + "/api/v6/channels/{}/messages".format(Channel), headers=Headers(Token) ,json={'content':Chars} ,verify=False)
        Rs = R.status_code

        if(Rs == 200):
            print("Ok ({})".format(Rs))
        elif(Rs == 429):
            print("{} Too Many Requests , Sleep(3)".format(Rs) )
            time.sleep(3)
        else:
            print("Not Ok [Server Response {}]".format(Rs) )
            time.sleep(3)
    except:
        print("An error occurred during function execution")
        exit()

def Spam_E(Channel,Message,Token):
    try:
        ListEmojis = ["%F0%9F%98%A2","%F0%9F%98%81","%F0%9F%A4%A4","%F0%9F%98%AC","%F0%9F%91%A8%E2%80%8D%F0%9F%A6%AF","%F0%9F%A4%AA","%F0%9F%98%98","%F0%9F%90%B9","%F0%9F%91%A8%E2%80%8D%F0%9F%94%A7","%F0%9F%A6%B7","%F0%9F%A7%99%E2%80%8D%E2%99%80%EF%B8%8F","%F0%9F%91%A8%E2%80%8D%F0%9F%8F%AB","%F0%9F%A4%A7","%F0%9F%A4%9B","%F0%9F%A7%A0","%F0%9F%98%B6","%F0%9F%92%87%E2%80%8D%E2%99%80%EF%B8%8F","%F0%9F%95%B5%EF%B8%8F%E2%80%8D%E2%99%82%EF%B8%8F","%F0%9F%90%AC"]
        Random = random.randint(0, 18)

        R = requests.put(Domain + "/api/v6/channels/{}/messages/{}/reactions/{}/@me".format(Channel,Message,ListEmojis[Random]), headers=Headers(Token) ,verify=False)
        R1 = requests.delete(Domain + "/api/v6/channels/{}/messages/{}/reactions/{}/@me".format(Channel,Message,ListEmojis[Random]), headers=Headers(Token) ,verify=False)
        
        Frist = R.status_code
        Second = R1.status_code
        
        if(Frist + Second == 408):
            print("Ok")
        else:
            print("Not Ok , Sleep(3) [Put Emoji Response ({})] [Delete Emoji Response ({})]".format(Frist,Second) )
            time.sleep(3)
    except:
        print("An error occurred during function execution")
        exit()
