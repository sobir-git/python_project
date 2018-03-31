"""This python script compiles a list of updates from the source mangatown.com and
displays the information in a list. 
*FUTURE PLAN: Integrate functionality into current manga app to obtain and display
updates on a different screen"""
import urllib.request
from bs4 import BeautifulSoup

try:
    url= 'http://www.mangatown.com/latest/text/'
    urllib.request.urlopen(url)    
except urllib.error.HTTPError as e:
    print("created previously missing table, please run application again")
    print(e.code)


url= 'http://www.mangatown.com/latest/text/'#URL to pull information from
request= urllib.request.Request(url)
response= urllib.request.urlopen(request)
soup = BeautifulSoup(response, 'html.parser')#Parse entire webpage
#name_box = soup.find('ul', attrs={'class': 'chapter_list'})#finds unordered list of chapter updates

chapter_list = soup.find('div', attrs={'class':'manga_text_content'})#finds div that contains chapter updates

hot_updates = chapter_list.find_all('span', attrs={'class':'hot'})#compiles chapter_list and find all 'HOT' updates

"""Below loop iterates through the list of updates and takes the parent HTMl
tag of <span class="hot">HOT</span> Then obtains the hyperlink and name of the items
within the hot chapter list"""
for item in hot_updates:
    parent_of_updates= item.parent #obtain parent tag of class="hot" tag
    content_of_parent= parent_of_updates.contents #display contents of parent tag
    update_url= content_of_parent[1]['href'] #contains url of updated manga
    updated_name= content_of_parent[1]['rel']#contains name of updated manga
    print('url: ' + update_url + ' Name: ' + str(updated_name))

