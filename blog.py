from bs4 import BeautifulSoup as soup
from urllib.request import Request,urlopen

def blogs(var):
        data = []
        page_url= "https://www.google.com/search?q="+var+"+blog&oq="+var+"+blog&aqs=chrome..69i57j0l7.9347j0j7&sourceid=chrome&ie=UTF-8"
        req = Request(page_url,headers={'User-Agent':'Mozilla/5.0'})
        client = urlopen(req).read()
        page_soup = soup(client,"html.parser")
        containers= page_soup.findAll("div",{"class":"BNeawe vvjwJb AP7Wnd"})
        titles=[]
        for container in containers :
            titles.append(container.text)
        links=[]
        urls = page_soup.findAll("div",{"class":"kCrYT"})
        for url in urls:
            links.append(url.find("a",href=True))
        urls = []
        for link in links:
            if link != None:
                a = urls.append(link.attrs['href'][7:])
                urls.append(a)
        ur = []
        prev = urls[0].split('/')[2]
        ur.append(urls[0].split('&')[0][:-1])
        for url in urls:
            if url != None:
                slash = url.split('/')[2]
                if(slash!=prev):
                    ur.append(url.split('&')[0][:-1])
                prev = slash
        for i in range (0,len(titles)):
            dr=[]
            dr.append(titles[i])
            dr.append(ur[i])
            data.append(dr)
        return data
