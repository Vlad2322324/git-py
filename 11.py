import random
import itertools


def randf(n):
    return [random.uniform(0, n) for h in range(n)]


def chained(a, b):
    return list(itertools.chain(a, b))


def responses_creator(item_ids):

    return [dict(item_id=item) for item in item_ids]



print(randf(2))
print(chained([1, 4], [4, 23]))
print(responses_creator([12, 21, 13]))
