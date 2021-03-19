from fundamentals.test_time import test_time


class Solution():
    def __init__(self):
        pass

    # @test_time
    def findLadders(self, beginWord, endWord, wordList):
        def build_graph(words):
            def tell_connect(wordi, wordj):
                diff = 0
                for char_i, char_j in zip(wordi, wordj):
                    if char_i != char_j:
                        diff += 1
                        if diff > 1:
                            return False
                if diff == 1:
                    return True

            graph = {wordi: set() for wordi in words}
            for i in range(len(words)):
                for j in range(i, len(words)):
                    if tell_connect(words[i], words[j]):
                        graph[words[i]].add(words[j])
                        graph[words[j]].add(words[i])
            return graph

        def dfs(start, end, graph):
            stack = [[start], ]
            solutions = []
            visited = {start}
            step = 0
            while stack:
                len_stack = len(stack)
                level_visited=set()
                for i in range(len_stack):
                    cur_path = stack.pop(0)
                    if cur_path[-1] == end:
                        solutions.append(cur_path)
                    for next_word in graph[cur_path[-1]]:
                        if next_word not in visited:
                            stack.append(cur_path + [next_word])
                            level_visited.add(next_word)
                if solutions:
                    return solutions
                visited=visited|level_visited
                step += 1
            return solutions

        if endWord not in wordList:
            return []
        graph = build_graph(wordList + [beginWord])

        solutions = dfs(beginWord, endWord, graph)
        return solutions

    def main(self):
        beginWord="aaaaaaaaaa"
        endWord="cccccccccc"
        wordList=["aaaaaaaaaa", "caaaaaaaaa", "cbaaaaaaaa", "daaaaaaaaa", "dbaaaaaaaa", "eaaaaaaaaa", "ebaaaaaaaa", "faaaaaaaaa",
         "fbaaaaaaaa", "gaaaaaaaaa", "gbaaaaaaaa", "haaaaaaaaa", "hbaaaaaaaa", "iaaaaaaaaa", "ibaaaaaaaa", "jaaaaaaaaa",
         "jbaaaaaaaa", "kaaaaaaaaa", "kbaaaaaaaa", "laaaaaaaaa", "lbaaaaaaaa", "maaaaaaaaa", "mbaaaaaaaa", "naaaaaaaaa",
         "nbaaaaaaaa", "oaaaaaaaaa", "obaaaaaaaa", "paaaaaaaaa", "pbaaaaaaaa", "qaaaaaaaaa", "qbaaaaaaaa", "raaaaaaaaa",
         "rbaaaaaaaa", "saaaaaaaaa", "sbaaaaaaaa", "taaaaaaaaa", "tbaaaaaaaa", "uaaaaaaaaa", "ubaaaaaaaa", "vaaaaaaaaa",
         "vbaaaaaaaa", "waaaaaaaaa", "wbaaaaaaaa", "xaaaaaaaaa", "xbaaaaaaaa", "yaaaaaaaaa", "ybaaaaaaaa", "zaaaaaaaaa",
         "zbaaaaaaaa", "bbaaaaaaaa", "bbcaaaaaaa", "bbcbaaaaaa", "bbdaaaaaaa", "bbdbaaaaaa", "bbeaaaaaaa", "bbebaaaaaa",
         "bbfaaaaaaa", "bbfbaaaaaa", "bbgaaaaaaa", "bbgbaaaaaa", "bbhaaaaaaa", "bbhbaaaaaa", "bbiaaaaaaa", "bbibaaaaaa",
         "bbjaaaaaaa", "bbjbaaaaaa", "bbkaaaaaaa", "bbkbaaaaaa", "bblaaaaaaa", "bblbaaaaaa", "bbmaaaaaaa", "bbmbaaaaaa",
         "bbnaaaaaaa", "bbnbaaaaaa", "bboaaaaaaa", "bbobaaaaaa", "bbpaaaaaaa", "bbpbaaaaaa", "bbqaaaaaaa", "bbqbaaaaaa",
         "bbraaaaaaa", "bbrbaaaaaa", "bbsaaaaaaa", "bbsbaaaaaa", "bbtaaaaaaa", "bbtbaaaaaa", "bbuaaaaaaa", "bbubaaaaaa",
         "bbvaaaaaaa", "bbvbaaaaaa", "bbwaaaaaaa", "bbwbaaaaaa", "bbxaaaaaaa", "bbxbaaaaaa", "bbyaaaaaaa", "bbybaaaaaa",
         "bbzaaaaaaa", "bbzbaaaaaa", "bbbbaaaaaa", "bbbbcaaaaa", "bbbbcbaaaa", "bbbbdaaaaa", "bbbbdbaaaa", "bbbbeaaaaa",
         "bbbbebaaaa", "bbbbfaaaaa", "bbbbfbaaaa", "bbbbgaaaaa", "bbbbgbaaaa", "bbbbhaaaaa", "bbbbhbaaaa", "bbbbiaaaaa",
         "bbbbibaaaa", "bbbbjaaaaa", "bbbbjbaaaa", "bbbbkaaaaa", "bbbbkbaaaa", "bbbblaaaaa", "bbbblbaaaa", "bbbbmaaaaa",
         "bbbbmbaaaa", "bbbbnaaaaa", "bbbbnbaaaa", "bbbboaaaaa", "bbbbobaaaa", "bbbbpaaaaa", "bbbbpbaaaa", "bbbbqaaaaa",
         "bbbbqbaaaa", "bbbbraaaaa", "bbbbrbaaaa", "bbbbsaaaaa", "bbbbsbaaaa", "bbbbtaaaaa", "bbbbtbaaaa", "bbbbuaaaaa",
         "bbbbubaaaa", "bbbbvaaaaa", "bbbbvbaaaa", "bbbbwaaaaa", "bbbbwbaaaa", "bbbbxaaaaa", "bbbbxbaaaa", "bbbbyaaaaa",
         "bbbbybaaaa", "bbbbzaaaaa", "bbbbzbaaaa", "bbbbbbaaaa", "bbbbbbcaaa", "bbbbbbcbaa", "bbbbbbdaaa", "bbbbbbdbaa",
         "bbbbbbeaaa", "bbbbbbebaa", "bbbbbbfaaa", "bbbbbbfbaa", "bbbbbbgaaa", "bbbbbbgbaa", "bbbbbbhaaa", "bbbbbbhbaa",
         "bbbbbbiaaa", "bbbbbbibaa", "bbbbbbjaaa", "bbbbbbjbaa", "bbbbbbkaaa", "bbbbbbkbaa", "bbbbbblaaa", "bbbbbblbaa",
         "bbbbbbmaaa", "bbbbbbmbaa", "bbbbbbnaaa", "bbbbbbnbaa", "bbbbbboaaa", "bbbbbbobaa", "bbbbbbpaaa", "bbbbbbpbaa",
         "bbbbbbqaaa", "bbbbbbqbaa", "bbbbbbraaa", "bbbbbbrbaa", "bbbbbbsaaa", "bbbbbbsbaa", "bbbbbbtaaa", "bbbbbbtbaa",
         "bbbbbbuaaa", "bbbbbbubaa", "bbbbbbvaaa", "bbbbbbvbaa", "bbbbbbwaaa", "bbbbbbwbaa", "bbbbbbxaaa", "bbbbbbxbaa",
         "bbbbbbyaaa", "bbbbbbybaa", "bbbbbbzaaa", "bbbbbbzbaa", "bbbbbbbbaa", "bbbbbbbbca", "bbbbbbbbcb", "bbbbbbbbda",
         "bbbbbbbbdb", "bbbbbbbbea", "bbbbbbbbeb", "bbbbbbbbfa", "bbbbbbbbfb", "bbbbbbbbga", "bbbbbbbbgb", "bbbbbbbbha",
         "bbbbbbbbhb", "bbbbbbbbia", "bbbbbbbbib", "bbbbbbbbja", "bbbbbbbbjb", "bbbbbbbbka", "bbbbbbbbkb", "bbbbbbbbla",
         "bbbbbbbblb", "bbbbbbbbma", "bbbbbbbbmb", "bbbbbbbbna", "bbbbbbbbnb", "bbbbbbbboa", "bbbbbbbbob", "bbbbbbbbpa",
         "bbbbbbbbpb", "bbbbbbbbqa", "bbbbbbbbqb", "bbbbbbbbra", "bbbbbbbbrb", "bbbbbbbbsa", "bbbbbbbbsb", "bbbbbbbbta",
         "bbbbbbbbtb", "bbbbbbbbua", "bbbbbbbbub", "bbbbbbbbva", "bbbbbbbbvb", "bbbbbbbbwa", "bbbbbbbbwb", "bbbbbbbbxa",
         "bbbbbbbbxb", "bbbbbbbbya", "bbbbbbbbyb", "bbbbbbbbza", "bbbbbbbbzb", "bbbbbbbbbb", "aaaaaaaaac", "aaaaaaaacc",
         "aaaaaaaccc", "aaaaaacccc", "aaaaaccccc", "aaaacccccc", "aaaccccccc", "aacccccccc", "accccccccc", "cccccccccc"]
        print(self.findLadders(beginWord, endWord, wordList))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
