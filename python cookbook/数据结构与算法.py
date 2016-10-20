一.数据结构与算法
1.解压序列赋值给多个变量
    data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
    name, shares, price, (year, mon, day) = data
    # Use placeholder to drop item
    data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
    _, shares, price, _ = data

2.解压可迭代对象赋值给多个变量
    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    # 值得注意的是上面解压出的 phone_numbers 变量永远都是列表类型，不管解压的电话号码数量是多少(包括0个)
    name, email, *phone_numbers = record 

    # 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割
    >>> line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    >>> uname, *fields, homedir, sh = line.split(':')
    >>> uname
    'nobody'
    >>> homedir
    '/var/empty'
    >>> sh
    '/usr/bin/false'
    >>>

3.保留最后N个元素
    from collections import deque

    def search(lines, pattern, history=5):
        previous_lines = deque(maxlen=history)
        for li in lines:
            if pattern in li:
                yield li, previous_lines
            previous_lines.append(li)

    # Example use on a file
    if __name__ == '__main__':
        with open(r'../../cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
    # 使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。
    >>> q = deque(maxlen=3)
    >>> q.append(1)
    >>> q.append(2)
    >>> q.append(3)
    >>> q
    deque([1, 2, 3], maxlen=3)
    >>> q.append(4)
    >>> q
    deque([2, 3, 4], maxlen=3)
    >>> q.append(5)
    >>> q
    deque([3, 4, 5], maxlen=3)
    # 在队列两端插入或删除元素时间复杂度都是 O(1) ，而在列表的开头插入或删除元素的时间复杂度为 O(N) 
    >>> q = deque()
    >>> q.append(1)
    >>> q.append(2)
    >>> q.append(3)
    >>> q
    deque([1, 2, 3])
    >>> q.appendleft(4)
    >>> q
    deque([4, 1, 2, 3])
    >>> q.pop()
    3 
    >>> q
    deque([4, 1, 2])
    >>> q.popleft()
    4
    
4.查找最大或最小的N个元素
    import heapq
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
    print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
    portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    # 用堆排序来实现排序
    >>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    >>> import heapq
    >>> heapq.heapify(nums)
    >>> nums
    [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
    >>> heapq.heappop(nums)
    -4
    >>> heapq.heappop(nums)
    1 
    >>> heapq.heappop(nums)
    2

5.实现一个优先级队列
    import heapq

    class PriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0

        def push(self, item, priority):
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1

        def pop(self):
            return heapq.heappop(self._queue)[-1]
    >>> class Item:
    ... def __init__(self, name):
    ... self.name = name
    ... def __repr__(self):
    ... return 'Item({!r})'.format(self.name)
    ...
    >>> q = PriorityQueue()
    >>> q.push(Item('foo'), 1)
    >>> q.push(Item('bar'), 5)
    >>> q.push(Item('spam'), 4)
    >>> q.push(Item('grok'), 1)
    >>> q.pop()
    Item('bar')
    >>> q.pop()
    Item('spam')
    >>> q.pop()
    Item('foo')
    >>> q.pop()
    Item('grok')
    >>>
    
    函数 heapq.heappush() 和 heapq.heappop()分别在队列 _queue 上插入和删除第一个元素

6.字典中的键映射多个值
    # value = list()
    d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
    }
    # value = set()
    e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
    }
    # defaultdict
    from collections import defaultdict
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)
    # setdefault()
    d = {} # A regular dictionary
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)

7.字典排序
    # 一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着一个双向链表
    from collections import OrderedDict

8.字典的运算
    prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
    min_price = min(zip(prices.values(), prices.keys()))
    # min_price is (10.75, 'FB')
    max_price = max(zip(prices.values(), prices.keys()))
    # max_price is (612.78, 'AAPL')
    prices_sorted = sorted(zip(prices.values(), prices.keys()))

9.查找两个字典的相同点
    a = {'x':1, 'y':2, 'z':3}
    b = {'w':10, 'x':11, 'y':2}
    # Find keys in common
    a.keys() & b.keys() # { 'x', 'y' }
    # Find keys in a that are not in b
    a.keys() - b.keys() # { 'z' }
    # Find (key,value) pairs in common
    a.items() & b.items() # { ('y', 2) }

10.删除序列相同元素并保持顺序
    # All item are hashable
    def dedupe(items):
        seen = set()
        for item in items:
            if item not in seen:
                yield item
                seen.add(item)
    # Not all item are hashable
    def dedupe(items, key=None):
        seen = set()
        for item in items:
            val = item if key is None else key(item)
            if val not in seen:
                yield item
                seen.add(val)
    # file 
    with open(somefile,'r') as f:
    for line in dedupe(f):
    # better???
    def dedupe(items, key=None):
        t = list()
        for item in itmes:
            val = item if key is None else key(item)
            if val not in t:
                t.append(t)
        return t
        
11.命名切片
    # 切片
    >>> items = [0, 1, 2, 3, 4, 5, 6]
    >>> a = slice(2, 4)
    >>> items[2:4]
    [2, 3]
    >>> items[a]
    [2, 3]
    >>> items[a] = [10,11]
    >>> items
    [0, 1, 10, 11, 4, 5, 6]
    >>> del items[a]
    >>> items
    [0, 1, 4, 5, 6]
    # (start、stop、step)
    >>> s = slice(5, 50, 2)
    >>> s.start
    5 
    >>> s.stop
    50
    >>> s.step
    2 
    # avoid index error
    >>> s = 'HelloWorld'
    >>> a.indices(len(s))
    (5, 10, 2)
    >>> for i in range(*a.indices(len(s))):
    ... print(s[i])
    ...
    W
    r
    d 
    >>>
    
