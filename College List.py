from lxml import html
import requests

pnum = int(input("Number of Pages:"))
with open("Colleges.txt",'w') as file:
	file.write('')
def scrape(pnum):
	if pnum > 1:
		page = requests.get('http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities?_page={}'.format(pnum), allow_redirects = 1)
	else:
		page = requests.get('http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities')
	tree = html.fromstring(page.content)
	rank = tree.xpath("//div[@class='block-normal']/div[@class='text-strong']/div/text()")
	college = tree.xpath("//h3[@class='heading-large block-tighter']/a/text()")
	for i in range(len(rank)):
		for x in [' ','#','inNationalUniversities','\n']:
			rank[i] = rank[i].replace(x,'')
	for i in rank:
		if i == '':
			rank.remove('')
	with open("Colleges.txt",'a') as file:
		for i in range(len(rank)):
			file.write("#{}: {}\n".format(rank[i],college[i]))
				
for i in range(pnum):
	scrape(i+1)