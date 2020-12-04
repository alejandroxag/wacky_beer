import wacky_beer as wb
import json
import random

def main():
    name, url = wb.beer_styles_urls()[random.randrange(0,80,1)]
    print(name)
    print(url)
    print(wb.bs_getinfo(url))
    # with open('beer-styles-info.json','w') as f: json.dump({url[0]:dict([('url', url[1]), ('bs-info',wb.bs_getinfo(url[1]))]) for url in wb.beer_styles_urls()}, f, indent = 4)
if __name__ == "__main__": main()