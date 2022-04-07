# Rule generator

This file contains a summary of all functions from *rules.py*.

## Purpose of *rules.py*

The file contains functions to check for yahtzees/kniffels special rules.

## Functions

All functions dedicated to special rules check whether the rule applies to an array of numbers and returns the following tupel:
- (<rule applies>: bool, <score>: int)



| Name | Description | Points |
|------|-------------|--------|
| multiple(throws: [], amount) | Checks if an array has <amount> equal duplicates and returns true/false as well as the sum of the elements | <Sum of the multiple>|
| triplet(throws: []) | Rule applies when aray contains 3 equal numbers | <Sum of those numbers> |
| quardupel(throws: []) | Rule applies when array contains 4 equal numbers | <Sum of those numbers> |
| full_house(throws: []) | Rula applies when array contains a pair of equal numbers, a triplet of numbers and the pair and triplet are not made of the same numbers | 25 |
| small_road(throws: []) | Rule applies when array contains a line of 4 numbers which follow each other. E.g: *(1, 2, 3, 4)* or *(2, 3, 4, 5)* | 30 |
| big_road(throws: []) | Rule applies when array contains a line of 5 numbers which follow each other. E.g: *(1, 2, 3, 4, 5)* or *(2, 3, 4, 5, 6)* | 40 |
| yahtzee(throws: []) | Rule applies when all numbers in the array are the same. | 50 |
| chance(throws: []) | Rule always applies | <Sum of all numbers> |
