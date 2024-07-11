class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        temp = self.contains(self.root, word)
        return temp is not None and temp.is_end_of_word

    def contains(self, node, word: str):
        if node is None:
            return None
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def traverse(self, node, word=""):
        if node.is_end_of_word:
            print(word)
        for key, value in node.children.items():
            self.traverse(value, word+key)

    def prefix_check(self, word: str):
        return self.contains(self.root, word) is not None

    def prefix_search(self, prefix: str):
        node = self.contains(self.root, prefix)
        if node is not None:
            self.traverse(node, prefix)
        else:
            print(f"No words found with prefix '{prefix}'")

    def print_trie(self, node=None, prefix=""):
        if node is None:
            node = self.root
        if node.is_end_of_word:
            print(prefix)
        for char, next_node in node.children.items():
            self.print_trie(next_node, prefix + char)


new = Trie()
movies = [
    "The Pursuit of Happyness",
    "Harry Potter",
    "Infinity war",
    "Star Wars",
    "Vettam",
    "Big B",
    "CID Moosa",
    "Batman",
    "chithram",
    "Life of Ram",
    "Interstellar",
]

for movie in movies:
    new.insert(movie)

# new.prefix_search("c")
new.print_trie()