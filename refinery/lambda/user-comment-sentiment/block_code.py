import sys
sys.path.append("/opt")


from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import nltk
nltk.data.path.append("/opt/nltk_data")

def main(block_input, backpack):
    """
    :returns: dict for the analysis type sentiments and
              a list of dicts for each tag's sentiment classification
    """

    sentiments = []
    for tag in block_input:
        name = tag["name"]
        comment = tag["comment"]

        blob = TextBlob(comment, analyzer=NaiveBayesAnalyzer())
        sentiments.append(dict(
            name=name,
            result=blob.sentiment.classification
        ))

    return dict(sentiments=sentiments)

