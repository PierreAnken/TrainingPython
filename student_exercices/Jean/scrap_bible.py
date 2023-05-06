import requests as requests
from bs4 import BeautifulSoup

url_base = 'http://www.info-bible.org/lsg/'
reponse = requests.get(url_base)
soup = BeautifulSoup(reponse.text, 'html.parser')
liens = soup.find_all('a', href=True)

liens_textes = [lien for lien in liens if lien['href'][0].isdigit()]

texte_bible = ''

for lien in liens_textes:
    reponse = requests.get(url_base + lien['href'])
    soup = BeautifulSoup(reponse.text, 'html.parser')
    # TODO cleanup

print(texte_bible)
