import pandas as pd

beer_datafile_loc = 'data/beer_merged_data.csv'
beer_info = pd.read_csv(beer_datafile_loc)


def fetchBeerReviews(style_match, count=0):
    style_key = style_match[1]
    print('style_key is '+style_key)
    result = beer_info[beer_info['style'] == style_key]
    result = result[['name', 'state', 'score']]
    result = result.sort_values(by=['score','name'], ascending=[False,True])
    result = result.reset_index()
    if count == 0:
        return result
    else:
        return result[:count]

