import typing
from typing import Optional, Dict
from collections.abc import Iterator

from py_boggle.boggle_dictionary import BoggleDictionary


class TrieNode:
    """
    Our TrieNode class. Feel free to add new properties/functions, but 
    DO NOT edit the names of the given properties (children and is_word).
    """
    def __init__(self):
        self.children : Dict[str, TrieNode] = {} # maps a child letter to its TrieNode class
        self.is_word = False # whether or not this Node is a valid word ending


class TrieDictionary(BoggleDictionary):
    """
    Your implementation of BoggleDictionary.
    Several functions have been filled in for you from our solution, but you are free to change their implementations.
    Do NOT change the name of self.root, as our autograder will manually traverse using self.root
    """

    def __init__(self):
        self.root : TrieNode = TrieNode()

    def load_dictionary(self, filename: str) -> None:
        # Remember to add every word to the trie, not just the words over some length.
        with open(filename) as wordsfile:
            for line in wordsfile:
                word = line.strip().lower()
                node = self.root
                for letter in word:
                    if letter not in node.children:
                        node.children[letter] = TrieNode()
                    node = node.children[letter]
                node.is_word = True
                # Do something with word here
        # raise NotImplementedError("method load_dictionary") # TODO: implement your code here

    def _insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_word = True

    def traverse(self, prefix: str) -> Optional[TrieNode]:
        """
        Traverse will traverse the Trie down a given path of letters `prefix`.
        If there is ever a missing child node, then returns None.
        Otherwise, returns the TrieNode referenced by `prefix`.
        """
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return None
            node = node.children[letter]
        return node

      #  raise NotImplementedError("method traverse") # TODO: implement your code here

    def is_prefix(self, prefix: str) -> bool:
        prefix = prefix.lower()
        return self.traverse(prefix) is not None
       # raise NotImplementedError("method is_prefix") # TODO: implement your code here

    def contains(self, word: str) -> bool:
        word = word.lower()
        node = self.traverse(word)
        return node.is_word if node else False

       # raise NotImplementedError("method contains") # TODO: implement your code here

    def __iter__(self) -> typing.Iterator[str]:
        words = []

        def dfs(node, current_word):
            if node.is_word:
                words.append(current_word)
            for letter, child_node in node.children.items():
                dfs(child_node, current_word + letter)

        dfs(self.root, "")
        return iter(words)

       # raise NotImplementedError("method __iter__") # TODO: implement your code here

