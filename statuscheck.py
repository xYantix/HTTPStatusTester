import os
import requests
import argparse
import future


parser = argparse.ArgumentParser()
parser.add_argument('-list', '-l', required=True, help='Enter path for domain/subdomain list')
#Can add additional args later - custom headers

args = parser.parse_args()


urllist = args.list
urls = open(urllist, 'r')

def statuscheck(url):
    try:
        response = requests.get(url.strip(), timeout=1)
        status = response.status_code
        print ("Testing: " + url.strip())
        outfile = open(f"{status}.txt","a")
        outfile.write(url)
    except Exception:
        pass


with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    checks = {executor.submit(statuscheck, url): for url in urls}
    for future in concurrent.futures.as_completed(checks):
        url = checks[future]
        try:
            data = future.result()
        except Exception as exc:
            pass


