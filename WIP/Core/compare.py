class Compare:
    def __init__(self):
        self.alphabet = "._-0123456789aábcdeéfghiíjklmnñoópqrstuúvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def compareGreaterLength(self, str1, str2):
        g = len(str1)

        if(len(str2) > g):
            g = len(str2)

        return g

    def compareLesserLength(self, str1, str2):
        l = len(str1)

        if(len(str2) < l):
            l = len(str2)

        return l

    def compare(self, str1, str2):
        str1 = str1.strip()
        str2 = str2.strip()

        lesser = self.compareLesserLength(str1, str2)

        for i in range (lesser):
            if(self.alphabet.index(str1[i]) > self.alphabet.index(str2[i])):
                return 1
            
            elif(self.alphabet.index(str1[i]) < self.alphabet.index(str2[i])):
                return -1

        if(lesser == self.compareGreaterLength(str1, str2)):
            return 0

        elif(len(str1) == len(str2)):
            return -1

        else:
            return 1


compare = Compare()