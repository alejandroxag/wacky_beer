# Test program for the python package wacky_beer

import wacky_beer as wb

def main():
    styles_table = wb.bs_relation()
    userInput = input("Search a beer style: ")
    while True:
        rl = wb.bs_search(styles_table, userInput)
        if len(rl[1]) > 0: break
    if len(rl[1]) == 1:
        print("Here is what we have for you for %s:" % (rl[1][0][0]))
        style_match = rl[1][0]
    else:
        for i, result in enumerate(rl[1]):
            print("%d. %s" % (i + 1, result))
        userInput = int(input("Here are the potential styles you are looking for. Pick one option: "))
        while userInput not in range(1, len(rl[1]) + 1):
            userInput = int(input("Invalid option. Pick one option: "))
        style_match = rl[1][userInput - 1]

    style_info = wb.bs_getinfo(wb.bs_findurl(style_match[0], wb.bs_urls())[0])
    print(f'\nThe style you chose is {style_info["NAME"]}. This beer style belons to the group of {style_info["CAT"]}. '
          f'This type of beer is characterized for its {style_info["FEATURES"]["APPEARANCE"]["COLOR"].lower()} color '
          f'({style_info["COLOR"][:(style_info["COLOR"].find(" SRM"))]} in the SRM scale), its '
          f'{"low" if int(style_info["IBU"][3:5]) < 100/3 else ("medium" if int(style_info["IBU"][3:5]) < 200/3 else "high")} bitterness flavor, ({style_info["IBU"]}) '
          f'and its {"light" if 0.5 * (float(style_info["ABV"][0:3]) + float(style_info["ABV"][4:7])) < 5.5 else ("medium" if 0.5 * (float(style_info["ABV"][0:3]) + float(style_info["ABV"][4:7])) < 11.0 else "high")} alcoholic volume '
          f'({style_info["ABV"]}). The ideal way to taste this type of beer is at a {style_info["TEMP"]} temperature, in a {style_info["GLASSWARE"][0].lower()} glass '
          f'({style_info["GLASSWARE"][1].lower()}).\n'
          f'This beer is ideal to pair with ', end = '')
    for i, p in enumerate(style_info['PAIRINGS']):
        if i == len(style_info['PAIRINGS']) - 1: print(p.lower(), end = '. ')
        else: print(p.lower(), end = ', ')
    print(f'If you like this beer style, maybe you would like to try these ones: ', end = '')
    for i, p in enumerate(style_info['SUGG']):
        if i == len(style_info['PAIRINGS']) - 1: print(p.lower(), end = '. ')
        else: print(p.lower(), end = ', ')
    print(f'\n\nHere is a brief description from the website CraftBeer.com:\n\n {style_info["DESC"]}')
    print(f'\nAnd here is a full X-Ray of this beer style (also from CraftBeer.com):')
    for k in style_info['FEATURES'].keys():
        print(f'\n{k.title()}')
        for k2 in style_info['FEATURES'][k]: print(f'\t{k2.title()}: {style_info["FEATURES"][k][k2].lower()}')

if __name__ == '__main__': main()


