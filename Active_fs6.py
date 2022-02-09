import requests, signal, socket
from discord_webhook import DiscordEmbed
from discord_webhook import DiscordWebhook
tell_tokin = ""
id_tell = ""
web_hook = ""
def Active_fs6():
    qq = requests.session()
    hostname = socket.gethostname()
    ip2 = (hostname)
    ip1 = requests.get('https://fs6.pw/ip/')
    ip = ip1.text
    print('ip address = ' + ip )
    g = requests.get('https://pastebin.com/raw/1gjbYkCp')
    if ip in g.text:
        FS6 = DiscordWebhook(url=web_hook)
        em = DiscordEmbed(title=f"new login successful at ip = {ip} hostname = {ip2} ", description=" This tool by @u929", color=3066993)
        em.set_thumbnail(url='https://imgur.com/m6lYzYC.gif')
        FS6.add_embed(em)
        FS6.execute()
        g = requests.get(f'https://api.telegram.org/bot{tell_tokin}/SendMessage?chat_id={id_tell}&text=new login successful at ip = {ip} hostname = {ip2} ' + '\n' + "This tool by @u929")
        print('Active')
    else:
        FS6 = DiscordWebhook(url=web_hook)
        em = DiscordEmbed(title=f"new login Fail at ip = {ip} hostname = {ip2} ", description=" This tool by @u929" , color=15548997)
        em.set_thumbnail(url='https://imgur.com/m6lYzYC.gif')
        FS6.add_embed(em)
        FS6.execute()
        g = requests.get(f'https://api.telegram.org/bot{tell_tokin}/SendMessage?chat_id={id_tell}&text=new login Fail at ip = {ip} hostname = {ip2} ' + '\n' + "This tool by @u929")
        print('unactive')
        exit()
Active_fs6()
