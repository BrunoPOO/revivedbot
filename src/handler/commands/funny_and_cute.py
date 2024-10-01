from calendar import c
from .base import Base
import urllib
import urllib.request
from bs4 import BeautifulSoup
from src.utils import random_element
#import xml.etree.ElementTree as ET


RULE34_URL = "https://safebooru.org/index.php?page=dapi&s=post&limit=10000&q=index&tags=loli%20"

class Loli(Base):
    name = 'loli'
    aliases = ['lolis', 'cunny', 'cute']

    def execute(self, command):
        print('entrou') 
        tags = '20%'.join(command.args)
        random_img = self.get_images(tags)
        img_url= random_img['img'] 
        tags= str(random_img['tags'])
        post_id = random_img['post_id']
        try:
            self.reply_with_photo(command, img_url, "Tags:\n" + tags + "\n\nOrigem:\nhttps://safebooru.org/index.php?page=post&s=view&id=" + post_id)
        except Exception as e:
            self.reply(command, "Não encontrei nenhuma loli :(" + repr(e))         
    
    def get_images(self, tags):
        url = RULE34_URL + tags
        result = urllib.request.urlopen(url)
        data = result.read()
        soup = BeautifulSoup(data)
        #xml_data = ET.fromstring(data)
        imgs = soup.find_all("post")
        img_list =[{}]
        for img in imgs:
            img_list.append({'img': img.get('file_url'), 'tags': img.get('tags'), 'post_id': img.get('id')})

        img_final = random_element(img_list)
        print(img_final)
        return img_final
