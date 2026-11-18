# Hadoop-MapReduce-Exercise


## Exercise 2

**Q1. Is your change in the mapper or in the reducer?**

The change is in the mapper because it processes each word before counting. We used `lower()` to convert words to lowercase and `rstrip(',.')` to remove trailing commas and dots.

## Exercise 3

**Q1. Is your change in the mapper or in the reducer?**

The change is in the reducer because it calculates the total count for each word and selects the three words with the highest counts.
