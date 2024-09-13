'''
Write a program to simulate a queue using arrays
'''

class pyqueue:

    def __init__(self, capacity):
        self.queue    = []
        self.capacity = capacity


    def enqueue(self, item):
        if len(self.queue) == self.capacity:
            print('Queue is full...')
        else:
            self.queue.append(item)


    def dequeue(self):
        return self.queue.pop(0)


    def peek(self):
        return self.queue[0]
  

    def __repr__(self):
        return str(self.queue)


    def __len__(self):
        return len(self.queue)


# Driver Code
if __name__ == '__main__':
    q = pyqueue(3)
    print(q)

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q)

    q.enqueue(4)
    q.dequeue()
    print(q)
    q.enqueue(4)
    print(q)
