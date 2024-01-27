import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit()
    # Read database file into a variable
    with open(sys.argv[1]) as data:
        data_reader = csv.reader(data)
        data_list = []
        for r in data_reader:
            data_list.append(r)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as sequance:
        sequance_reader = sequance.read()

    # TODO: Find longest match of each STR in DNA sequence

    count = []
    for i in data_list[0][1:]:
        count.append(longest_match(sequance_reader, i))
    # TODO: Check database for matching profiles

    for i in range(1, len(data_list)):
        full_check = 0
        for j in range(1, len(count)+1):
            if int(data_list[i][j]) == count[j-1]:
                full_check += 1
            if full_check == len(count):
                print(data_list[i][0])
                exit(0)
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
