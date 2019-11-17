import pandas as pd
import json
import emoji
import regex
from pymongo import MongoClient
import re

def split_count(text):

    emoji_list = []
    data = regex.findall(r'\X', text)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI for char in word):
            emoji_list.append(word)

    flags = regex.findall(U'[\U0001F1E6-\U0001F1FF]', text)

    return emoji_list + flags


# Connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://localhost/')
db = client['twitter_collect_db']
# Issue the serverStatus command and print the results
collection = db['tweet_collect']
# print('Total Record for the collection: ' + str(collection.count()))
cursor = collection.find()  #.limit(20)

column_names = ['user_name','tweeted_time','full_text','num_follower','country','language','emoji']
# full_df = pd.DataFrame(columns=column_names)

file = open('co-mention-tweets.csv', 'w')

for data in cursor:
    dict_ = {}
    emojis = []
    pure_text = ''.join(data['text'].splitlines())

    if re.search('^RT', pure_text):
        pure_text = ''.join(pure_text.split(':')[1:]).split('#')[0].split("https")[0]
    else:
        pure_text = pure_text.split('#')[0].split("https")[0]

    counter = split_count(pure_text)
    if len(counter) == 0:
        pass
    else:
        user = data['user_name']
        time = data['tweeted_at']
        follwers = data['num_follower']
        # country = data['country']
        language = data['lang']
        for face in counter:
            # print(emoji.demojize(face)[1:-1].replace('_',' '))
            emojis.append(emoji.demojize(face)[1:-1].replace('_', ' '))
            pure_text = re.sub(face, '', pure_text)
        dict_ = {'user_name': user,
                 'tweeted_time': time,
                 'full_text': pure_text,
                 'num_follower': follwers,
                 # 'country': country,
                 'language': language,
                 'emoji': emojis}
        for k, v in dict_.items():
            file.write(str(v) + '>')
        file.writelines('\n')
# full_df.to_csv(r'co-mention-tweets.csv', header=None, index = None, sep=' ', mode='w')

print('Finished')

