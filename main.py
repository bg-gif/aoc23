import regex

def get_file_info():
    with open('./inputs/dayone.txt') as f:
        lines = f.readlines()
        return lines

def find_numbers(lines):
    dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    allnums = []
    for line in lines:
        numbers = regex.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        for idx, val in enumerate(numbers):
            if val in dict.keys():
                numbers[idx] = dict[val]
        val = str(numbers[0]) + str(numbers[-1])
        allnums.append(int(val))
    return sum(allnums)

if __name__ == '__main__':
    lines = get_file_info()
    numbers = find_numbers(lines)
    print(numbers)

