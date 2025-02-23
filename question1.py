class Utility:
    def isPalindrome(ctx : str):
        reversed = ctx [::-1] 

        if reversed == ctx:
            return True
    
    def getInput():
        n = int(input())
        words = []

        for x in range(n):
            words.append(str(input()))

        return n, words
    
    def findPalindrome(word : str): 

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for position in range(len(word) + 1):
           # print(word[:position] + "X" + word[position:])
           for letter in alphabet:
               word_checkable = word[:position] + letter + word[position:]
               if Utility.isPalindrome(word_checkable):
                   print(word_checkable)
                   return
               
        print("NONE")
        

def Solution():
    _in = Utility.getInput()

    n = _in[0]
    words = _in[1]

    for word in words:
        if Utility.isPalindrome(word):
            print(word)
        else:
            Utility.findPalindrome(word)


Solution()