import requests, sys

res = requests.get('https://arxiv.org/pdf/1904.07428.pdf', verify = False)
# check for errors
try:
    res.raise_for_status()
except Exception as e:
    print(str(e))
    sys.exit()
with open(r'./fascinating_article.pdf', 'wb') as article:
    article.write(res.content)
