
# Knapsack Problem
Now that you saw the dynamic programming solution for the knapsack problem, it's time to implement it. Implement the function `max_value` to return the maximum value given the items (`items`) and the maximum weight of the knapsack (`knapsack_max_weight`). The `items` variable is the type `Item`, which is a [named tuple](https://docs.python.org/3/library/collections.html#collections.namedtuple).


```python
import collections

Item = collections.namedtuple('Item', ['weight', 'value'])


def max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    # row vector of weights
    lookup_table = [0] * (knapsack_max_weight + 1)
    print(lookup_table)
    for item in items:
        print('item: {}'.format(item))
        for capacity in reversed(range(knapsack_max_weight + 1)):
            print('w: {}'.format(capacity), end= ' ')
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)
            print(lookup_table)
    return lookup_table[-1] # return the last value (solution cost)



tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
assert tests[0]['correct_output'] == max_value(**tests[0]['input'])
# for test in tests:
#     assert test['correct_output'] == max_value(**test['input'])
```

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    item: Item(weight=10, value=7)
    w: 15 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7]
    w: 14 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7]
    w: 13 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7]
    w: 12 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7]
    w: 11 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7]
    w: 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7]
    w: 9 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7]
    w: 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7]
    w: 7 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7]
    w: 6 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7]
    w: 5 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7]
    w: 4 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7]
    w: 3 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7]
    w: 2 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7]
    w: 1 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7]
    w: 0 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7]
    item: Item(weight=9, value=8)
    w: 15 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 8]
    w: 14 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 8, 8]
    w: 13 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 8, 8, 8]
    w: 12 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 8, 8, 8, 8]
    w: 11 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 8, 8, 8, 8, 8]
    w: 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8]
    w: 9 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8]
    w: 8 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8]
    w: 7 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8]
    w: 6 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8]
    w: 5 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8]
    w: 4 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8]
    w: 3 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8]
    w: 2 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8]
    w: 1 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8]
    w: 0 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8]
    item: Item(weight=5, value=6)
    w: 15 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 14]
    w: 14 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 14, 14]
    w: 13 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 14, 14]
    w: 12 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 14, 14]
    w: 11 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 14, 14]
    w: 10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 14, 14]
    w: 9 [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 14, 14]
    w: 8 [0, 0, 0, 0, 0, 0, 0, 0, 6, 8, 8, 8, 8, 8, 14, 14]
    w: 7 [0, 0, 0, 0, 0, 0, 0, 6, 6, 8, 8, 8, 8, 8, 14, 14]
    w: 6 [0, 0, 0, 0, 0, 0, 6, 6, 6, 8, 8, 8, 8, 8, 14, 14]
    w: 5 [0, 0, 0, 0, 0, 6, 6, 6, 6, 8, 8, 8, 8, 8, 14, 14]
    w: 4 [0, 0, 0, 0, 0, 6, 6, 6, 6, 8, 8, 8, 8, 8, 14, 14]
    w: 3 [0, 0, 0, 0, 0, 6, 6, 6, 6, 8, 8, 8, 8, 8, 14, 14]
    w: 2 [0, 0, 0, 0, 0, 6, 6, 6, 6, 8, 8, 8, 8, 8, 14, 14]
    w: 1 [0, 0, 0, 0, 0, 6, 6, 6, 6, 8, 8, 8, 8, 8, 14, 14]
    w: 0 [0, 0, 0, 0, 0, 6, 6, 6, 6, 8, 8, 8, 8, 8, 14, 14]


<span class="graffiti-highlight graffiti-id_sczu399-id_vljhmf7"><i></i><button>Hide Solution</button></span>


```python
def max_value(knapsack_max_weight, items):
    # row vector of weights
    lookup_table = [0] * (knapsack_max_weight + 1)

    for item in items:
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]
```
