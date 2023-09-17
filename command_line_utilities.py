# command line utilities are programs that can be run from the terminal or command line interface, and they are an essential part of many development workflows. In python, you can create your own command line utilities using the built_in argparse module.
import argparse

import requests

def DownloadFile(url,local_filename):
    if local_filename is None:
     local_filename = url.split('/')[-1]
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return 
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help= "Url of the file to download")
# parser.add_argument("output", help= "by which name do you want to save your file")
parser.add_argument("-o", "--output", help= " name of the file", default= None)


# parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.url)
print(args.output)
DownloadFile(args.url,args.output)
