class BrowserHistory:
    def __init__(self, homepage: str) -> None:
        self.l, self.r = [], []
        self.l.append(homepage)

    def visit(self, url: str) -> None:
        self.l.append(url)
        self.r.clear()
        
    def back(self, steps: int) -> str:
        length = len(self.l)
        for i in range(min(steps, length - 1)):
            self.r.append(self.l.pop()) 
        return self.l[-1]

    def forward(self, steps: int) -> str:
        length = len(self.r)
        for i in range(min(steps, length)):
            self.l.append(self.r.pop())
        return self.l[-1]

tab = BrowserHistory("leetcode.com")
tab.visit("google.com")
tab.visit("facebook.com")
tab.visit("youtube.com")
print(tab.back(1))
print(tab.back(1))
print(tab.forward(1))
tab.visit("linkedin.com")
print(tab.forward(2))
print(tab.back(2))
print(tab.back(7))