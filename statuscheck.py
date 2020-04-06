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
    response = requests.get(url.strip(), timeout=300)
    if response.status_code == 200:
        print url + " = " + str(response.status_code)
        outfile = open("200.txt","a")
        outfile.write(url)

    elif response.status_code == 300:
        print url + " = " + str(response.status_code)
        outfile = open("300.txt","a")
        outfile.write(url)

    elif response.status_code == 301:
        print url + " = " + str(response.status_code)
        outfile = open("301.txt","a")
        outfile.write(url)

    elif response.status_code == 302:
        print url + " = " + str(response.status_code)
        outfile = open("301.txt","a")
        outfile.write(url)

    elif response.status_code == 304:
        print url + " = " + str(response.status_code)
        outfile = open("304.txt","a")
        outfile.write(url)

    elif response.status_code == 307:
        print url + " = " + str(response.status_code)
        outfile = open("307.txt","a")
        outfile.write(url)

    elif response.status_code == 400:
        print url + " = " + str(response.status_code)
        outfile = open("400.txt","a")
        outfile.write(url)

    elif response.status_code == 401:
        print url + " = " + str(response.status_code)
        outfile = open("401.txt","a")
        outfile.write(url)

    elif response.status_code == 404:
        print url + " = " + str(response.status_code)
        outfile = open("404.txt","a")
        outfile.write(url)

    elif response.status_code == 410:
        print url + " = " + str(response.status_code)
        outfile = open("410.txt","a")
        outfile.write(url)

    elif response.status_code == 429:
        print url + " = " + str(response.status_code)
        outfile = open("429.txt","a")
        outfile.write(url)

    elif response.status_code == 500:
        print url + " = " + str(response.status_code)
        outfile = open("500.txt","a")
        outfile.write(url)

    elif response.status_code == 501:
        print url + " = " + str(response.status_code)
        outfile = open("501.txt","a")
        outfile.write(url)

    elif response.status_code == 503:
        print url + " = " + str(response.status_code)
        outfile = open("503.txt","a")
        outfile.write(url)

    elif response.status_code == 550:
        print url + " = " + str(response.status_code)
        outfile = open("550.txt","a")
        outfile.write(url)
