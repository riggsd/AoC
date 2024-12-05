#!/usr/bin/env Rscript

# https://adventofcode.com/2024/day/3

input <- scan("input.txt", what = "character", quiet = TRUE)
text <- paste(input, collapse=" ")  # Combine into single string

pattern <- gregexpr("mul\\([0-9]{1,3},[0-9]{1,3}\\)", text)
matches <- regmatches(text, pattern)[[1]]

numbers <- gsub("mul\\(|\\)", "", matches)
pairs <- strsplit(numbers, ",")
result <- sum(sapply(pairs, function(p) as.numeric(p[1]) * as.numeric(p[2])))
print(result)