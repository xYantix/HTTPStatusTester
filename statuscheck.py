import os
import requests
import argparse
import concurrent.futures


parser = argparse.ArgumentParser()
parser.add_argument('-list', '-l', required=True, help='Enter path for domain/subdomain list')
parser.add_argument('-threads', '-t', required=False, default=10, help='Enter threads - Default is 10')
#Can add additional args later - custom headers

args = parser.parse_args()


urllist = args.list
threadcount = args.threads
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


with concurrent.futures.ThreadPoolExecutor(max_workers=int(threadcount)) as executor:
    checks = {executor.submit(statuscheck, url): url for url in urls}
    for future in concurrent.futures.as_completed(checks):
        url = checks[future]
        try:
            data = future.result()
        except Exception as exc:
            pass
