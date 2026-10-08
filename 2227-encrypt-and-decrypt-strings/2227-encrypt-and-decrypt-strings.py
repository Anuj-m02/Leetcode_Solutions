class Encrypter:

    def __init__(self, keys: list[str], values: list[str], dictionary: list[str]):

        self.enc_map = {k : v for k,v in zip(keys , values)}

        self.dict_counts = Counter()
        for word in dictionary :
            encrypted_word = self.encrypt(word)
            if encrypted_word :
                self.dict_counts[encrypted_word] += 1
        

    def encrypt(self, word1: str) -> str:
        res = []
        for char in word1 :
            if char not in self.enc_map :
                return ""
            
            res.append(self.enc_map[char])
        
        return "".join(res)

        

    def decrypt(self, word2: str) -> int:

        return self.dict_counts[word2]
        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)