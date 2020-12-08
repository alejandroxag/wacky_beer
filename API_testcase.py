# test case for API code


import API_v4 as API #import the API program

style = 'Porter'
beerList = API.fetchBrew(style)

for line in beerList:
    Name,Style,Category,Brewery,Country,State,City,Address = line
    print('Beer Name: '+Name)
    print('Style: '+Style)
    print('Category: '+Category)
    print('Brewery: '+Brewery)
    print('Country: '+Country)
    print('State: '+State)
    print('City: '+City)
    print('Address: '+ Address)
    print()
    
    
state = input('Enter a state: ')
city = input('Enter a city: ')

breweryList = API.findBrewery(style,city,state)
for line in breweryList:
    Name,Style,Category,Brewery,Country,State,City,Address = line
    print('Beer Name: '+Name)
    print('Style: '+Style)
    print('Category: '+Category)
    print('Brewery: '+Brewery)
    print('Country: '+Country)
    print('State: '+State)
    print('City: '+City)
    print('Address: '+ Address)
    print()