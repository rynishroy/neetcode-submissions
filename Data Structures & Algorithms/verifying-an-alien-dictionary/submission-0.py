class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        #first get the index and store it in map
        #word2 index should be greater than word1 index
        #if the word 1 still there and word2 end return false

        indexOrdering = {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]

            for j in range(len(word1)):

                if j == len(word2):
                    return False
                
                if word1[j] != word2[j]:
                    if indexOrdering[word2[j]]< indexOrdering[word1[j]]:
                        return False
                    break
        return True
                

        