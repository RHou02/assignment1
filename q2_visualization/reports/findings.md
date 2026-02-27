# Assignment 1 — Question 2  
# Student Performance Visualization Analysis

---

## Data Ingestion and Preprocessing

The dataset contains 1000 student records with demographic and academic performance information. 
No missing values were detected in any of the columns. 
Therefore, no data imputation was required. 
A new variable, **overall_avg**, was created by calculating the mean of math, reading, and writing scores for each student. 
This variable represents overall academic performance. 
The dataset was clean and ready for visualization analysis.

---

## V1 — Gender Differences in Math and Reading

Female students score noticeably higher than male students in reading.  
In mathematics, female students score slightly lower than male students, although the difference is relatively small.  
The gender difference is more pronounced in reading than in math.  
Overall, there are moderate gender differences in academic performance.

---

## V2 — Impact of Test Preparation on Math Scores

The bar chart shows that students who completed the test preparation course have a higher average math score than those who did not complete it. 
This indicates a positive association between test preparation and math performance. 
The difference in mean scores suggests a meaningful performance gap between the two groups. 
While the visualization does not prove causation, it provides evidence that preparation is linked to improved outcomes. 
Overall, completing the test preparation course appears to benefit students’ math achievement.

---

## V3 — Lunch Type and Overall Academic Performance

The grouped bar chart indicates that students with standard lunch have a higher average overall score compared to those receiving free or reduced lunch. 
This suggests a potential relationship between socioeconomic factors and academic performance. 
The difference in mean overall averages highlights a noticeable performance gap. 
Students receiving free or reduced lunch tend to have lower overall academic outcomes. 
Although the visualization does not establish causation, it reveals an association between lunch type and student achievement. 
Overall, lunch type appears to be related to overall performance levels.

---

## V4 — Correlation Among Math, Reading, and Writing

The heatmap shows strong positive correlations among math, reading, and writing scores. All correlation coefficients are high and close to 1, indicating that students who perform well in one subject tend to perform well in the others. 
The strongest relationship appears between reading and writing scores. 
Math is also strongly associated with both reading and writing. 
These findings suggest that academic performance is consistent across subjects. 
Overall, the three subject scores move together in a strongly positive manner.

---

## V5 — Math vs Reading Relationship by Test Preparation

The scatter plot shows a strong positive relationship between reading and math scores for both groups. 
Students who completed the test preparation course and those who did not both exhibit similar upward trends. 
The regression lines have very similar slopes, suggesting that the strength of the relationship between reading and math does not substantially differ between the two groups. 
This indicates that test preparation may improve overall performance levels but does not significantly change the underlying association between reading and math scores. 
Overall, math and reading performance move together consistently regardless of preparation status.