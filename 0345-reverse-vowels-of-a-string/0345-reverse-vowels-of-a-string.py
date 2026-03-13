class Solution:
    def reverseVowels(self, s: str) -> str:
        list_s = list(s)
        vowels = []

        for i in range(len(s)):
            if list_s[i] in 'aeiouAEIOU':
                vowels.append(list_s[i])

        for i in range(len(s)):
            if list_s[i] in 'aeiouAEIOU':
                list_s[i] = vowels.pop()

        
        return ''.join(list_s)


        