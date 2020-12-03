import wacky_beer as wb

urls = wb.beer_styles_urls()
bs_id, fobj = wb.bs_soup(urls[0][1])
print(bs_id)
print(fobj)