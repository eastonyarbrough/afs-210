# Stack Class
class Stack:
    def __init__(self):
        self.letters = []

    def isEmpty(self):
        return self.letters == []

    def push(self, letter):
        self.letters.append(letter)

    def pop(self):
        return self.letters.pop()

    def peek(self):
        return self.letters[len(self.letters) - 1]

    def size(self):
        return len(self.letters)

# Queue Class
class Queue:
    def __init__(self):
        self.letters = []

    def isEmpty(self):
        return self.letters == []

    def enqueue(self, letter):
        self.letters.insert(0, letter)

    def dequeue(self):
        self.letters.pop()

    def peek(self):
        return self.letters[len(self.letters) - 1]

    def size(self):
        return len(self.letters)

# isPalindrome function
def isPalindrome(word):
    # Initialize both classes
    stackWord = Stack()
    queueWord = Queue()
    # For loop through the word and push letters into Stack
    for char in word.lower():
        stackWord.push(char)
    # For loop through the word and enqueue letters into the Queue
    for char in word.lower():
        queueWord.enqueue(char)
    # Compare Stack and Queue to determine if palindrome
    if stackWord.letters == queueWord.letters:
        return True
    else:
        return False

print(isPalindrome('racecar'))
print(isPalindrome('noon'))
print(isPalindrome('python'))
print(isPalindrome('madam'))
