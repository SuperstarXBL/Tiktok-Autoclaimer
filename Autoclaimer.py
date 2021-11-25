import os, random, threading, requests, ctypes, colorama

from colorama import init
from threading import Thread
from discord_webhook import DiscordEmbed, DiscordWebhook
from requests import get, post, session

colorama.init(autoreset=True)
init()

ERROR = "[\x1b[31m-\x1b[39m]"
WHITE = "\033[1;37;40m"
BLUE = "\033[1;36;40m"
SUCCESS = "[\x1b[32m+\x1b[39m]"
INFO = "[\x1b[33m?\x1b[39m]"
INPUT = "[\x1b[35m*\x1b[39m]"

spinners = ["/", "-", "\\", "|"]

S = session()
Sessions = []
Proxies = []
List = []
WebhookUrl = 'PUT WEBHOOK URL HERE'

Headers = {
	"Host":"www.tiktok.com",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
	"Accept-Language":"ar",
	"Connection":"keep-alive"
}

with open(os.getcwd() + '/Sessions.txt', 'r', encoding='latin1') as fd:
    sessionpool = fd.read().splitlines()

for i in open('Proxies.txt', 'r').read().splitlines():
	Proxies.append(i)
with open(os.getcwd() + '/Proxies.txt', 'r', encoding='latin1') as fd:
    proxypool = fd.read().splitlines()

for i in open('Targets.txt', 'r').read().splitlines():
	List.append(i)
with open(os.getcwd() + '/Targets.txt', 'r', encoding='latin1') as fd:
    targetpool = fd.read().splitlines()

print("{}{} Tiktok Autoclaimer | Developed by Superstar#1282\n".format(WHITE, SUCCESS))
print("{} Sessions loaded: {}{}{}".format(SUCCESS, BLUE, len(sessionpool), WHITE))
print("{} Target's loaded: {}{}{}".format(SUCCESS, BLUE, len(targetpool), WHITE))
print("{} Proxies loaded: {}{}{}\n".format(SUCCESS, BLUE, len(proxypool), WHITE))
print('{}'.format(INPUT), end='');thread_count = int(input(' Thread\'s: '))
print("\n{} All threads successfully initialized".format(SUCCESS))

Tiktok_Headers = {
	"Host":"api16-normal-c-alisg.tiktokv.com",
	"Connection":"close",
	"Content-Type":"application/x-www-form-urlencoded",
	"sdk-version":"2",
	"passport-sdk-version":"5.12.1"
}

Token = post("https://www.tiktok.com").cookies["tt_csrf_token"]

Attempts = 0
RL = 0
SB = 0
Session = 0

def Claimer():
	global Attempts, RL, SB
	while True:
		for Session in Sessions:
			for User in List:
				try:
					Proxy = random.choice()
					Proxy.strip()
					NewProxies = {
						'http': f'http://{Proxy}',
						'https': f'http://{Proxy}'
					}
					S.proxies = NewProxies
					Cookies = {
						"tt_csrf_token":Token,
						"sessionid":Session
					}
					Check = S.get("https://www.tiktok.com/@" + User + "?lang=ar", headers=Tiktok_Headers, cookies=Cookies, timeout=3).status_code
					if Check == 200:
						Attempts += 1
					elif Check == 400:
						RL += 1
					elif Check == 404:
						Claimed = post("https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly", data={"login_name":User}, headers=Tiktok_Headers, cookies=Cookies).text
						if "success" in Claimed:
							if SB == 0:
								SB == 1
								with open(f"@{User} info.txt", "a") as x:
									x.write(f"User : {User}\nSessionid : {Session}\n")
								webhook = DiscordWebhook(url=WebhookUrl)
								embed = DiscordEmbed(title='Tiktok Autoclaimer', description=f'Claimed {User} Successfully!', color='03b2f8')
								webhook.add_embed(embed)
								response = webhook.execute()
								List.remove(User)
								Sessions.remove(Session)
								print("\r{} Claimed username \x1b[32m@{}\x1b[37m after \x1b[32m{:,}\x1b[37m attempts".format(SUCCESS, User, Attempts + 1))
						elif "This username is taken, but you can try a different one" in Claimed:
							Attempts += 1
						else:
							RL += 1
					for spinner in spinners:
						print("[\x1b[33m{}\x1b[37m] {:,} attempts | RL: {:,} | R/s: {:,}{}".format(spinner, Attempts, RL, " " * 10), end="\r", flush=True)
				except Exception as e:
					SB = 0

for Session in open("Sessions.txt", "r").read().splitlines():
	Cookies = {
		"tt_csrf_token":Token,
		"sessionid":Session
	}

	Claimed = post("https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly", data={"login_name":"sahe"}, headers=Tiktok_Headers, cookies=Cookies).text
	if "This username is taken, but you can try a different one" in Claimed:
		Session += 1
		Sessions.append(Session)

if not Sessions == []:
	ThreadsLst = []
	for i in range(Threads):
		t = Thread(target=Claimer).start()
		ThreadsLst.append(t)
		print("\n{} All threads successfully initialized".format(SUCCESS))
		
else:
	print('\n{} Sessions are invalid'.format(ERROR))
	print('{}'.format(INPUT), end='');exit = (input(' Press enter to exit turbo...'))