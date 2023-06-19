import xml.etree.ElementTree as ET
from os import getenv
from dotenv import find_dotenv, load_dotenv
from xml.dom import minidom
load_dotenv(find_dotenv())

S3_CDN_URL = getenv('S3_CDN_URL')
S3_OBJECT_EXPORT_INDEX = getenv('S3_OBJECT_EXPORT_INDEX')
S3_OBJECT_EXPORT_URL = getenv('S3_OBJECT_EXPORT_URL')
S3_OBJECT_EXPORT_INDEX_NAME = getenv('S3_OBJECT_EXPORT_INDEX_NAME')

RSS_TITEL = getenv('RSS_TITEL')
RSS_LANGUAGE = getenv('RSS_LANGUAGE')
RSS_LANGUAGE = getenv('RSS_LANGUAGE')
RSS_DESCRIPTION = getenv('RSS_DESCRIPTION')
RSS_GENERATOR = getenv('RSS_GENERATOR')

def GenerateXML(filename, data):
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = RSS_TITEL
    ET.SubElement(channel, "link").text = S3_OBJECT_EXPORT_URL+ S3_OBJECT_EXPORT_INDEX
    ET.SubElement(channel, "language").text = RSS_LANGUAGE
    ET.SubElement(channel, "description").text = RSS_DESCRIPTION
    ET.SubElement(channel, "generator").text = RSS_GENERATOR

    for product in data:
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = product['values']['name'][0]['data']
        if 'url' in product['values']:
            ET.SubElement(item, "link").text = product['values']['url'][0]['data']
        if 'disambiguatingDescription' in product['values']:
            ET.SubElement(item, "description").text = product['values']['disambiguatingDescription'][0]['data']
        #urlAttribute = "https://jrtagpimtsoch.sos-ch-dk-2.exoscale-cdn.com/catalog/3/2/3/8/32380c71b0fea38b4c69fefce054d0f322c9c501_wellness_hotel_glacier__1_.jpg"
        if 'image' in product['values']:
            urlAttribute = S3_CDN_URL + product['values']['image'][0]['data']
            lengthAttribute = ""
            typeAttribute = "image/jpeg"
            dict = {'url': urlAttribute, 'length': lengthAttribute, 'type': typeAttribute}
            new = ET.Element("enclosure", dict)
        item.append(new)
        for category in product['categories']:
            ET.SubElement(item, "category").text = category
        ET.SubElement(item, "pubDate").text = product['updated']
        ET.SubElement(item, "guid").text = product['identifier']

    tree = ET.ElementTree(rss)
    tree.write(filename)
    return tree


def transform(data):
    rssdata = GenerateXML(r'output/'+S3_OBJECT_EXPORT_INDEX_NAME, data)
    return rssdata
