class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index = word.find(ch)
        # print(word , index)
        if index:
            txt = word[:index+1][::-1]
            word = txt + word[index+1:]
            return word
        
        else:
            return word


obj1=Solution()
print("dcbaefd",obj1.reversePrefix("abcdefd","d"))
print("zxyxxe",obj1.reversePrefix("xyxzxe","z"))
print("abcd",obj1.reversePrefix("abcd","z"))
# print("",obj1.reversePrefix("",""))
# print("",obj1.reversePrefix("",""))