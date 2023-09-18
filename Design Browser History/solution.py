class Node:
    def __init__(self, value: str, prev=None, next=None) -> None:
        self.value = value
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str) -> None:
        self.currentNode = Node(value=homepage)

    def visit(self, url: str) -> None:
        # Create a new node
        newNode = Node(value=url)
        # Update the current node's next pointer to point to the new node
        # and the new node's previous to the currentNode
        self.currentNode.next = newNode
        newNode.prev = self.currentNode
        # Update the current node
        self.currentNode = newNode
        
    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.currentNode.prev:
                return self.currentNode.value
            self.currentNode = self.currentNode.prev
        return self.currentNode.value

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.currentNode.next:
                return self.currentNode.value
            self.currentNode = self.currentNode.next
        return self.currentNode.value
    
# Testing
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
