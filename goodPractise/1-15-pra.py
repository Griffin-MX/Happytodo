# 斐波那契
# a = 1
# b = 1
# print(a)
# print(b)
# for i in range(20):
#     c = a + b
#     print(c)
#     b = a
#     a = c


# 完美数
import math
import time

start = time.time()
for num in range(2, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if (factor > 1) and (num // factor) != factor:
                result += num // factor
    if result == num:
        print(num)
end = time.time()
print(f"运行耗时:{end-start}")

start = time.time()
for i in range(1, 10000):
    num = 0
    for k in range(1, i):
        if i % k == 0:
            num += k
    if i == num:
        print(i)
end = time.time()
print(f"运行耗时:{end-start}")
