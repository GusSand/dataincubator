from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import traceback
import nltk
from nltk.corpus import stopwords


cachedStopWords = list(stopwords.words("english"))

twitter_ignore_list = ['https', 'bernie', 'http', 'https', 'BernieSanders',
'Sanders', 'RT', 'hillary', 'HillaryClinton', 'realDonaldTrump',
'trump2016',
'Trump', 'Trump2016', 'co', 'wn', 'Wn', 'en', 'wh', 'thank', 'thanks']


twitter_ignore_list.extend(cachedStopWords)

def create_wordcloud(inputfile, outputfile, text):

    # Generate a word cloud image
    print twitter_ignore_list

    wordcloud = WordCloud().generate(text)

    # take relative word frequencies into account, lower max_font_size
    #wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
    wc = WordCloud(relative_scaling=.5).generate(text)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

    wc.to_file(outputfile)


def create_twitter_wordcloud():

    #gov_name = "realdonaldtrump"
    gov_name = "hillaryclinton"
    inputfile = gov_name + "_tweets.csv"
    outputfile = "twitter_wordcloud_" + gov_name + ".png"

    tweets = pd.read_csv(inputfile, encoding="utf-8")

    text = ""
    for index, row in tweets.iterrows():
        cur_text = tweets.text[index]

        # split all the words in the tweet
        text_list = cur_text.split()

        # if the words are in the dictionary
        # and are not stopwords#
        # add them to the text
        for word in text_list:
            word = word.lower()
            if is_english_word(word) and not is_ignore_list(word):
                #print word
                text = text + ' ' + word

    # Finally create the word cloud
    create_wordcloud(inputfile, outputfile, text)

with open("english_words.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def is_english_word(word):
    return word.lower() in english_words


def is_ignore_list(word):
    return word.lower() in ignore_list

def test_stuff():
    # first split all the words

    text = ""
    cur_text = 'Thanks thank thanks I will be interviewed on @foxandfriends with the legendary Coach Bobby Knight- tomorrow morning.'
    text_list = cur_text.split()

    # if the words are in the dictionary
    # and are not stopwords#
    # add them to the text

    #print "original ===> " + cur_text

    for word in text_list:
        word = word.lower()
        if is_english_word(word) and not is_ignore_list(word):
            print word
            text = text + ' ' + word

    print text

if __name__ == '__main__':
    try:
        #create_bills_wordclouds()
        #print is_english_word("ham")
        ignore_list = set(twitter_ignore_list)

        #test_stuff()

        create_twitter_wordcloud()

    except:
        traceback.print_exc()
