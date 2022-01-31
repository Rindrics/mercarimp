from http.client import HTTPSConnection

from mercarimp.query import construct_query


class CoreModule:
    def __init__(self):
        self.base_url = "jp.mercari.com"

    def query(self, search_condition):
        url = construct_query(
            "https://" + self.base_url + "/search?",
            search_condition.keyword,
            search_condition.item_condition_id,
            search_condition.status,
        )
        conn = HTTPSConnection(self.base_url)

        conn.request("GET", url)
        self.dom = conn.getresponse().read()
