from flask import render_template

import feedparser

from flask import Flask

app = Flask(__name__)

RSS_FEED = {'bbc':'http://feeds.bbci.co.uk/news/world/rss.xml',
'cnn': 'http://rss.cnn.com/rss/edition_world.rss',
'nature':'http://feeds.nature.com/nature/rss/current',
'reuter':'http://feeds.reuters.com/Reuters/worldNews'}

@app.route('/')
@app.route('/<publication>')
def get_news(publication='bbc'):
    feed = feedparser.parse(RSS_FEED[publication])
    return render_template('home.html', articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)