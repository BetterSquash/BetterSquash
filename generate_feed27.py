import os
import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree, tostring, register_namespace
from xml.dom.minidom import parseString
from bs4 import BeautifulSoup
import pytz

def create_rss_feed():
    # Register the 'atom' namespace
    register_namespace('atom', 'http://www.w3.org/2005/Atom')

    rss = Element('rss', version='2.0')
    channel = SubElement(rss, 'channel')

    # Channel details
    channel_details = {
        'title': 'BETTERSQUASH',
        'description': 'If you are looking to improve your squash, you have visited the right website!',
        'link': 'https://bettersquash.com',
        'language': 'en',
        'copyright': '© 2003-2024 Phillip Marlowe',
        'webMaster': 'squashcoachphillip@gmail.com (Phillip Marlowe)'
    }

    for key, value in channel_details.items():
        SubElement(channel, key).text = value

    # Image element
    image = SubElement(channel, 'image')
    image_details = {
        'link': 'https://bettersquash.com',
        'title': 'BETTERSQUASH',
        'url': 'https://bettersquash.com/fav/favicon-32x32.png',
        'description': 'Improve Your Squash Today',
        'height': '32',
        'width': '32'
    }

    for key, value in image_details.items():
        SubElement(image, key).text = value

    # Atom link element
    atom_link = SubElement(channel, '{http://www.w3.org/2005/Atom}link', href='https://bettersquash.com/bettersquash_feed.xml', rel='self', type='application/rss+xml')

    # Walk through the directory and process HTML files
    for root, dirs, files in os.walk('.'):
        if '/srm/' in root:
            continue

        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')
                    title = soup.title.string if soup.title else 'No Title'
                    description = soup.find('meta', attrs={'name': 'description'})
                    description = description['content'] if description else 'No Description'

                    link = f"https://bettersquash.com/{os.path.relpath(file_path).replace(os.sep, '/')}"
                    pub_date = datetime.datetime.now(pytz.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')

                    item = SubElement(channel, 'item')
                    item_details = {
                        'title': title,
                        'link': link,
                        'description': description,
                        'author': 'squashcoachphillip@gmail.com (Phillip Marlowe)',
                        'guid': link,
                        'pubDate': pub_date
                    }

                    for key, value in item_details.items():
                        SubElement(item, key).text = value

    # Convert to pretty XML string
    dom = parseString(tostring(rss))
    pretty_xml_as_string = dom.toprettyxml(indent="   ")

    # Write to XML file
    with open('bettersquash_feed27.xml', 'w', encoding='utf-8') as f:
        f.write(pretty_xml_as_string)

if __name__ == "__main__":
    create_rss_feed()
