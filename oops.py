

class StringClass:
    def __init__(self):
        self.str1 = input("enter the string: ")

    def length(self):
        return len(self.str1)

    def listOfCharacters(self):
        return list(self.str1)


class PairsPossible(StringClass):
    def __init__(self, str2):
        super().__init__()
        self.str2 = str2

    def pairsList(self):
        str_list = list(self.str2)
        pairs_list = []
        for i in range(len(str_list)):
            for j in range(len(str_list)):
                pairs_list.append([str_list[i], str_list[j]])
        return pairs_list

    def displayPairs(self):
        print("pairs of string:")
        self.l = self.pairsList()
        for pairs in self.l:
            print(pairs, end=" ")


s2 = input("enter string2: ")
pair = PairsPossible(s2)
s1 = pair.str1
print("length of string:", pair.length())
print("string to list: ", pair.listOfCharacters())
pairlist = pair.pairsList()
pair.displayPairs()