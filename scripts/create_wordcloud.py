from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import traceback

twitter_ignore_list = ['https', 'bernie', 'http', 'https', 'BernieSanders',
'Sanders', 'RT', 'Hillary', 'HillaryClinton']


# Create a mapping of legislator to government id
# thesea are on https://www.govtrack.us
candidates = {
    'Bernie': 400357,
    'Hillary': 300022,
    'Cruz': 412573,
    'Kasich':400590
 }


def words_in_string(word_list, a_string):
    return set(word_list).intersection(a_string.split())


def create_wordcloud(inputfile, outputfile, text):

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # take relative word frequencies into account, lower max_font_size
    #wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
    wc = WordCloud(relative_scaling=.5).generate(text)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

    wc.to_file(outputfile)


def create_twitter_wordclouds():

    # create word clouds for the twitter files
    for gov_name, gov_id in candidates.items():
        inputfile = "twitter_" + gov_name + ".csv"
        outputfile = "twitter_wordcloud_" + gov_name + ".png"

        tweets = pd.read_csv(inputfile, encoding="utf-8")

        text = ""
        for index, row in tweets.iterrows():
            cur_text = tweets.text[index]
            for word in twitter_ignore_list:
                cur_text = cur_text.replace(word, '')
            text += cur_text

        create_wordcloud(inputfile, outputfile, text)


def create_bills_wordclouds():
    # create word clouds for the bill files

    inputfile = 'realdonaldtrump_tweets.csv'
    result = pd.read_csv(inputfile, encoding="utf-8")

    text = ""
    for index, row in result.iterrows():
        text += result.clean_title[index]

    create_wordcloud(inputfile, outputfile, text, None)


if __name__ == '__main__':

    try:
        #create_bills_wordclouds()
        create_twitter_wordcloud()

    except:
        traceback.print_exc()
