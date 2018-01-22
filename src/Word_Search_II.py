# coding: utf8
"""
---------------------------------------------
    File Name: Word_Search_II
    Description: 
    Author: wangdawei
    date:   2018/1/19
---------------------------------------------
    Change Activity: 
                    2018/1/19
---------------------------------------------    
"""

class TrieNode():
    def __init__(self):
        self.is_string = False
        self.leaves = {}

    def insert(self, word):
        cur_node = self
        for w in word:
            if w not in cur_node.leaves:
                cur_node.leaves[w] = TrieNode()
            cur_node = cur_node.leaves[w]
        cur_node.is_string = True


class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = TrieNode()
        for word in words:
            trie.insert(word)
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        result = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.findWordsRecu(board, trie, 0, i, j, visited, [], result)

        return list(result.keys())

    def findWordsRecu(self, board, trie, cur, i, j, visited, cur_word, result):
        # print(i, j)
        if not trie or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return

        if board[i][j] not in trie.leaves:
            return

        cur_word.append(board[i][j])
        next_node = trie.leaves[board[i][j]]
        if next_node.is_string:
            result["".join(cur_word)] = True
        visited[i][j] = True
        self.findWordsRecu(board, next_node, cur + 1, i + 1, j, visited, cur_word, result)
        self.findWordsRecu(board, next_node, cur + 1, i - 1, j, visited, cur_word, result)
        self.findWordsRecu(board, next_node, cur + 1, i, j + 1, visited, cur_word, result)
        self.findWordsRecu(board, next_node, cur + 1, i, j - 1, visited, cur_word, result)
        visited[i][j] = False
        cur_word.pop()
        pass



def main():
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    solu = Solution()
    print(solu.findWords(board, words))
    pass


if __name__ == "__main__":
    main()

