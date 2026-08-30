class TextEditor:

    def __init__(self):

        self.left = []
        self.right = []

        # self.stack = []
        # self.cursor = 0
        # self.length = 0

    def addText(self, text: str) -> None:
        
        for letters in text :
            self.left.append(letters)
            # self.cursor += 1
            # self.length += 1


    def deleteText(self, k: int) -> int:
        cnt = 0
        while self.left and cnt < k :
            self.left.pop()
            cnt += 1
        
        return cnt


    def cursorLeft(self, k: int) -> str:

        while self.left and k > 0 :
            self.right.append(self.left.pop())
            k -= 1
        
        return "".join(self.left[-10 : ])



    def cursorRight(self, k: int) -> str:

        while self.right and k > 0 :
            self.left.append(self.right.pop())
            k -= 1
        
        return "".join(self.left[-10:])
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)