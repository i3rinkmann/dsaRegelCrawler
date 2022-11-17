import os
import aiohttp
import asyncio


def main():
    links = load_links_from_file('Ressources/Bestiarium/Tiere/Tier-liste.txt')
    pages = asyncio.run(crawl_all_links(links))
    print(pages)



def load_links_from_file(ressource):
    res_path = os.path.abspath(ressource)
    links = []
    if os.path.exists(res_path):
        with open(res_path, 'r') as file:
            links = file.read().splitlines()
    return links

def crawl_link(url):
    content = ''
    return content


async def crawl_all_links(links):
    pages = {}
    async with aiohttp.ClientSession() as session:
        for link in links:
            async with session.get(link) as response:
                pages[link] = await response.text()
    return pages


if __name__ == '__main__':
    main()