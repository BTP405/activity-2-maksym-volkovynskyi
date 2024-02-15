def decorator(func):
    def wrapper(line):
        numbers = func(line)
        print(f'Numbers read: {numbers}')
        print(f'Count: {len(numbers)}')
        print(f'Avg: {sum(numbers) / len(numbers)}')
        print(f'Max: {max(numbers)}')
        print('')
    return wrapper

@decorator
def parseInput(line):
    numbers = []
    for word in line.split():
        numbers.append(int(word))
    return numbers

def printStats(t):
    f = open(t, 'r')
    for line in f:
        parseInput(line)
        
printStats('q4.txt')