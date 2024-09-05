# imports
from bs4 import BeautifulSoup
import requests 
from Hash_set import Hash_Set


url = "https://quotes.toscrape.com"
response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")

# find all quotes and authors
quotes = soup.find_all("span", attrs = {"class":"text"})
authors = soup.find_all("small", attrs = {"class":"author"})

# create a hash set
hs = Hash_Set(50)

# organizes quotes to authors then inserts into a hash set
for quote, author in zip(quotes, authors):
    hs.insert(f"{quote.text}\n - {author.text}")
    
# uncomment to show quotes stored
hs.debug()




