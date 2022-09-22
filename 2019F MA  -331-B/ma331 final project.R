#Max Shi and Hien Bui Final Project R code

cheese <- read.csv("C:/Users/Max/Documents/ex11-54cheese.csv")
#11.53
summary(cheese)
sd(cheese$taste)
sd(cheese$acetic)
sd(cheese$h2s)
sd(cheese$lactic)
stem(cheese$taste)
qqnorm(cheese$taste)
qqline(cheese$taste)
stem(cheese$acetic)
qqnorm(cheese$acetic)
qqline(cheese$acetic)
stem(cheese$h2s)
qqnorm(cheese$h2s)
qqline(cheese$h2s)
stem(cheese$lactic)
qqnorm(cheese$lactic)
qqline(cheese$lactic)

#11.54
plot(cheese$taste, cheese$acetic)
cor.test(cheese$taste, cheese$acetic)
plot(cheese$taste, cheese$h2s)
cor.test(cheese$taste, cheese$h2s)
plot(cheese$taste, cheese$lactic)
cor.test(cheese$taste, cheese$lactic)
plot(cheese$acetic, cheese$h2s)
cor.test(cheese$acetic, cheese$h2s)
plot(cheese$acetic, cheese$lactic)
cor.test(cheese$acetic, cheese$lactic)
plot(cheese$h2s, cheese$lactic)
cor.test(cheese$h2s, cheese$lactic)
  
  
#11.55
cm1 = lm(taste ~ acetic, data = cheese)
summary(cm1)
qqnorm(residuals(cm1))
qqline(residuals(cm1))
plot(cheese$acetic,cheese$taste)
abline(cm1)
plot(cheese$h2s, residuals(cm1))
plot(cheese$lactic, residuals(cm1))
  
#11.56
cm2 <- lm(taste~h2s, data=cheese)
summary(cm2)
plot(cheese$h2s, cheese$taste)
abline(cm2)
plot(cheese$h2s, residuals(cm2))
qqnorm(residuals(cm2))
qqline(residuals(cm2))
plot(cheese$acetic, residuals(cm2))
plot(cheese$lactic, residuals(cm2))
  
#11.57:
cm3 <- lm(taste~lactic, data=cheese)
summary(cm3)
plot(cheese$lactic, cheese$taste)
abline(cm3)
plot(cheese$lactic, residuals(cm2))
qqnorm(residuals(cm3))
qqline(residuals(cm3))
plot(cheese$acetic, residuals(cm3))
plot(cheese$h2s, residuals(cm3))
  
#11.59:
mul1 <- lm(taste ~ acetic + h2s, data=cheese)
summary(mul1)
  
#11.60:
mul2 <- lm(taste ~ h2s + lactic, data=cheese)
summary(mul2)
  
#11.61:
mul3 <- lm(taste ~ acetic + h2s + lactic, data=cheese)
summary(mul3)
qqnorm(residuals(mul3))
qqline(residuals(mul3))
plot(cheese$acetic, residuals(mul3))
plot(cheese$h2s, residuals(mul3))
plot(cheese$lactic, residuals(mul3))
  
