class LNode(object):
    """Node of Linked list"""
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LinkedListUnderflow(ValueError):
    pass

class LList(object):
    """Single Linked List"""
    def __init__(self):
        self._head = None
    
    # O(1)
    def is_empty(self):
        return self._head is None

    # O(1)
    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    # O(1)
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next

        return e

    # O(n)
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    # O(n)
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p. next

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def reverse(self):
        if self._head is None:
            return
        p = self._head
        prev = None
        while p is not None:
            temp = p.next
            p.next = prev
            prev = p
            p = temp
        self._head = prev

    def clear(self):
        if self._head is None:
            return
        p = self._head
        while p is not None:
            temp = p.next
            del p.next
            p = temp
        self._head = None

if __name__ == '__main__':
    t = LList()
    for i in range(10):
        t.append(i)
    t.reverse()
    for i in t.elements():
        print(i)

