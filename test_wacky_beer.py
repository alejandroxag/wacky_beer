import wacky_beer as wb

urls = wb.beer_styles_urls()
print(wb.bs_getinfo(urls[0][1]))