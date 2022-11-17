import os
import aiohttp
import asyncio
from tqdm.asyncio import trange, tqdm


def main():
    links = load_links_from_file('Ressources/Bestiarium/Tiere/Tier-liste.txt')
    pages = asyncio.run(crawl_all_links(links))


def load_links_from_file(ressource):
    res_path = os.path.abspath(ressource)
    links = []
    if os.path.exists(res_path):
        with open(res_path, 'r') as file:
            links = file.read().splitlines()
    return links


async def crawl_all_links(links):
    pages = {}
    async with aiohttp.ClientSession() as session:
        async for i in trange(len(links)):
            link = links[i]
            async with session.get(link) as response:
                pages[link] = await crawl_content_from_response(response.text())
    return pages

async def crawl_content_from_response(response):
    # get content
    return response

def write_content_to_table(content):
    pass


if __name__ == '__main__':
    main()