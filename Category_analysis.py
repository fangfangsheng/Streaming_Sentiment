import pandas as pd
import numpy as np

## Finish first part of mapping
# emojis = pd.read_csv('edge_list_emoji_en.csv', sep=" ")
# print(emojis.head())
# emojis.to_csv(r'edge_list_emoji_en_new.csv', index=None,  mode='w')
# emoji_categ = pd.read_csv('emoji_df.csv')
# emoji_categ = emoji_categ.drop_duplicates('name', keep='last')
#
# node1 = emojis.source
# node2 = emojis.target
#
# nodes = np.concatenate((node1, node2))
#
# unqiue, counts = np.unique(nodes, return_counts=True)
#
# Count = dict(zip(unqiue, counts))
#
#
# nodes_df = pd.DataFrame(columns=['Emoji','group','count', 'version','unicode'])
#
#
# for emoji in unqiue:
#     freq = int(Count[emoji])
#     group = np.array_str(emoji_categ.loc[emoji_categ['name'] == emoji]['group'].values)[2:-2]
#     # sub_group = np.array_str(emoji_categ.loc[emoji_categ['name'] == emoji]['sub_group'].values)[2:-2]
#     version = np.array_str(emoji_categ.loc[emoji_categ['name'] == emoji]['version'].values)[1:-2]
#     unicode = np.array_str(emoji_categ.loc[emoji_categ['name'] == emoji]['emoji'].values)[2:-2]
#     # print(emoji, version)
#
#     nodes_df = nodes_df.append({'Emoji': emoji,
#                                 'group': group,
#                                 'count': freq,
#                                 'version': version,
#                                 'unicode': unicode}, ignore_index=True)
#
# nodes_df.to_csv(r'node_list_emoji_en.csv', index=None,  mode='w')

## Finish second part of mapping --- Nodes
# emojis = pd.read_csv('node_list_emoji_en.csv')
#
# for category in emojis.group.unique():
#     top6_name = emojis[emojis['group'] == category].sort_values(by='count', ascending=False)['Emoji'][:6].values
#     top6_count = emojis[emojis['group'] == category].sort_values(by='count', ascending=False)['count'][:6].values
#     print('In {}, the top 6 emojis are {} and the frequecnce is {}'.format(category, top6_name, top6_count))


# Finish third part of mapping --- Edges

# emojis = pd.read_csv('edge_list_emoji_en.csv', sep=" ")
# emoji_categ = pd.read_csv('emoji_df.csv')
# emoji_categ = emoji_categ.drop_duplicates('name', keep='last')
# nodes_df = pd.DataFrame(columns=['Source', 'Target', 'Counts'])
#
#
# for index, row in emojis.iterrows():
#     source = np.array_str(emoji_categ.loc[emoji_categ['name'] == row[0]]['group'].values)[2:-2]
#     target = np.array_str(emoji_categ.loc[emoji_categ['name'] == row[1]]['group'].values)[2:-2]
#     # cate = np.array_str(emoji_categ.loc[emoji_categ['name'] == row[0]]['group'].values) + np.array_str(emoji_categ.loc[emoji_categ['name'] == row[1]]['group'].values)
#     nodes_df = nodes_df.append({'Source': source, 'Target': target, 'Counts': row[2]}, ignore_index=True)
#
# # df_new = pd.pivot_table(nodes_df, index=['Source','Target'], values='Counts', aggfunc=len).rename('count')
#
# df_new = nodes_df.groupby(['Source', 'Target']).agg({'Counts': 'sum'}).reset_index()
#
# # print(df_new)
#
# for category in emojis.Category.unique():
#     top6_name_1 = emojis[emojis['Category'] == category].sort_values(by='Count', ascending=False)['First'][:6].values
#     top6_name_2 = emojis[emojis['Category'] == category].sort_values(by='Count', ascending=False)['Second'][:6].values
#     top6_count = emojis[emojis['Category'] == category].sort_values(by='Count', ascending=False)['Count'][:6].values
#     print('In {}, the top 6 emojis are {},{} and the frequecnce is {}'.format(category, top6_name_1, top6_name_2, top6_count))
#
# df_new.to_csv(r'category.csv', index=None,  mode='w')
