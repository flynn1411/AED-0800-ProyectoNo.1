class Compare:
    def __init__(self):
        self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def compareGreaterLength(self, str1, str2):
        greater = len(str1)

        if(len(str2) > greater):
            greater = len(str2)

        return greater

    def compareLesserLength(self, str1, str2):
        lesser = len(str1)

        if(len(str2) < lesser):
            lesser = len(str2)

        return lesser

    def compare(self, str1, str2):
        str1 = str1.strip()
        str2 = str2.strip()