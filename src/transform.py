import xml.etree.ElementTree as ET
from os import getenv
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

S3_CDN_URL = getenv('S3_CDN_URL')

def GenerateXML(filename, data):
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = "Jungfrau Region Tourismus AG - Alle Daten"
    ET.SubElement(channel, "link").text = "opendata.jungfrauregion.swiss/api/catgory/products.rss"
    ET.SubElement(channel, "language").text = "de-ch"
    ET.SubElement(channel, "docs").text = "opendata.jungfrauregion.swiss/api"
    ET.SubElement(channel, "description").text = "Alle Daten der Jungfrau Region Tourismus AG von jrtag.pim.tso.ch als RSS"
    ET.SubElement(channel, "generator").text = "Contentdesk.io"

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
        ET.SubElement(item, "category").text = "Experience"
        ET.SubElement(item, "category").text = "Grindelwald"
        ET.SubElement(item, "pubDate").text = "Sun, 06 Sep 2009 16:20:00 +0000"
        ET.SubElement(item, "guid").text = product['identifier']

    tree = ET.ElementTree(rss)
    tree.write(filename)
    return tree


def transform(data):
    rssdata = GenerateXML('all.rss', data)
    return rssdata
