import os
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-list', '-l', required=True, help='Enter path for domain/subdomain list')
#Can add additional args later - custom headers

args = parser.parse_args()


urllist = args.list
urls = open(urllist, 'r')

for url in urls:
    try:
        response = requests.get(url.strip(), timeout=1)
        status = response.status_code
        print ("Testing: " + url.strip())
        outfile = open(f"{status}.txt","a")
        outfile.write(url)
    except Exception:
        pass
