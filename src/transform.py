import xml.etree.ElementTree as ET

def GenerateXML(filename, data):
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = "My Channel"
    ET.SubElement(channel, "link").text = "http://example.com/"
    ET.SubElement(channel, "language").text = "de-ch"
    ET.SubElement(channel, "description").text = "This is an example of an RSS feed"
    ET.SubElement(channel, "generator").text = "Contentdesk.io"

    item = ET.SubElement(channel, "item")
    ET.SubElement(item, "title").text = "Example entry"
    ET.SubElement(item, "link").text = "http://example.com/blog/post/1"
    ET.SubElement(item, "description").text = "Here is some text containing an interesting description."
    urlAttribute = "https://jrtagpimtsoch.sos-ch-dk-2.exoscale-cdn.com/catalog/3/2/3/8/32380c71b0fea38b4c69fefce054d0f322c9c501_wellness_hotel_glacier__1_.jpg"
    lengthAttribute = "12345"
    typeAttribute = "image/jpeg"
    dict = {'url': urlAttribute, 'length': lengthAttribute, 'type': typeAttribute}
    new = ET.Element("enclosure", dict)
    item.append(new)
    #ET.SubElement(item, "enclosure").url = "https://jrtagpimtsoch.sos-ch-dk-2.exoscale-cdn.com/catalog/3/2/3/8/32380c71b0fea38b4c69fefce054d0f322c9c501_wellness_hotel_glacier__1_.jpg"
    #ET.SubElement(item, "enclosure").length = ""
    #ET.SubElement(item, "enclosure").type = "image/jpeg"
    ET.SubElement(item, "category").text = "Experience"
    ET.SubElement(item, "category").text = "Grindelwald"
    ET.SubElement(item, "pubDate").text = "Sun, 06 Sep 2009 16:20:00 +0000"
    ET.SubElement(item, "guid").text = "7bd204c6-1655-4c27-aeee-53f933c5395f"

    tree = ET.ElementTree(rss)
    tree.write(filename)
    return tree


def transform(data):
    rssdata = GenerateXML('all.rss', data)
    return rssdata
