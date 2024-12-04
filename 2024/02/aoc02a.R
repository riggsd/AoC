#!/usr/bin/env Rscript

# https://adventofcode.com/2024/day/2

input <- lapply(readLines("input.txt"), function(x) as.numeric(strsplit(x, " ")[[1]]))

diffs <- lapply(input, diff)

safe <- function(a) {
  diffs <- diff(a)
  if (!(all(diffs < 0) || all(diffs > 0))) return(FALSE)
  diffs <- abs(diffs)
  if (max(diffs) > 3 || min(diffs) < 1) return(FALSE)
  TRUE
}

total <- sum(unlist(lapply(input, safe)))
print(total)
