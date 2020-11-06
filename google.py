i = input('Enter Query:\n')
i = i.replace(' ', '+')

url = 'https://www.google.com/search?sxsrf=ALeKk007UZzexzay2zIkZitBrM5EHYiYLw%3A1601904168587&source=hp&ei=KB57X4j2IcOQ4-EP3curuAo&q='+i+'&oq='+i+'&gs_lcp=ChFtb2JpbGUtZ3dzLXdpei1ocBADOgcIIxDqAhAnOgQIIxAnOgUIABCRAjoICAAQsQMQgwE6BQgAELEDOgQIABBDOgcIABAUEIcCOgIIADoECAAQClDhFli_NGDpNmgAcAB4AIAB3wGIAYQdkgEGMC4xNi40mAEAoAEBsAEP&sclient=mobile-gws-wiz-hp'

import requests
from bs4 import BeautifulSoup
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
r = requests.get(url,  headers=header)
soup = BeautifulSoup(r.text, 'html.parser')

for link in soup.find_all('li'):
	print(link.get('href'))
	print('\n')