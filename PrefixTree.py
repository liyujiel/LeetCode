class TrieNode():
    def __init__(self,key):
        self.word = False
        self.key = key
        self.children = {}

class Trie(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)
        
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for pos in prefix:
            if pos not in node.children:
                return False
            node = node.children[pos]
        return True