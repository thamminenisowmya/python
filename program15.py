class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
    def is_empty(self):
        return len(self.stack) == 0
def reverse(sentence):
        words = sentence.split()
        stack = Stack()
        for word in words:
             stack.push(word)
        reversed_sentence = ""
        while not stack.is_empty():
             reversed_sentence += stack.pop() + ""
        return reversed_sentence.strip()
# Read input
T = int(input())
test_case = [input() for _ in range(T)]
# Reverse and print sentences
for sentence in test_case:
        reversed_sentence = reverse(sentence)
        print(reversed_sentence)
        