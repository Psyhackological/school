"""
This module contains two functions: int_to_u2() and main().

int_to_u2(decimal: int) -> str:
This function converts an integer to its binary and hexadecimal representation
in the following format: "binary:1111 0000 hex:0xF0".

Args:
    decimal: An int to be converted.

Returns:
    A string in the format "binary:1111 0000 hex:0xF0".

main():
This function calls int_to_u2() and prints the result for each number in the range -127..128 (8bit).
"""
from math import ceil


def int_to_u2(decimal: int, bits=8) -> str:
    """
    This function converts an integer to its binary and hexadecimal representation in the format
    "binary:1111 0000 hex:0xF0"

    :param decimal: integer to be converted
    :return: string in the format "binary:1111 0000 hex:0xF0"
    """
    binary = ""
    # Iterate 8 times
    for i in range(bits):
        # Check if the least significant bit is set and add it to the binary string
        binary = str(decimal & 1) + binary
        # Shift the bits to the right
        decimal = decimal >> 1
    # Convert binary to hexadecimal
    hex_str = hex(int(binary, 2))[2:].upper()
    # Add spaces between each 4 bit
    binary_with_spaces = " ".join([binary[i : i + 4] for i in range(0, len(binary), 4)])
    # return in the format "binary:1111 0000 hex:0xF0"
    return f"binary:{binary_with_spaces} hex:{'0x' + hex_str.zfill(ceil(bits/4))}"


def main(bits=8):
    """
    This function calls int_to_u2() and prints the result for each number in the range -127 to 128
    """

    start = -(2 ** (bits - 1))
    end = 2 ** (bits - 1)
    # loop through the range -127 to 128
    for i in range(start, end):
        # convert i to a string and right justify it to 4 spaces
        i_str = str(i).rjust(len(str(start)))
        # print the result of int_to_u2 for the current value of i
        print(f"{i_str} = {int_to_u2(i, bits)}")


if __name__ == "__main__":
    main(8)
