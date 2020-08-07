
class JsonQueries:
    def __init__(self, item_list):
        self.tabula_rasa_query = ""
        self.enlighten_2_query = ""
        self.enlighten_3_query = ""
        self.perandus_blazon_query = ""
        self.item_list = item_list
        self.initialize_queries()

    def initialize_queries(self):
        self.tabula_rasa_query = {"query": {"status": {"option": "online"},
                                            "name": "Tabula Rasa",
                                            "filters": {"trade_filters": {"disabled": False, "filters": {"price": {"max": self.item_list["tabula_rasa"]}}}},
                                            "stats": [{"type": "and", "filters": []}]}, "sort": {"price": "asc"}}

        self.enlighten_3_query = {"query": {"status": {"option": "online"},
                                            "type": "Enlighten Support",
                                            "filters": {"trade_filters": {"disabled": False, "filters": {"price": {"max": self.item_list["enlighten_3"]}}},
                                                        "misc_filters": {"filters": {"gem_level": {"min": 3, "max": 3}}}}}, "sort": {"price": "asc"}}

        self.enlighten_2_query = {"query": {"status": {"option": "online"},
                                            "type": "Enlighten Support",
                                            "filters": {"trade_filters": {"disabled": False, "filters": {"price": {"max": self.item_list["enlighten_2"]}}},
                                                        "misc_filters": {"filters": {"gem_level": {"min": 2, "max": 2}}}}}, "sort": {"price": "asc"}}

    def get_query(self, item):
        if item == "tabula_rasa":
            return self.tabula_rasa_query
        elif item == "enlighten_2":
            return self.enlighten_2_query
        elif item == "enlighten_3":
            return self.enlighten_3_query
