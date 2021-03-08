class MagicList:
    def __init__(self):
        self.myList = dict()

    def __getitem__(self, key):
        if key in self.myList:
            return self.myList[key]

    def __setitem__(self, key, value):
        self.myList[key] = value

    def __str__(self):
        return str(list(self.myList.values()))




