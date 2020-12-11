import pandas as pd
import numpy as np
import os.path as path
import fuzzymatcher
import recordlinkage


beer_datafile_loc = 'data/beer_merged_data.csv'
beer_info = pd.read_csv(beer_datafile_loc)


def fetchBeerReviews(style_match, count=0):
    style_key = style_match[1]
    # print('style_key is '+style_key)
    result = beer_info[beer_info['style'] == style_key]
    result = result[['name', 'state', 'score']]
    result = result.sort_values(by=['score','name'], ascending=[False,True])
    result = result.reset_index()
    if count == 0:
        return result
    else:
        return result[:count]


def processDataset(dataset_path):
    beers_df = pd.read_csv(path.join(dataset_path, 'beers.csv'))
    breweries_df = pd.read_csv(path.join(dataset_path, 'breweries.csv'))
    reviews_df = pd.read_csv(path.join(dataset_path, 'reviews.csv'))
    reviews_mean_df = reviews_df[['beer_id', 'overall', 'score']].groupby(by='beer_id').mean()
    beer_merged_df = pd.merge(left=beers_df[['id', 'name', 'brewery_id', 'state', 'country', 'style']],
                              right=reviews_mean_df, how='inner', left_on='id', right_on='beer_id')
    beer_merged_us_df = beer_merged_df[beer_merged_df['country'] == 'US']
    beer_merged_us_df = beer_merged_us_df[beer_merged_us_df['style'].notnull()]
    beer_merged_us_df.to_csv('data/gen_beer_merged_data.csv', index=False)


def matchStyles(dataset_path):
    beers_df = pd.read_csv(path.join(dataset_path, 'beers.csv'))
    beers_style_list = list(beers_df.groupby(by=['style'], axis=0).count().index)
    beers_style_df = pd.DataFrame(beers_style_list, columns=['style'])
    craft_beer_style_df = pd.read_csv('data/craftbeer_beerstyles.csv')
    left_on = ['Craft_Beer_Styles']
    right_on = ['style']
    matched_results = fuzzymatcher.fuzzy_left_join(craft_beer_style_df,
                                                   beers_style_df,
                                                   left_on,
                                                   right_on,
                                                   left_id_col='Craft_Beer_Styles',
                                                   right_id_col='style')
    matched_results.to_csv('data/beerstyles_matched.csv')