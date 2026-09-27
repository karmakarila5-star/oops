class DailyDataHelper:
    def __init__(self, owner="rajdip"):
        self.owner = owner
        self.data_list = ["Wake up", "Exercise", "Work/Study", "Read a book", "Sleep"]
        print(f"--- [START] DailyDataHelper initialized for {self.owner} ---")

    def display_all(self):
        print(f"\nCurrent Daily Log for {self.owner}:")
        for index, value in enumerate(self.data_list):
            print(f"Index [{index}]: {value}")

    def search_by_index(self, index):
        try:
            value = self.data_list[index]
            print(f"\n[Search Success] Found at index [{index}]: '{value}'")
            return value
        except IndexError:
            print(f"\n[Search Error] Index [{index}] is out of bounds.")
            return None

    def search_by_value(self, value):
        clean_value = str(value).strip().lower()
        for index, item in enumerate(self.data_list):
            if str(item).strip().lower() == clean_value:
                print(f"\n[Search Success] '{item}' found at index [{index}].")
                return index
        print(f"\n[Search Error] '{value}' not found in the daily data.")
        return -1

    def add_data(self, new_item):
        self.data_list.append(new_item)
        print(f"\nAdded: '{new_item}' to the log.")

    def __del__(self):
        print(f"--- [END] DailyDataHelper object for {self.owner} has been destroyed ---")


if __name__ == "__main__":
    helper = DailyDataHelper("rajdip")
    helper.display_all()
    helper.add_data("Meditation")
    helper.display_all()
    helper.search_by_index(2)
    helper.search_by_value("Read a book")
    del helper