# Write a function to print the transposition (rows and columns changed) of a
# two-dimensional array with M rows and N columns

# assuming a well-formed array is getting passed in here...
def transposition(values):
    result = []

    for x in range(len(values)):
        result.append([])

    for x in range(len(values)):
        for y in values:
            result[x].append(y[x])

    return result


if __name__ == "__main__":
    result = transposition([ [1,1,1], [2,2,2], [3,3,3] ])
    print(result)
