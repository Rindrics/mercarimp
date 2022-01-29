class SearchCondition:
    def __init__(self, keyword):
        self.set_keyword(keyword)

    def set_keyword(self, keyword):
        self.keyword = keyword

    def set_commodity_condition(self, condition):
        self.commodity_condition = condition
