# -*- coding: UTF-8 -*-
import itertools
import re
import pandas as pd
from pandas import Series, DataFrame


# data = pd.read_csv('co-mention-tweets.txt', sep='>', header=None, names=['user_name','tweeted_time','full_text','num_follower','language','emoji','Extra'],low_memory=False)
# print(data.shape)  #(167148, 7)
data = pd.read_csv('unique_tweets_en.csv', sep=' ')

emoji_short_code = data[['emojis']]
# print(emoji_short_code[:10])

freq_df = pd.DataFrame(columns=['First', 'Second'])

# with open('pure_emoji.txt','w') as f:
for index, row in emoji_short_code.iterrows():
    relations = row[0].split(', ')

    if len(relations) > 1:

        pairs = list(zip(relations, relations[1:]))
        # print(pairs)

        for pair in pairs:

            freq_df = freq_df.append({'First': pair[0], 'Second': pair[1]}, ignore_index=True)


freq_df = DataFrame({'Count': freq_df.groupby(['First', 'Second']).size()}).reset_index()
# print(freq_df)
print('Finished!!!')
freq_df.to_csv(r'weighted_edges.csv', index=None, mode='w')
