"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check string lengths since to be an anagram,
        # since both words need to have same no of characters
        if len(s) != len(t):
            return False
        
        # Create HashMap for no of occurences of each chaacter in both strings
        hashS = {}
        hashT = {}
        for i in range(len(s)):
            hashS[s[i]] = hashS.get(s[i], 0) + 1
            hashT[t[i]] = hashT.get(t[i], 0) + 1
        
        # Now Match all occurences, if any dissimilarity found, return False
        for key in hashS:
            if hashS[key] != hashT.get(key, 0):
                return False
        
        return True