12.序列中出现次数最多的元素
    words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under']
    from collections import Counter
    word_counts = Counter(words)
    # 出现频率最高的3个单词
    top_three = word_counts.most_common(3)
    print(top_three)
    # Outputs [('eyes', 8), ('the', 5), ('look', 4)]
    >>> word_counts['not']
    1 >
    >> word_counts['eyes']
    8
    >>> morewords = ['why','are','you','not','looking','in','my','eyes']
    >>> word_counts.update(morewords)
    Counter()对象之间还可以和数学运算操作

13.通过某个关键字排序一个字典列表
    from operator import itemgetter
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))

14.排序不支持原生比较的对象
    class User:
        def __init__(self, user_id):
            self.user_id = user_id
        def __repr__(self):
            return 'User({})'.format(self.user_id)
    # Use lambda as key
    def sort_notcompare():
        users = [User(23), User(3), User(99)]
        print(users)
        print(sorted(users, key=lambda u: u.user_id))

    # Use operator.attrgetter()
    >>> from operator import attrgetter
    >>> sorted(users, key=attrgetter('user_id'))
    [User(3), User(23), User(99)]

    # In the min, max function
    min(users, key=attrgetter('user_id'))
    max(users, key=attrgetter('user_id'))

    # compared in the tuple
    by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
    
15.通过某个字段将记录分组
    # groupby()函数扫描整个序列并查找连续相同的值
    from operator import itemgetter
    from itertools import groupby
    # Sort by the desired field first
    rows.sort(key=itemgetter('date'))
    # Iterate in groups
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)
    # Use the defaultdict
    from collections import defaultdict
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)

16.过滤序列元素
    [n for n in mylist if n > 0] # 占内存
    (n for n in mylist if n > 0) # 不占内存

    # Use the filter() function
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
    ivals = list(filter(is_int, values))

    # Use itertools.compress()
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK'
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
        ]sss
    counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
    >>> from itertools import compress
    >>> more5 = [n > 5 for n in counts]
    >>> more5
    [False, False, True, False, False, True, True, False]
    >>> list(compress(addresses, more5))
    ['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']
    >>>

17.从字典中提取子集
    prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
    } #
    Make a dictionary of all prices over 200
    p1 = {key: value for key, value in prices.items() if value > 200}
    # Make a dictionary of tech stocks
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}
    

18.映射名称到序列元素
    >>> from collections import namedtuple
    >>> Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    >>> sub = Subscriber('jonesy@example.com', '2012-10-19')
    >>> sub
    Subscriber(addr='jonesy@example.com', joined='2012-10-19')
    >>> sub.addr
    'jonesy@example.com'
    >>> sub.joined
    '2012-10-19'
    
19.转换并同时计算数据
    # Determine if any .py files exist in a directory
    import os
    files = os.listdir('dirname')
    if any(name.endswith('.py') for name in files):
        print('There be python!')
    else:
        print('Sorry, no python.')

    # Output a tuple as CSV
    s = ('ACME', 50, 123.45)
    print(','.join(str(x) for x in s))

    # Sum data
    s = sum(x * x for x in nums) # The better and fast way
    s = sum([x * x for x in nums]) # Waste memery

    # Original: Returns 20
    min_shares = min(s['shares'] for s in portfolio)
    # Alternative: Returns {'name': 'AOL', 'shares': 20}
    min_shares = min(portfolio, key=lambda s: s['shares'])

20.合并多个字典或映射
    a = {'x': 1, 'z': 3 }
    b = {'y': 2, 'z': 4 }
    from collections import ChainMap
    c = ChainMap(a,b)
    # ChainMap 类只是在内部创建了一个容纳这些字典的列表 并重新定义了一些常见的字典操作来遍历这个列表
    >>> len(c)
    3 
    >>> list(c.keys())
    ['x', 'y', 'z']
    >>> list(c.values())
    [1, 2, 3]
    # 对于字典的更新或删除操作总是影响的是列表中第一个字典
    >>> c['z'] = 10
    >>> c['w'] = 40
    >>> del c['x']
    >>> a
    {'w': 40, 'z': 10}
    >>> del c['y']
    Traceback (most recent call last):
    ...
    KeyError: "Key not found in the first mapping: 'y'"
    # ChainMap 对于编程语言中的作用范围变量(比如 globals , locals 等)是非常有用的。 事实上  
    >>> values = ChainMap()
    >>> values['x'] = 1
    >>> # Add a new mapping
    >>> values = values.new_child()
    >>> values['x'] = 2
    >>> # Add a new mapping
    >>> values = values.new_child()
    >>> values['x'] = 3
    >>> values
    ChainMap({'x': 3}, {'x': 2}, {'x': 1})
    >>> values['x']
    3 >
    >> # Discard last mapping
    >>> values = values.parents
    >>> values['x']
    2 >
    >> # Discard last mapping
    >>> values = values.parents
    >>> values['x']
    1 >
    >> values
    ChainMap({'x': 1})
    # 作为 ChainMap 的替代，你可能会考虑使用 update() 方法将两个字典合并
    >>> a = {'x': 1, 'z': 3 }
    >>> b = {'y': 2, 'z': 4 }
    >>> merged = dict(b)
    >>> merged.update(a)