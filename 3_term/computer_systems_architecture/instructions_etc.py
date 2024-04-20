

try:
    numbers_of_instructions = int(input("Number of instructions (default 1): "))
except ValueError:
    numbers_of_instructions = 1
try:
    CLOCK_FREQUENCY_MHZ = int(input("Clock frequency in MHz (default 80MHz): "))
except:
    CLOCK_FREQUENCY_MHZ = 80
    CLOCK_FREQUENCY_HZ = CLOCK_FREQUENCY_MHZ * 10**6

numbers_of_cycles = numbers_of_instructions * 2

def calculate_seconds(num_of_cycles: int) -> int:
    return 1 / (CLOCK_FREQUENCY_HZ / num_of_cycles)

def calculate_nanoseconds(num_of_cycles: int) -> int:
    return 1 / (CLOCK_FREQUENCY_HZ / num_of_cycles) * 10**9

def seconds_to_instructions(seconds: int):
    return CLOCK_FREQUENCY_HZ * seconds // 2

time_to_execute_in_seconds = calculate_seconds(numbers_of_cycles)
print(f"It executed in {time_to_execute_in_seconds} seconds")

time_to_execute_in_nanoseconds = calculate_nanoseconds(numbers_of_cycles)
print(f"It executed in {time_to_execute_in_nanoseconds} nanoseconds")

seconds = 300 # 5 minutes
num_of_instructions = seconds_to_instructions(seconds)
print(f"To wait {seconds} seconds you need {num_of_instructions} instructions.")
print(f"Zeroes: {str(num_of_instructions).count('0')}")