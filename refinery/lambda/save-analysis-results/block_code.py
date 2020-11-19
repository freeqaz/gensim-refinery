from pynamodb.exceptions import DoesNotExist

from shared_files.models import UserModel, TagModel

"""
The configured analysis types which have been executed prior to this block.
"""
analysis_types = ["sentiments", "summaries"]

def merge_results(analysis_type: str, return_results: dict, analysis: dict) -> None:
    """
    :param analysis_type: the type of analysis to merge results from analysis into results
    :param results: map of tags to their 
    :param analysis: map of analysis types to the results of the analysis
    """

    analysis_results = analysis.get(analysis_type)
    if analysis_results is None:
        return

    for analysis_result in analysis_results:
        name = analysis_result["name"]
        result = analysis_result["result"]
        if return_results.get(name) is None:
            return_results[name] = {t: [] for t in analysis_types}
        
        return_results[name][analysis_type].append(result)

def analysis_type_merge(analysis_type: str, results: dict, analysis: dict) -> None:   
    if analysis_type not in analysis_types:
        print(f"analysis results are not handled: {analysis}")
        return

    merge_results(analysis_type, results, analysis)

def main(block_input, backpack):
    results = dict()
    for analysis in block_input:
        for analysis_type in analysis:
            analysis_type_merge(analysis_type, results, analysis)

    #username = backpack["username"]
    username = "demo"
    try:
        user = UserModel.get(username)
    except DoesNotExist:
        print(f"user not able to be found: {username}")
        return

    if user.tag_names is None:
        user.tag_names = []

    for name, analyses in results.items():
        tag = TagModel.query(name, user.user_id)
        
        if tag.total_count == 0:
            tag = TagModel(name, user.user_id)

        if tag.comment_sentiments is None:
            tag.comment_sentiments = []
        tag.comment_sentiments.extend(analyses["sentiments"])

        if tag.comment_summaries is None:
            tag.comment_summaries = []
        tag.comment_summaries.extend(analyses["summaries"])
        tag.save()

        user.tag_names.append(tag.name)

    user.save()
