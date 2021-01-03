library(ggplot2)

#Save as PNG
png("rplot.png")

#Load in the data
df <- data.frame(dose=c("D0.5", "D1", "D2"), len=c(4.2, 10, 29.5))


#Plor the Plot
p<-ggplot(data=df, aes(x=dose, y=len)) +
  	geom_bar(stat="identity", fill="darkgray", width=0.5)+
    theme_minimal()


p

