import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item} | Queue: {self.items}")

    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued {removed} | Queue: {self.items}")
            return removed
        else:
            print("Queue is empty. Nothing to dequeue.")
            return None

    def peek(self):
        if not self.is_empty():
            print(f"Front of queue: {self.items[0]}")
            return self.items[0]
        else:
            print("Queue is empty. No front item.")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        if not self.is_empty():
            winner = random.choice(self.items)
            self.items.remove(winner)
            for i in self.items:
                self.dequeue()
            print(winner)
            print(self.items)
            return winner

if __name__ == "__main__":
    q = Queue()
    q.enqueue("Order #1")
    q.enqueue("Order #2")
    q.enqueue("Order #3")
    q.select_and_announce_winner()