# Hadoop-MapReduce-Exercise

## Exercise 1

**Q1. How many files are there now?**

There are 6 output files (`part-00000` to `part-00005`), plus one `_SUCCESS` file.

**Q2. Did the number of mappers change?**

No, the number of mappers remained 9 because the input files and input splits did not change.

**Q3. Did the number of reducers change?**

Yes, the number of reducers increased from 3 to 6 because we added the parameter `-numReduceTasks 6`.

**Q4. Did the number of output files change? Why?**

Yes, the number of output files increased from 3 to 6 because each reducer creates its own output file.

**Q5. What does the value of "Merged Map outputs" represent, and how is it calculated?**

"Merged Map outputs" represents the number of map outputs merged by the reducers during the shuffle and merge phase.

In the first run, there were 9 mappers and 3 reducers, resulting in 27 merged map outputs (9 × 3).

In the second run, there were 9 mappers and 6 reducers, resulting in 54 merged map outputs (9 × 6).

In our runs, this value equals the number of mappers multiplied by the number of reducers.

## Exercise 2

**Q1. Is your change in the mapper or in the reducer?**

The change is in the mapper because it processes each word before counting. We used `lower()` to convert words to lowercase and `rstrip(',.')` to remove trailing commas and dots.

## Exercise 3

**Q1. Is your change in the mapper or in the reducer?**

The change is in the reducer because it calculates the total count for each word and selects the three words with the highest counts.
