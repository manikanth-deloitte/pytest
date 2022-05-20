from collections import Counter

"""----------List-------------------"""


# count duplicates in list
def duplicateCount(arr):
    for ele in arr:
        dic = Counter(ele)
        for key in dic:
            if dic[key] > 1:
                print(key, "->", dic[key])


l = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 4]]
print("Return all the duplicate values from list of arraylist")
duplicateCount(l)
print()

# Merge two lists
print("Merge two lists")
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
output_list = []
for i in range(len(list2)):
    for j in range(len(list1)):
        s = list1[i] + list2[j]
        output_list.append(s)
print(output_list)
print()

# extend by adding subList
print("extending by adding subList")
nested_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
nested_list[2][1][2].extend(sub_list)
print([nested_list])

"""--------Dictionary-----------"""
# map the following list into dictionary
print("map the lists into dictionary")
Keys = ["Ten", "Twenty", "Thirty"]
Value = [10, 20, 30]
Dic = {}
for i in range(len(Keys)):
    Dic[Keys[i]] = Value[i]
print(Dic)
Dic_zip = dict(zip(Keys,Value))
print("merging lists using zip:\n", Dic_zip)
print()


# merge two dictionaries
print("merging two dictionaries")
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
res = dict1 | dict2
print(res)
# using update method
dict1.update(dict2)
print(dict1)
print()

# Rename key city to location in the following dictionary
print("Rename key city to location in the given dictionary")
sampleDict = {
  "name": "Kelly",
  "age": 25,
  "salary": 8000,
  "city": "New york"
}
# sampleDict["location"]=sampleDict["city"]
# del sampleDict["city"]
sampleDict["location"] = sampleDict.pop("city")
print(sampleDict)
print()


# Convert Dictionary to list
print("convert Dictionary to list")
Dict = {"HuEx": [1, 3, 4],
        "is": [7, 6],
        "best": [4, 5]
        }
res_list = []
for key in Dict:
    temp_list = []
    temp_list.append(key)
    for i in Dict[key]:
        temp_list.append(i)
    res_list.append(temp_list)
print(res_list)


