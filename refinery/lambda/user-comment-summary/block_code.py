import sys
sys.path.append('/opt')

from gensim.summarization.summarizer import summarize

def main(block_input, backpack):
    """
    :returns: dict for the analysis type summarizations and
              a list of dicts for each tag's summarization classification
    """

    summaries = []
    for tag in block_input:
        name = tag["name"]
        comment = tag["comment"]

        try:
            summaries.append(dict(
                name=name,
                result=summarize(comment)
            ))
        except ValueError:
            # summarize may not work on short comments
            summaries.append(dict(
                name=name,
                result=comment
            ))

    return dict(summaries=summaries)
