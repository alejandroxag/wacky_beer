import json
import requests

#returns a list of beers information from API of the selected style
def fetchBrew(style):
    headers = {'Content-Type': 'application/json'}    
    #the limit of return records is 300, this could be changed in the url
    url = 'https://data.opendatasoft.com/api/records/1.0/search/?dataset=open-beer-database%40public-us&rows=300&facet=style_name&facet=cat_name&facet=name_breweries&facet=country&refine.style_name='+style
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        if 'nhits' in data:
            count = data['nhits']
            beerList = list()
            for i in range(0,count):
                records = dict(data['records'][i])
                fields = records['fields']
                if 'name' in fields:
                    Name = (fields['name'])
                if 'style_name' in fields:
                    Style = (fields['style_name'])
                if 'cat_name' in fields:
                    Category = (fields['cat_name'])
                if 'name_breweries' in fields:
                    Brewery = (fields['name_breweries'])
                if 'country' in fields:
                    Country = fields['country']
                if 'state' in fields:
                    State = fields['state']
                if 'city' in fields:
                    City = fields['city']
                if 'address1' in fields:
                    Address = fields['address1']
                beerList.append([Name,Style,Category,Brewery,Country,State,City,Address])
    return beerList


def findBrewery(style,city,state):
    beerList = fetchBrew(style)
    breweryList = list()
    for line in beerList:
        Name,Style,Category,Brewery,Country,State,City,Address = line
        #count = 0
        if state in line:
            if city in line:
                breweryList.append([Name,Style,Category,Brewery,Country,State,City,Address])
                #while count < 6:
    return breweryList


def main(style):
    beerList = fetchBrew(style)


if __name__ == '__main__':
    main()   



