#!/bin/bash

# Define the script file
script_name="ant_colony_optimization.py"

# Check if the script file exists
if [ ! -f "$script_name" ]; then
	echo "The script $script_name does not exist."
	exit 1
fi

# Run the script 10000 times in parallel and append the results to best_paths.txt
seq 10000 | parallel -n0 python3 ../"$script_name" >>best_paths.txt

# Sort the results numerically and retain only unique duplicate lines
sort -n outcome.txt | uniq -d >best_paths_count.txt

# Count the occurrences of each line
sort -n outcome.txt | uniq -c >best_paths_unique.txt

echo "Done"
