#!/usr/bin/env Rscript

# https://adventofcode.com/2024/day/1

input <- read.table("input.txt", header = FALSE)
a <- input[, 1]
b <- input[, 2]
print( sum(abs(sort(a) - sort(b))) )
