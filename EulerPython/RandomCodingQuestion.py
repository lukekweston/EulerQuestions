
map = { 2 : ["a", "b", "c"],
       3: ["d", "e", "f"],
       4: ["g", "h", "i"],
       5: ["j","k","l"],
       6: ["m", "n", "o"],
       7: ["p", "q", "r","s"],
       8: ["t","u","v"],
       9: ["w", "x", "y","z"]}


map2 = {"abc" : "2",
        "def": "3",
        "ghi": "4",
        "jkl": "5",
        "mno" : "6",
        "pqrs": "7",
        "tuv": "8",
        "wxyz": "9"}

def whatWeDo2(phoneNumber, words):

    goodwords = []

    for word in words:

        number = ""
        for i in word:
            for key in map2.keys():

                if(i in key):

                    number += map2.get(key)


        if(number in phoneNumber):

            goodwords.append(word)

    return goodwords


def whatWeDo(phoneNumber, words):
    goodWords = []
    for w in words:
        for i in range(len(phoneNumber) - len(w)):
            for j in range(len(w)):

                if(w[j] in map[int(phoneNumber[i + j])]):
                    if(j == len(w) -1):
                        goodWords.append(w)
                        break
    return goodWords

#


print(whatWeDo("3662277", ["foo", "bar", "baz", "foobar", "emo", "car", "cat"]))
print(whatWeDo2("3662277", ["foo", "bar", "baz", "foobar", "emo", "car", "cat"]))


print('a' in map[2])

