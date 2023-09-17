# Multiprocessing is a python module that provides a simple way to run multiple processes in parallel. It allows you to take advantage of multiple cores or processors on your system and can give significantly improve the performance of your code.

#import multiprocessing
import concurrent.futures
import requests

def downloadFile(url,name):
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading{name}")
# ye sb ko aik sth start kr day ga
    
if __name__ == "__Multi_Processing__":
    url = "https://www.pexels.com/photo/a-person-on-a-bicycle-at-ark-of-bukhara-17593738/"
# pros = []
# for i in range(5):
#      #downloadFile(url,i)
#      p = multiprocessing.Process(target=downloadFile, args=[url,i])
     
#      p.start()
#      pros.append(p)

# for p in pros:
#     p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(60)]
    l2 = [i for i in range(60)]
    results = executor.map(downloadFile, url, l1, l2)
    for r in results:
        print(r)

