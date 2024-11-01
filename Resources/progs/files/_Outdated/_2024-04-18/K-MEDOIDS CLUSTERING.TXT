library(factoextra)
df <- USArrests
df <- na.omit(df)
df <- scale(df)
head(df)
fviz_nbclust(df, pam, method = "wss")
gap_stat <- clusGap(df,FUN = pam,K.max = 10,B = 50)
fviz_gap_stat(gap_stat)
set.seed(1)
kmed <- pam(df, k = 4)
kmed
fviz_cluster(kmed, data = df)