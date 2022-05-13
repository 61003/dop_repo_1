from time import time


def random(start, stop):
    rand = int(time() * 10 ** 7) % 10 ** 5
    cnt = start - 1
    while 1:
        cnt += 1
        if cnt > stop:
            cnt = start - 1
        rand -= 1
        if rand < 0:
            return cnt


beg = 1
end = 10
dict = {}
for num in range(beg, end):
    dict[f'elem_{num}'] = random(beg, end)
print(dict)
