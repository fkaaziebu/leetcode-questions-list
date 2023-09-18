class Node:
    def __init__(self, value: str, prev=None, next=None) -> None:
        self.value = value
        self.prev = prev
        self.next = next

class TextEditor:

    def __init__(self):
        self.cursor = Node("|")
        self.length = 0
        
    def moveCursor(self, direction, k):
        text_to_left_of_cursor = ""
        for i in range(k):
            if direction == "left":
                if self.cursor.prev and self.cursor.next:
                    self.cursor.prev.next = self.cursor.next
                    self.cursor.next.prev = self.cursor.prev
                    self.cursor.next = self.cursor.prev
                    self.cursor.prev = self.cursor.prev.prev if self.cursor.prev.prev else None
                    self.cursor.next.prev = self.cursor
                    if self.cursor.prev:
                        self.cursor.prev.next = self.cursor
                    self.length = self.length - 1

                if not self.cursor.next and self.cursor.prev:
                    self.cursor.prev.next = None
                    self.cursor.next = self.cursor.prev
                    self.cursor.prev = self.cursor.prev.prev if self.cursor.prev.prev else None
                    self.cursor.prev.next = self.cursor
                    self.cursor.next.prev = self.cursor
                    self.length = self.length - 1

                if not self.cursor.prev and self.cursor.next:
                    break

            elif direction == "right":
                if self.cursor.prev and self.cursor.next:
                    self.cursor.prev.next = self.cursor.next
                    self.cursor.next.prev = self.cursor.prev
                    self.cursor.prev = self.cursor.next
                    self.cursor.next = self.cursor.next.next if self.cursor.next.next else None
                    if self.cursor.next:
                        self.cursor.next.prev = self.cursor
                    self.cursor.prev.next = self.cursor
                    self.length += 1

                if not self.cursor.prev and self.cursor.next:
                    self.cursor.next.prev = None
                    self.cursor.prev = self.cursor.next
                    self.cursor.next = self.cursor.next.next if self.cursor.next.next else None
                    self.cursor.prev.next = self.cursor
                    self.length += 1

                if not self.cursor.next and self.cursor.prev:
                    break


        self.currentCharacter = self.cursor.prev
        for i in range(min(10, self.length)):
            if not self.currentCharacter:
                return text_to_left_of_cursor
            text_to_left_of_cursor =  self.currentCharacter.value + text_to_left_of_cursor
            self.currentCharacter = self.currentCharacter.prev
        
        return text_to_left_of_cursor

    def addText(self, text: str) -> None:
        for s in text:
            # Create new Node
            newNode = Node(s, next=self.cursor)
            if self.cursor.prev:
                self.cursor.prev.next = newNode
                newNode.prev = self.cursor.prev
            self.cursor.prev = newNode
            self.length += 1

        

    def deleteText(self, k: int) -> int:
        num_of_deleted_text = 0
        for i in range(k):
            if self.cursor.prev and self.cursor.prev.prev:
                self.cursor.prev.prev.next = self.cursor
                self.cursor.prev = self.cursor.prev.prev
                num_of_deleted_text += 1
                self.length = max(0, self.length - 1)
            elif self.cursor.prev:
                self.cursor.prev = None
                num_of_deleted_text += 1
                self.length = max(0, self.length - 1)
                break
        return num_of_deleted_text
    
        

    def cursorLeft(self, k: int) -> str:
        return self.moveCursor("left", k)
        

    def cursorRight(self, k: int) -> str:
        return self.moveCursor("right", k)


file = TextEditor()
print("Number of text to left after cursor moved 20 to left", file.cursorLeft(20))
file.addText("zmuwfndzyrusrsen")
file.addText("jvgaphkicrhxqb")
print("Number of text to left after cursor moved 12 to right", file.cursorRight(12))
file.addText("ptbdvcgaq")
print("Number of text to left after cursor moved 5 to right", file.cursorRight(5))
# print("Number of text deleted", file.deleteText(8))
# print(file.length)






# file.addText("leetcode")
# print("Number of text deleted", file.deleteText(4))
# file.addText("practice")
# print("Number of text to left after cursor moved 3 to right", file.cursorRight(3))
# print("Number of text to left after cursor moved 8 to left", file.cursorLeft(8))
# print("Number of text deleted", file.deleteText(10))
# print("Number of text to left after cursor moved 2 to left", file.cursorLeft(2))
# print("Number of text to left after cursor moved 6 to right", file.cursorRight(6))

