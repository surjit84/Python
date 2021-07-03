# significance value = alpha (decided by domain expert)
# Confidence interval CI based on aplha value/
# perform p value based on statistical analysis
# if p value falls in CI region then accept H0 (null hypothesis)
# if p value is outside of CI region the we will reject H0, and accept alternate hypothesis H1.
# p value is outcome of statistical experiment and aplha value is given by domain expert

# Type of Tests
# Z Test Comparison of Mean
# T Test: Comparison of Mean
# f Test: Comparison of variance
# ANOVA Test: Analysis of Variance Test
# Chi2 Test: Comparision/Correlation between two categorical Variables

# Point Estimate : Value of any statistics that estimate value of a parameter is called point estimate.
# Confidence Interval = Point Estimate +/- Margin of Error

# Eg: On Verbal Test of CAT exam, sd = 100,  
#25 test taken, they have mean of 520, Construct a 95% CI about mean

#sd = 100, n = 25, alpha = .05, CI = 95%

# = 520 + Z(0.025)*(100/root(25))
# = 520 + 1.96*(100/root(25)) = 559.2
# = 520 - Z(0.025)*(100/root(25))
# = 520 - 1.96*(100/root(25)) = 480.2

# So if value is between 480.2 to 559.2 then we will accept H0 else H1 with 95% CI.


