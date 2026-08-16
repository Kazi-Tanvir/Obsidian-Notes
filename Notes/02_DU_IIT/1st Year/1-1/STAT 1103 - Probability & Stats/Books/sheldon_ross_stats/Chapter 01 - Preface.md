# Preface

The sixth edition of this book continues to demonstrate how to apply probability theory to gain insight into real, everyday statistical problems and situations. As in the previous editions, carefully developed coverage of probability motivates probabilistic models of real phenomena and the statistical procedures that follow. This approach ultimately results in an intuitive understanding of statistical procedures and strategies most often used by practicing engineers and scientists.

This book has been written for an introductory course in statistics or in probability and statistics for students in engineering, computer science, mathematics, statistics, and the natural sciences. As such it assumes knowledge of elementary calculus.

## Organization and coverage

**Chapter 1** presents a brief introduction to statistics, presenting its two branches of descriptive and inferential statistics, and a short history of the subject and some of the people whose early work provided a foundation for work done today.

The subject matter of descriptive statistics is then considered in **Chapter 2**. Graphs and tables that describe a data set are presented in this chapter, as are quantities that are used to summarize certain of the key properties of the data set.

To be able to draw conclusions from data, it is necessary to have an understanding of the data’s origination. For instance, it is often assumed that the data constitute a “random sample” from some population. To understand exactly what this means and what its consequences are for relating properties of the sample data to properties of the entire population, it is necessary to have some understanding of probability, and that is the subject of **Chapter 3**. This chapter introduces the idea of a probability experiment, explains the concept of the probability of an event, and presents the axioms of probability.

Our study of probability is continued in **Chapter 4**, which deals with the important concepts of random variables and expectation, and in **Chapter 5**, which considers some special types of random variables that often occur in applications. Such random variables as the binomial, Poisson, hypergeometric, normal, uniform, gamma, chi-square, $t$, and $F$ are presented.

In **Chapter 6**, we study the probability distribution of such sampling statistics as the sample mean and the sample variance. We show how to use a remarkable theoretical result of probability, known as the central limit theorem, to approximate the probability distribution of the sample mean. In addition, we present the joint probability distribution of the sample mean and the sample variance in the important special case in which the underlying data come from a normally distributed population.

**Chapter 7** shows how to use data to estimate parameters of interest. For instance, a scientist might be interested in determining the proportion of Midwestern lakes that are afflicted by acid rain. Two types of estimators are studied. The first of these estimates the quantity of interest with a single number (for instance, it might estimate that 47 percent of Midwestern lakes suffer from acid rain), whereas the second provides an estimate in the form of an interval of values (for instance, it might estimate that between 45 and 49 percent of lakes suffer from acid rain). These latter estimators also tell us the “level of confidence” we can have in their validity. Thus, for instance, whereas we can be pretty certain that the exact percentage of afflicted lakes is not 47, it might very well be that we can be, say, 95 percent confident that the actual percentage is between 45 and 49.

**Chapter 8** introduces the important topic of statistical hypothesis testing, which is concerned with using data to test the plausibility of a specified hypothesis. For instance, such a test might reject the hypothesis that fewer than 44 percent of Midwestern lakes are afflicted by acid rain. The concept of the $p$-value, which measures the degree of plausibility of the hypothesis after the data have been observed, is introduced. A variety of hypothesis tests concerning the parameters of both one and two normal populations are considered. Hypothesis tests concerning Bernoulli and Poisson parameters are also presented.

**Chapter 9** deals with the important topic of regression. Both simple linear regression — including such subtopics as regression to the mean, residual analysis, and weighted least squares — and multiple linear regression are considered.

**Chapter 10** introduces the analysis of variance. Both one-way and two-way (with and without the possibility of interaction) problems are considered.

**Chapter 11** is concerned with goodness of fit tests, which can be used to test whether a proposed model is consistent with data. In it we present the classical chi-square goodness of fit test and apply it to test for independence in contingency tables. The final section of this chapter introduces the Kolmogorov–Smirnov procedure for testing whether data come from a specified continuous probability distribution.

**Chapter 12** deals with nonparametric hypothesis tests, which can be used when one is unable to suppose that the underlying distribution has some specified parametric form (such as normal).

**Chapter 13** considers the subject matter of quality control, a key statistical technique in manufacturing and production processes. A variety of control charts, including not only the Shewhart control charts but also more sophisticated ones based on moving averages and cumulative sums, are considered.

**Chapter 14** deals with problems related to life testing. In this chapter, the exponential, rather than the normal, distribution plays the key role.

In **Chapter 15**, we consider the statistical inference techniques of bootstrap statistical methods and permutation tests. We first show how probabilities can be obtained by simulation and then how to utilize simulation in these statistical inference approaches.

**Chapter 16**, new to this edition, introduces machine learning and big data techniques. These are methods that are applicable in situations where one has a large amount of data that can be used to estimate probabilities without assuming any particular probability model. For instance, we consider situations where one wants to estimate the probability that an experiment, characterized by a vector $(x_1,\dots,x_n)$, will be a success. When the characterizing vectors are qualitative in nature, such techniques as the naive Bayes approach, and nearest neighbor rules are studied. In cases where the components of the characteristic vector are quantitative, we also study logistic regression models.

Aside from the newly added Chapter 16, the most important change in this edition is the use of the statistical software R. No previous experience with R is necessary, and we incorporate its use throughout the text. Aside from additional subsections devoted to R, we also have the newly added Section 2.7, dealing with Lorenz curves and the Gini index. There are also many new examples and problems in this edition. In addition, the sixth edition contains a multitude of small changes designed to even further increase the clarity of the text’s presentations and arguments.

## Supplemental materials

Solutions manual for instructors is available at: https://textbooks.elsevier.com/web/Manuals.aspx?isbn=9780128243466.

## Acknowledgments

We thank the following people for their helpful comments on material of the sixth edition:

- Gideon Weiss, University of Haifa
- N. Balakrishnan, McMaster University
- Mark Brown, Columbia University
- Rohitha Goonatilake, Texas A and M University
- Steve From, University of Nebraska at Omaha
- Subhash Kochar, Portland State University
- Sumona Mondal, Mathematics, Clarkson University
- Kamel Belbahri, Mathematics and Statistics, Université de Montréal
- Anil Aswani, Industrial Engineering and Operations Research, University of California, Berkeley

as well as all those reviewers who asked to remain anonymous.
