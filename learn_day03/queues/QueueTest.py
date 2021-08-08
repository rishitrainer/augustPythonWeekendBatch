import queue

fifo = queue.Queue(10)
lifo = queue.LifoQueue()
simple = queue.SimpleQueue()
priority = queue.PriorityQueue()

for i in range(1,11):
    fifo.put("Message " + str(i))
    lifo.put("Message " + str(i))
    simple.put("Message " + str(i))
    priority.put("Message " + str(i))

# qsize
print(fifo.qsize())
print(lifo.qsize())
print(simple.qsize())
print(priority.qsize())

# get message
print(fifo.get())
print(lifo.get())
print(simple.get())
print(priority.get())

# qsize
print(fifo.qsize())
print(lifo.qsize())
print(simple.qsize())
print(priority.qsize())

fifo.put("Message 10")

if fifo.full():
    print("queue is full")
else:
    print("you can add more messages")
