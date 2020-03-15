
## Problem Statement

Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number of platforms required so that no train has to wait for the other(s) to leave. 

You will be given arrival and departure times in the form of a list.

Note: Time `hh:mm` would be written as integer `hhmm` for e.g. `9:30` would be written as `930`. Similarly, `13:45` would be given as `1345`


```python
def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    return
```

<span class="graffiti-highlight graffiti-id_khuho24-id_mgzo0p4"><i></i><button>Hide Solution</button></span>


```python
def min_platforms(arrival, departure):
    # sort the lists in ascending order
    arrival.sort()
    departure.sort()
    
    # initialize the platform for the first arrival
    platform_count = 1
    output = 1
    
    i = 1 # iterator for the arrival (start at the second arrival)
    j = 0 # iterator for the departure
    
    # the arrival list may be longer than the departure list
    # some trains may not leave the station

    while i < len(arrival) and j < len(arrival):
        print('arrival time: {} \t departure time: {}'.format(arrival[i],departure[j]))
        # if the arrival time of a train in the station is less than the 
        # earliest departure time of the trains in the station:
        if arrival[i] < departure[j]:
    
            platform_count += 1 # increment the number of platforms
            i += 1 # move to the next arrival time (train)
            
            # we need a variable output to keep track of the maximum deadlock
            # note that the platform count can increase and decrease
            if platform_count > output:
                output = platform_count

        else: # otherwise a train left the station before the current arrival train
            platform_count -= 1 # decrement the number of platforms
            j += 1 # move to the next departure time (train)
        print('platform count: {} \t output: {}'.format(platform_count, output))

    return output
```


```python
def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]
    
    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
```


```python
arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)
```

    arrival time: 940 	 departure time: 910
    platform count: 0 	 output: 1
    arrival time: 940 	 departure time: 1120
    platform count: 1 	 output: 1
    arrival time: 950 	 departure time: 1120
    platform count: 2 	 output: 2
    arrival time: 1100 	 departure time: 1120
    platform count: 3 	 output: 3
    arrival time: 1500 	 departure time: 1120
    platform count: 2 	 output: 3
    arrival time: 1500 	 departure time: 1130
    platform count: 1 	 output: 3
    arrival time: 1500 	 departure time: 1200
    platform count: 0 	 output: 3
    arrival time: 1500 	 departure time: 1900
    platform count: 1 	 output: 3
    arrival time: 1800 	 departure time: 1900
    platform count: 2 	 output: 3
    Pass



```python
arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)
```

    arrival time: 210 	 departure time: 230
    platform count: 2 	 output: 2
    arrival time: 300 	 departure time: 230
    platform count: 1 	 output: 2
    arrival time: 300 	 departure time: 320
    platform count: 2 	 output: 2
    arrival time: 320 	 departure time: 320
    platform count: 1 	 output: 2
    arrival time: 320 	 departure time: 340
    platform count: 2 	 output: 2
    arrival time: 350 	 departure time: 340
    platform count: 1 	 output: 2
    arrival time: 350 	 departure time: 400
    platform count: 2 	 output: 2
    arrival time: 500 	 departure time: 400
    platform count: 1 	 output: 2
    arrival time: 500 	 departure time: 430
    platform count: 0 	 output: 2
    arrival time: 500 	 departure time: 520
    platform count: 1 	 output: 2
    Pass



```python

```
