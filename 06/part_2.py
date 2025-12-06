import sys

if __name__ == "__main__":
    worksheet = []
    number_length = -1
    with open(sys.argv[1]) as file_handle:
        for line in file_handle:
            worksheet.append(line[::-1][1:])
            number_length += 1
    total = 0
    numbers = []
    for i in range(len(worksheet[0])):
        number = ''
        for j in range(number_length):
            number += worksheet[j][i]
        try:
            numbers.append(int(number))
        except ValueError:
            next
        operator = worksheet[number_length][i]
        if operator == '*':
            answer = 1
            for number in numbers:
                answer *= number
            total += answer
            numbers = []
        elif operator == '+':
            answer = 0
            for number in numbers:
                answer += number
            total += answer
            numbers = []
    print(total)
