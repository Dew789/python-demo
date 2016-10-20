1.使用多个界定符分割字符串
    # 使用正则表达式的分割方法
    >>> line = 'asdf fjdk; afed, fjek,asdf, foo'
    >>> import re
    >>> re.split(r'[;,\s]\s*', line)
    ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
    >>> fields = re.split(r'(;|,|\s)\s*', line)
    >>> fields
    ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
    >>>

2.字符串开头或结尾匹配
    >>> import os
    >>> filenames = os.listdir('.')
    >>> filenames
    [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
    >>> [name for name in filenames if name.endswith(('.c', '.h')) ]
    ['foo.c', 'spam.c', 'spam.h'
    >>> any(name.endswith('.py') for name in filenames)
    True

3.用Shell通配符匹配字符串
    # fnmatch根据操作系统的大小写敏感规则, fnmatchcase强制大小写敏感
    '''
    fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。 如果在数据处
    理操作中只需要简单的通配符就能完成的时候，这通常是一个比较合理的方案
    '''
    >>> from fnmatch import fnmatch, fnmatchcase
    >>> fnmatch('foo.txt', '*.txt')
    True
    >>> fnmatch('foo.txt', '?oo.txt')
    True
    >>> fnmatch('Dat45.csv', 'Dat[0-9]*')
    True
    >>> names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    >>> [name for name in names if fnmatch(name, 'Dat*.csv')]
    ['Dat1.csv', 'Dat2.csv']

4.字符串匹配与搜索
    re.finditer()
    str.find()
    str.endswith()
    str.startswith()
    '''
    如果你打算做大量的匹配和搜索操作的话，最好先编译正则表达式，
    然后再重复使用它。 模块级别的函数会将最近编译过的模式缓存起来，因此并不会消耗
    太多的性能，但是如果使用预编译模式的话，你将会减少查找和一些额外的处理损耗
    '''

5.字符串搜索和替换
    str.replace()
    re.sub()
    >>> text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    >>> import re
    >>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    'Today is 2012-11-27. PyCon starts 2013-3-13.'
    >>>