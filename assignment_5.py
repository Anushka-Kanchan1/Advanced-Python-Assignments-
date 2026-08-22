# Longest Common Subsequence using Dynamic Programming

def calculate_lcs(first, second):

    a = len(first)
    b = len(second)

    matrix = [[0] * (b + 1) for x in range(a + 1)]

    # Build the DP matrix
    for x in range(a):
        for y in range(b):

            if first[x] == second[y]:
                matrix[x + 1][y + 1] = matrix[x][y] + 1

            else:
                value1 = matrix[x][y + 1]
                value2 = matrix[x + 1][y]

                matrix[x + 1][y + 1] = value1 if value1 >= value2 else value2

    # Find the actual LCS
    x = a
    y = b
    answer = []

    while x > 0 and y > 0:

        if first[x - 1] == second[y - 1]:
            answer.append(first[x - 1])
            x -= 1
            y -= 1

        elif matrix[x - 1][y] >= matrix[x][y - 1]:
            x -= 1

        else:
            y -= 1

    answer.reverse()

    return ''.join(answer), matrix[a][b]


# Main Program

print("LONGEST COMMON SUBSEQUENCE")
print("--------------------------")

first_string = input("Enter first sequence: ")
second_string = input("Enter second sequence: ")

subsequence, size = calculate_lcs(first_string, second_string)

print("\nFirst Sequence  :", first_string)
print("Second Sequence :", second_string)
print("Common Sequence  :", subsequence)
print("Length           :", size)


OUTPUT

Enter first sequence: ABCDGH
Enter second sequence: AEDFHR

First Sequence  : ABCDGH
Second Sequence : AEDFHR
Common Sequence : ADH
Length          : 3
