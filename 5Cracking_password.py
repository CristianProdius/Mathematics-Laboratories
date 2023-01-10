def vigenere(x, key):
    lst_final = []
    code = list(x)
    j = 0
    for i, char in enumerate(code):
        if char.isalpha():
            code[i] = key[(i + j) % len(key)]
            lst_final.append((ord(x[i]) - ord(code[i])) % 26)
        else:
            lst_final.append(ord(char))
            j -= 1
    for i, char in enumerate(code):
        if char.isalpha():
            lst_final[i] = chr(lst_final[i] + 65)
        else:
            lst_final[i] = chr(lst_final[i])
    return ''.join(lst_final)

phrase = "OOGNVMTNTCLUOGZSZSHTXAZGMOMEPKWDDQM"
possibleKeys = []
with open("English_Dictionary.txt", "r", encoding="utf-8") as dictionary:
    for word in dictionary:
        possibleKeys.append(word.strip("\n"))
i = 1
possibleAnswers = {}
answerToPossibleNr = {}
for x in possibleKeys:
    print("Trying the: ", i, "key")
    i += 1
    value = 0
    decrypted = vigenere(phrase, x).replace("\n", "")
    for j in possibleKeys:
        if j in decrypted:
            value += len(j)
    possibleAnswers[x + " / " + decrypted] = value
possibleAnswers = dict(sorted(possibleAnswers.items(), key=lambda item: item[1], reverse=True))
with open("result.txt", "w", encoding="utf-8") as file:
    for x in possibleAnswers:
        file.write(x + " " + str(possibleAnswers[x]) + "\n")