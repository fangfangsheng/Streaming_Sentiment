import re, config

class Tweet:

    def __init__(self, data):
        self.data = data

    def user_link(self):
        return 'http://twitter.com/{}'.format(self.data['username'])

    def filtered_text(self):
        return self.filter_keywords(self.filter_urls(self.data['text']))

    def filter_keywords(self, text):
        keywords = list(config.keyword)

        for keyword in keywords:
            if keyword in text:
                text = text.replace(keyword, '<mark>{}</mark>'.format(keyword))
            else:
                continue
        return text

    def filter_urls(self, text):
        return re.sub("(https?:\/\/\w+(\.\w+)+(\/[\w\+\-\,\%]+)*(\?[\w\[\]]+(=\w*)?(&\w+(=\w*)?)*)?(#\w+)?)", r'<a href="\1" target="_blank">\1</a>', text)
       
