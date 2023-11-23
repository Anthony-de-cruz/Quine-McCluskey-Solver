def int_to_bin_str(number: int, digits: int) -> str:

    bin_str = str(bin(number))[2:]
    
    difference = len(bin_str) - digits
    if difference > 0:
        for digit in range(difference):
            
        


def get_ones(number: int) -> int:

    """Get the number of ones in the binary representation of a number"""

    bin_string = str(bin(number))[2:]

    ones = 0
    for char in bin_string:
        if char == "1":
            ones += 1

    return ones


def main():

    # Test table
    truth_table: dict[int, bool | None] = {
        0: False,
        1: False,
        2: False,
        3: False,
        4: True,
        5: False,
        6: False,
        7: False,
        8: True,
        9: None,
        10: True,
        11: True,
        12: True,
        13: False,
        14: None,
        15: True,
    }
    # Build min term table
    min_term_table: dict[int, dict[str, list[int]]] = {1: {}, 2: {}, 3: {}, 4: {}}

    for term in truth_table.keys():
        if truth_table.get(term) is True or truth_table.get(term) is None:
            min_term_table[get_ones(term)][str(bin(term))] = [term]

    print(min_term_table)

    print(int_to_bin_str(4, 1))


if __name__ == "__main__":
    main()
