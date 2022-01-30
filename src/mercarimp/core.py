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

    _valid_deal_status = {
        0: "sold_out",
        1: "on_sale",
    }

    def __init__(self, keyword):
        self.set_keyword(keyword)

    def set_keyword(self, keyword):
        self.keyword = keyword

    def set_item_condition(self, condition):
        self._validate_item_condition(condition)
        self.item_condition = condition

    def _validate_item_condition(self, condition):
        if type(condition) != int:
            raise TypeError
        if condition not in self._valid_item_conditions.keys():
            raise ValueError

    def set_deal_status(self, status):
        self._validate_deal_status(status)
        self.deal_status = status

    def _validate_deal_status(self, condition):
        if type(condition) != int:
            raise TypeError
        if condition not in self._valid_deal_status.keys():
            raise ValueError
