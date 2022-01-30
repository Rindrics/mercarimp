from http.client import HTTPSConnection


class SearchCondition:
    _valid_item_conditions = {
        # メルカリの定義合わせて 1 始まりとした
        1: "新品、未使用：購入してからあまり時間が経っておらず、一度も使用していない",
        2: "未使用に近い：数回しか使用しておらず、傷や汚れがない",
        3: "目立った傷や汚れなし：よく見ないとわからない程度の傷や汚れがある",
        4: "やや傷や汚れあり：中古品とわかる程度の傷や汚れがある",
        5: "傷や汚れあり：誰がみてもわかるような大きな傷や汚れがある",
        6: "全体的に状態が悪い",
    }

    _valid_status = {
        0: "sold_out",
        1: "on_sale",
    }

    def __init__(self, keyword):
        self.set_keyword(keyword)

    def set_keyword(self, keyword):
        self.keyword = keyword

    def set_item_condition_id(self, condition_id):
        self._validate_item_condition_id(condition_id)
        self.item_condition_id = condition_id

    def _validate_item_condition_id(self, condition_id):
        if type(condition_id) != int:
            raise TypeError
        if condition_id not in self._valid_item_conditions.keys():
            raise ValueError

    def set_status(self, status_id):
        self._validate_status_id(status_id)
        self.status = self._valid_status[status_id]

    def _validate_status_id(self, status_id):
        if type(status_id) != int:
            raise TypeError
        if status_id not in self._valid_status.keys():
            raise ValueError

    def query(self):
        url = (
            "https://jp.mercari.com/search?"
            + "keyword="
            + self.keyword
            + "&item_condition_id="
            + str(self.item_condition_id)
            + "&status="
            + self.status
        )
        conn = HTTPSConnection("www.python.org")

        conn.request("GET", url)
        response = conn.getresponse()

        return response.read()
