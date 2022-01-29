class SearchCondition:
    _valid_commodity_conditions = {
        0: "新品、未使用：購入してからあまり時間が経っておらず、一度も使用していない",
        1: "未使用に近い：数回しか使用しておらず、傷や汚れがない",
        2: "目立った傷や汚れなし：よく見ないとわからない程度の傷や汚れがある",
        3: "やや傷や汚れあり：中古品とわかる程度の傷や汚れがある",
        4: "傷や汚れあり：誰がみてもわかるような大きな傷や汚れがある",
        5: "全体的に状態が悪い",
    }

    def __init__(self, keyword):
        self.set_keyword(keyword)

    def set_keyword(self, keyword):
        self.keyword = keyword

    def set_commodity_condition(self, condition):
        self._validate_commodity_condition(condition)
        self.commodity_condition = condition

    def _validate_commodity_condition(self, condition):
        if type(condition) != int:
            raise TypeError
        if condition not in self._valid_commodity_conditions.keys():
            raise ValueError
