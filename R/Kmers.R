#!/usr/bin/env Rscript
library(ggplot2)

#Allow arguments
args = commandArgs(trailingOnly=TRUE)

inn   <- args[1]
out   <- args[2]
title <- args[3]

#Save as PNG
png(args[2])

#Load in the data
data <- read.table(file = args[1], sep = '\t', header = FALSE)
names(data) <- c('Kmers','Frequency')

#Plot the plot
ggplot(data, aes(x=Kmers, y=Frequency)) + 
	  geom_bar(stat = "identity", fill="darkgray",  width=0.5) +
	  ggtitle(title)

