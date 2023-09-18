class TextEditor:

    def __init__(self):
        # Two stacks that are relative to the cursor, r is in reverse
        self.l, self.r = [], []

    def addText(self, text: str) -> None:
        self.l.extend(list(text))

    def deleteText(self, k: int) -> int:
        for _ in range((d := min(k, len(self.l)))):
            self.l.pop()
        return d

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.l))):
            self.r.append(self.l.pop())
        return ''.join(self.l[-10:])

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.r))):
            self.l.append(self.r.pop())
        return ''.join(self.l[-10:])