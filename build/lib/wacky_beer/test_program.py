#Final Project - Search Function

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
        print(rl)
    else:
        for i, result in enumerate(rl[1]):
            print("%d. %s" % (i + 1, result))
        userInput = int(input("Here are the potential styles you are looking for. Pick one option: "))
        while userInput not in range(1, len(rl[1]) + 1):
            userInput = int(input("Invalid option. Pick one option: "))
        style_match = rl[1][userInput]

    # style_info = wb.bs_getinfo(style_match[0])

if __name__ == '__main__': main()


