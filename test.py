import ll
import dll
import stack
import queue
import dequeue
import rpn

# setup of all collections
ll = ll.ll()
dll = dll.dll()
stack = stack.stack()
queue = queue.queue()
dequeue = dequeue.dequeue()

# testing rpn
print(rpn.rpn(""))
print(rpn.rpn("3"))
print(rpn.rpn("3 3"))
print(rpn.rpn("3 3 *"))
print(rpn.rpn("3.25 3 *"))
print(rpn.rpn("1 2 * 3 + 4"))
print(rpn.rpn("10000000000000000 99 *"))

# testing ll
ll.add("testing, testing")
ll.remove("testing, testing")
ll.add("the thing")
ll.search("the thing")
