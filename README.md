# TOP 25 - PGA Masters Tournament
## Project Purpose and Description
 - The goal of this project was to gather data through an API or through web scraping and create a machine learning model that could classify the data in a specific manner.  

# Classification
Objective is to predict if a player would be a top 25 finisher in the Masters. All statistics/rankings are aggregated from a player’s performance in every PGA Tournament played leading up until the Masters Tournament that year. Data was scraped from 1980-2019. 

## Data:

! [Screenshot](https://github.com/FBowditch/Classification/blob/master/pga_charts/Stats.png)
 
- **pgatour.com**
	- Golf Player Statistics (1980-2009)
- **8 Main Features**
	- Number of Top 10's Made (STD)
	- Rank for Percent of Holes Better Than Par
	- Ranking for Total Money Earned (STD)
	- Percent of Greens Hit in Regulation
	- Percent Par3 Birdie or Better
	- Percent Par4 Birdie or Better
	- Percent Par5 Birdie or Better
	- Average Score Before Cut
	
## Tools (all in Python):
   - pandas
   - BeautifulSoup
   - Seaborn/Matplotlib
   - SciPy/NumPy
   - Scikit-learn
   
## Baseline Model

! [Screenshot](https://github.com/FBowditch/Classification/blob/master/pga_charts/baseline.png)

## Models Tested

   - Logistic Regression
   - Randorm Forest Regression
   - Support Vector Machine
 
## Conclusion & Going Forward

! [Screenshot](https://github.com/FBowditch/Classification/blob/master/pga_charts/roc_curve.png)

   - Logistic Regression performed the best
   - Out of all the predictions the model made 70% were correct
   - Improve F1 score
   - Statistics going back to 1980 were limited - Look at more recent years where more stats are available
   - Incorportate a parameter that accounts for a player's past PGA Master Tournament finishes/Major finishes

   
