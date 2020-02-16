stack = [3,4,5]
stack.append(8)
print(stack)
stack.pop()
print(stack)
l = [1, 2, 2, 3, 4, 5, 6]
l2 = []
nl = []
for i in range(len(l)-1):
    if l[i] % 2 == 0:
        nl.append(l[i])
nl.pop()
nl.pop()
print(nl)
from collections import deque
ll = deque(["sachu", "newbie", "arpit"])
ll.append("hi")
print(ll)
a = ll.popleft()
ll.popleft()
print(ll)
x = ll.append("sachi")
print(x)


lws = [2, 3, 4, 5, 6]
lws.pop()
lws.pop()
print(lws)


lp = deque([1, 2, 3, 4, 5])
lp.popleft()
print(lp)
lp.appendleft(2)
print(lp)
lp.append(3)
b = (hex(id(lp[-1])))
print(b)
b_l = []
for i in b:
    b_l.append(i)
print(len(b_l))

