class WordDictionary:

    def __init__(self):
        self.hm = {}
        

    def addWord(self, word: str) -> None:
        cur = self.hm
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["."] = True
        

    def search(self, word: str) -> bool:
        def recurseSearch(cur, string)-> bool:
           
            for i,c in enumerate(string):
                paths = [letter for letter in cur if letter != "."] if c == "." else []
               
                if not paths:
                    if c!="." and c in cur:
                        cur=cur[c]
                    else: return False
                else:
                    rest = string[i+1:]
                    for p in paths:
                        if recurseSearch(cur[p], rest):
                            return True
                    return False
           
            return "." in cur

        return recurseSearch(self.hm, word)

        
