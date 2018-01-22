# coding: utf8
"""
---------------------------------------------
    File Name: Implement_Trie
    Description: 
    Author: wangdawei
    date:   2018/1/19
---------------------------------------------
    Change Activity: 
                    2018/1/19
---------------------------------------------    
"""


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.isWord = True

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        trieNode = self.trie
        for w in word:
            trieNode = trieNode.setdefault(w, {})
        trieNode[self.isWord] = self.isWord
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        trieNode = self.trie
        for w in word:
            if w in trieNode:
                trieNode = trieNode.get(w, {})
            else:
                return False
        if self.isWord in trieNode:
            return True
        else:
            return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        trieNode = self.trie
        for w in prefix:
            if w in trieNode:
                trieNode = trieNode.get(w, {})
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "book"
obj.insert(word)
param_2 = obj.search(word)
print(param_2)
prefix = "bo"
param_3 = obj.startsWith(prefix)
print(param_3)
prefix = "bok"
param_3 = obj.startsWith(prefix)
print(param_3)

