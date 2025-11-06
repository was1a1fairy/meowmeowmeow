class Sorted:

    def __init__(self, iterable, key, reverse=False):
        self.key = key
        self.reverse = reverse
        self.iterable = sorted(iterable, key=key, reverse=reverse)
        self.current = 0

    def __next__(self):
        if self.current >= len(self.iterable):
            raise StopIteration

        res = self.iterable[self.current]
        self.current += 1
        return res

    def __iter__(self):
        return self


it = Sorted([3, 1, 2], key=lambda x: x)
print(list(it)) # ожидаемо [1, 2, 3]

it = Sorted(["aaa", "bbbb", "c"], key=lambda s: len(s), reverse=True)
print(list(it)) # ожидаемо ["bbbb", "aaa", "c"]

class WordsEager:

    def __init__(self, str:str):
        self.str = str.split(" ")
        self.current = 0

    def __next__(self):
        if self.current >= len(self.str):
            raise StopIteration

        res = self.str[self.current]
        self.current += 1
        return res

    def __iter__(self):
        return self


it = WordsEager("a b c")
print(list(it)) # ['a', 'b', 'c']

class WordsLazy:

    def __init__(self, str:str):
        self.str = str.strip()
        self.current = 0

    def __next__(self):

        while self.current < len(self.str) and self.str[self.current] == " ":
            self.current += 1

        if self.current >= len(self.str):
            raise StopIteration

        start = self.current

        while self.current < len(self.str) and self.str[self.current] != " ":
            self.current += 1

        res = self.str[start:self.current]
        return res

    def __iter__(self):
        return self


it = WordsLazy("a b c")
print(list(it)) # ['a', 'b', 'c']


class Primes:

    def __init__(self, n):
        self.n = n
        self.current = 2
        self.count = 0

    def __iter__(self):
        return self

    def __is_divide(self, n):
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

    def __next__(self):
        while self.count != self.n:
            res = self.current
            self.current += 1
            if self.__is_divide(res):
                self.count += 1
                return res
        raise StopIteration


p = Primes(20) # 5 первых простых чисел
print(list(p)) # [2, 3, 5, 7, 11]


def chunked(iterable,size):
    if size > len(iterable):
        raise ValueError("size > iterable!!!")

    for i in range(0, len(iterable), size):
        res = iterable[i:i+size]
        yield tuple(res)


print(list(chunked(range(7), 3))) # [(0,1,2), (3,4,5), (6,)]


def words_generator(text):

    word = ""
    for i in text:
        if i != " ":
            word += i
        else:
            yield word
            word = ""


for w in words_generator(" hi there "):
    print(w)  # 'hi' затем 'there'


def primes_in_range(start, stop):

    flag = False
    for i in range(start, stop):
        for j in range(2,int(stop**0.5)+1):
            if i % j == 0:
                flag = False
                break
            else:
                flag = True
        if flag:
            yield i

print(list(primes_in_range(10, 30)))  # [11, 13, 17, 19, 23, 29]