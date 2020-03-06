
# Bubble Sort Exercises
Now that you know how about bubble sort works, you'll implement bubble sort for two exercises.

## Exercise 1

Sam records when they wake up every morning. Assuming Sam always wakes up in the same hour, use bubble sort to sort by earliest to latest.




```python
wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
def bubble_sort_1(l):
    # TODO: Implement bubble sort solution
    pass

bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")
```

<span class="graffiti-highlight graffiti-id_y26wn0b-id_uppmlq4"><i></i><button>Hide Solution</button></span>


```python
def bubble_sort_1(l):
    iter = 0
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]
            # skip this iteration and compare the prev to the successive element
            if prev <= this:
                continue

            l[index] = prev
            l[index - 1] = this

wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")
```

    Pass


## Exercise 2

Sam doesn't always go to sleep in the same hour. Given the following times Sam has gone to sleep, sort the times from latest to earliest.


```python
# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(l):
    # TODO: Implement bubble sort solution
    pass

bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")
```

    Fail


<span class="graffiti-highlight graffiti-id_f6s1i29-id_hxr8nmt"><i></i><button>Hide Solution</button></span>


```python
def bubble_sort_2(l):
    iter = 0
    for iteration in range(len(l)):
        print('outerloop')
        for index in range(1, len(l)):
            this_hour, this_min = l[index]
            prev_hour, prev_min = l[index - 1]
            iter += 1
            print('iteration: {} {} ({},{}) ({},{})'.format(iter,l,prev_hour,prev_min,this_hour, this_min))
            if prev_hour > this_hour or (prev_hour == this_hour and prev_min > this_min):
                continue

            l[index] = (prev_hour, prev_min)
            l[index - 1] = (this_hour, this_min)

# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]
bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")
print('number of iteration: 7*6 = {}'.format(7*6))
```

    outerloop
    iteration: 1 [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)] (24,13) (21,55)
    iteration: 2 [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)] (21,55) (23,20)
    iteration: 3 [(24, 13), (23, 20), (21, 55), (22, 5), (24, 23), (21, 58), (24, 3)] (21,55) (22,5)
    iteration: 4 [(24, 13), (23, 20), (22, 5), (21, 55), (24, 23), (21, 58), (24, 3)] (21,55) (24,23)
    iteration: 5 [(24, 13), (23, 20), (22, 5), (24, 23), (21, 55), (21, 58), (24, 3)] (21,55) (21,58)
    iteration: 6 [(24, 13), (23, 20), (22, 5), (24, 23), (21, 58), (21, 55), (24, 3)] (21,55) (24,3)
    outerloop
    iteration: 7 [(24, 13), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3), (21, 55)] (24,13) (23,20)
    iteration: 8 [(24, 13), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3), (21, 55)] (23,20) (22,5)
    iteration: 9 [(24, 13), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3), (21, 55)] (22,5) (24,23)
    iteration: 10 [(24, 13), (23, 20), (24, 23), (22, 5), (21, 58), (24, 3), (21, 55)] (22,5) (21,58)
    iteration: 11 [(24, 13), (23, 20), (24, 23), (22, 5), (21, 58), (24, 3), (21, 55)] (21,58) (24,3)
    iteration: 12 [(24, 13), (23, 20), (24, 23), (22, 5), (24, 3), (21, 58), (21, 55)] (21,58) (21,55)
    outerloop
    iteration: 13 [(24, 13), (23, 20), (24, 23), (22, 5), (24, 3), (21, 58), (21, 55)] (24,13) (23,20)
    iteration: 14 [(24, 13), (23, 20), (24, 23), (22, 5), (24, 3), (21, 58), (21, 55)] (23,20) (24,23)
    iteration: 15 [(24, 13), (24, 23), (23, 20), (22, 5), (24, 3), (21, 58), (21, 55)] (23,20) (22,5)
    iteration: 16 [(24, 13), (24, 23), (23, 20), (22, 5), (24, 3), (21, 58), (21, 55)] (22,5) (24,3)
    iteration: 17 [(24, 13), (24, 23), (23, 20), (24, 3), (22, 5), (21, 58), (21, 55)] (22,5) (21,58)
    iteration: 18 [(24, 13), (24, 23), (23, 20), (24, 3), (22, 5), (21, 58), (21, 55)] (21,58) (21,55)
    outerloop
    iteration: 19 [(24, 13), (24, 23), (23, 20), (24, 3), (22, 5), (21, 58), (21, 55)] (24,13) (24,23)
    iteration: 20 [(24, 23), (24, 13), (23, 20), (24, 3), (22, 5), (21, 58), (21, 55)] (24,13) (23,20)
    iteration: 21 [(24, 23), (24, 13), (23, 20), (24, 3), (22, 5), (21, 58), (21, 55)] (23,20) (24,3)
    iteration: 22 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (23,20) (22,5)
    iteration: 23 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (22,5) (21,58)
    iteration: 24 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (21,58) (21,55)
    outerloop
    iteration: 25 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (24,23) (24,13)
    iteration: 26 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (24,13) (24,3)
    iteration: 27 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (24,3) (23,20)
    iteration: 28 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (23,20) (22,5)
    iteration: 29 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (22,5) (21,58)
    iteration: 30 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (21,58) (21,55)
    outerloop
    iteration: 31 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (24,23) (24,13)
    iteration: 32 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (24,13) (24,3)
    iteration: 33 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (24,3) (23,20)
    iteration: 34 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (23,20) (22,5)
    iteration: 35 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (22,5) (21,58)
    iteration: 36 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (21,58) (21,55)
    outerloop
    iteration: 37 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (24,23) (24,13)
    iteration: 38 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (24,13) (24,3)
    iteration: 39 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (24,3) (23,20)
    iteration: 40 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (23,20) (22,5)
    iteration: 41 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (22,5) (21,58)
    iteration: 42 [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)] (21,58) (21,55)
    Pass
    number of iteration: 7*6 = 42



```python

```
