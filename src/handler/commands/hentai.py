from calendar import c
from .base import Base
import urllib
import urllib.request
from bs4 import BeautifulSoup
from src.utils import random_element
#import xml.etree.ElementTree as ET


RULE34_URL = "https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags="

class Hentai(Base):
    name = 'hentai'

    def execute(self, command):
        tags = '%20'.join(command.args)
        print('entrou') 
        random_img = self.get_images(tags)
        img_url= random_img['img'] 
        tags= random_img['tags']
        post_id = random_img['post_id']
        try:
            self.reply_with_photo(command, img_url, "Tags:\n" + tags + "\n\nOrigem:\nhttps://gelbooru.com/index.php?page=dapi&s=post&q=index&tags=" + post_id)
        except Exception as e:
            self.reply(command, "Não foi possível encontrar ou enviar a imagem.\n" + 
            "Use (_) para espaços e escreva o nome corretamente!")         
    
    def get_images(self, tag):
        url = RULE34_URL + tag
        result = urllib.request.urlopen(url)
        data = result.read()
        soup = BeautifulSoup(data)
        #xml_data = ET.fromstring(data)
        imgs = soup.find_all("post")
        img_list =[{}]
        for img in imgs:
            img_list.append({'img': img.find('file_url').get_text(), 'tags': img.find('tags').get_text(), 'post_id': img.find('id').get_text()})

        img_final = random_element(img_list)
        print(img_final)
        return img_final