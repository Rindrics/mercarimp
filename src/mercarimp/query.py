def construct_query(base_url, keyword, item_condition_id, status):
    url = (
        base_url
        + "keyword="
        + keyword
        + "&item_condition_id="
        + str(item_condition_id)
        + "&status="
        + status
    )
    return url
