def wordChecker(word):
    
    x = open('ScrabbleWords2019.txt', 'r')
    word = word.upper()
    
    for value in x:
        word_ = value.split('\n')[0]
        if word == word_:
            return True
    
    return False

def wordScoreCalculator(word):
    
    if wordChecker(word) != True:
        return('Not a valid Scrabble Word!')
    
    else:
        word = word.upper()
        scores = {"A": 1, "B": 3, "C": 3, "E": 1, "D": 2, "G": 2,
         "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
         "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
         "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
         "X": 8, "Z": 10}
        
        return sum(scores[i] for i in word)

def wordFinder(letters = 'Excel'):
    
    x = open('ScrabbleWords2019.txt', 'r')
    letters = letters.upper()
    length = len(letters)
    answer = []
    
    for value in x:
        word = value.split('\n')[0]
        
        if len(word) > length:
            continue
        else:
            flag = 0
            
            for i in list(word):
                if (i not in letters) or (word.count(i) > letters.count(i)):
                    flag = 1
                    break
                
            if flag == 0:
                a = (word, wordScoreCalculator(word))
                answer.append(a)
    
    if ('', 0) in answer:
        answer.remove(('', 0))
    
    answer.sort(key = lambda x: x[1], reverse = True) 
    return answer


letters = input("Enter the letters: ")
for i in wordFinder(letters):
    print(i[0], i[1])    
