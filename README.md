# Quine-McCluskey-Solver
A script to minimize boolean functions using the Quine-McCluskey algorithm, providing working out.
[wikipedia](https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm)

The method involves 2 steps:
1. Find prime implicants
2. Use those implicants to find the essential implicants of the function, as well as other implicants that are necessary to complete the function.

Finding the implicants can be done iteratively.
Starting with a truth table, you can take all of the min terms and don't cares and place them in a min term table.
The table is arranged so the terms are put in order of the number of 1s in their binary representation.
Then iterate over the table, 
