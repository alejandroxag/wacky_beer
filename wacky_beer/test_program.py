#Final Project - Search Function

import wacky_beer as wb

def main():
    styles_table = wb.bs_relation()
    while True:
        userInput = input("Search a beer style (type QUIT to quit): ")
        if userInput.upper()=='QUIT':
            break
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
            style_match = rl[1][userInput - 1]

        style_info = wb.bs_getinfo(wb.bs_findurl(style_match[0], wb.bs_urls())[0])
        print(style_info)
        print(style_match[2])
        state = input('Enter a state: ')
        breweryList = wb.findBrewery(style_match[2], state)
        for line in breweryList:
            Name, Style, Category, Brewery, Country, State, City, Address = line
            print('Beer Name: ' + Name)
            print('Style: ' + Style)
            print('Category: ' + Category)
            print('Brewery: ' + Brewery)
            print('Country: ' + Country)
            print('State: ' + State)
            print('City: ' + City)
            print('Address: ' + Address)
            print()

        beer_reviews = wb.fetchBeerReviews(style_match, 5)
        if beer_reviews.empty:
            print('No Beer reviews founds for this style.')
        else:
            print('Top 5 beers reviewed of this style: ')
            print(beer_reviews)

if __name__ == '__main__': main()


