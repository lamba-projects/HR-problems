letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'
'l', 'm', 'n', 'o', 'p','q','r','s','t','u','v','w','x','y','z'
]

def slowestKey(keyTimes):

    slowest_key = keyTimes[0][0]
    slowest_time = keyTimes[0][1]
    for i in range(1, len(keyTimes)):
        current_time = keyTimes[i][1] - keyTimes[i - 1][0]
        if current_time > slowest_time:
            slowest_time = current_time
            slowest_key = keyTimes[i][0]
    return letters[slowest_key]
