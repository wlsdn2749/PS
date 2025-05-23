import collections

class Trie:
    def __init__(self):
        self.root = collections.defaultdict()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current["_end"] = True  # 단어의 끝을 표시

    # def search(self, word: str) -> bool:
    #     current = self.root
    #     for letter in word:
    #         if letter not in current:
    #             return False
    #         current = current[letter]
    #     return "_end" in current

    # def startsWith(self, prefix: str) -> bool:
    #     current = self.root
    #     for letter in prefix:
    #         if letter not in current:
    #             return False
    #         current = current[letter]
    #     return True
    
    def display(self) -> None:
        """
        Trie 구조를 보기 좋게 출력
        """
        def pretty_print(node, level=0):
            for key, child in node.items():
                print("  " * level + f"- {key}")
                if isinstance(child, dict):
                    pretty_print(child, level + 1)

        print("Trie Structure:")
        pretty_print(self.root)


def findWords(board, words):
    def dfs(node, x, y, path):
        char = board[x][y]
        if char == '#' or char not in node:
            return

        next_node = node[char]
        path += char

        if "_end" in next_node:
            result.add(path)  # 단어를 결과에 추가

        # 현재 셀 방문 처리
        board[x][y] = '#'

        # 상하좌우 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                dfs(next_node, nx, ny, path)

        # 방문 표시 해제
        board[x][y] = char

    # Step 1: Trie에 단어 삽입
    trie = Trie()
    for word in words:
        trie.insert(word)

    trie.display()
    # Step 2: DFS 탐색
    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(trie.root, i, j, "")

    return list(result)

# Example Usage
board = [["o", "a", "a", "n"],
         ["e", "t", "a", "e"],
         ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]]
words = ["oak", "tree", "oaks", "cat", "cats"]



"""
- o
    - a
        - k
            - _end
            - s
                - _end

- t
    - r
        - e
            - e
                _ end
            
- c
    - a
        - t
            - _end
            - s
                - _end
        
"""
print(findWords(board, words))  # Output: ['eat', 'oath']