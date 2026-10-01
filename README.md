# NBA-game-outcome-prediction
CS506 Final project - NBA game outcome prediction and betting market analysis

## 1. Project Description
The goal of this project is to build a machine learning system that predicts NBA game outcomes using hitorical team performance data. NBA teams can change significatnly throughout a season because of roster changes, injuries and changes in team performance. Because of this, using only season-long averages may not accurately represent a team's current strength. This project will focus on recent team performance by creating features based on statistics from each team's previous 5 and 10 games.

This project will use historical NBA game data from the 2024-2025 and 2025-2026 seasons, features such that the recent win percentage, points scored, rebounds, asists, shooting percentages, turnovers, point differential, and some other important data to predict the result of the game. Also, I also plan to explore predicting the final point differential between the two teams. several machine learning models, including Logistic regression, K-nearest Neighbors, and random forest, will be compared.

Last part of the project will investigate betting market information. If historical betting data is available, pre-game point spreads, moneylines, and over/under lines will becombined with the basketball statistics(I will first focus on pre-game point spreads). All features used for prediction will be based only on information available before each game in order prevent data leakage.

## 2. Project Goals
The main goal of this project is to evaluate how well machine learning models can predict NBA game outcomes using recent team performance and bettting market data. the specific goals are:

1. build a dataset that represent each NBA game using only information abvailable before the game, including rolling statistics from each team's previous 5-10 games.

2. training and compare multiple machine learning models, including logistic regression, K-nearest Neighbors, and random forest, to predict whether the home team will win or not.

3. compare the predictive value of statistics from the previous 5 games and previous 10 games to determine which time window better represents a team's recent performance.

4. Evaluate the models using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC......

5. Add betting data and compare a model using only basketball statistics with a model that also includes pre-game point spreads, moneylines, and over/under lines.

6. If time permits, I will develop an additional regression model to predict the point differential of future NBA games.

## 3. Data Collection Plan
NBA game data will be collected using the NBA stats API through the python 'nba_api' package. The dataset will include the games from the 2024-2025 and 2025-2026 NBA seasons. 

Historical pre-game betting data will be collected from a historical odds dataset or an odds API, depending on data availability. The main betting features will include point spreads, moneylines, and over/under totals.

### 3.1 Data preparation

The collected data will be cleaned and combined into a game level dataset, where each row represents on NBA game. missing values and games without enough previous ovservations will be handled during preprocessing. To avoid data leakage, the train and test sets will be separated chronologically rather than using a random split.

## 4. Project Timeline.
### Weeks 1-2: Data Collection and Preparation
- Collect NBA game data and historical betting data.
- Clean and combine the datasets.

### Weeks 3-4: Feature Engineering and Data Analysis
- Create features using statistics from the previous 5 and 10 games.
- Explore and visualize the data.

### Weeks 5-6: Model Development and Evaluation
- Train Logistic Regression, K-Nearest Neighbors, and Random Forest models.
- Evaluate and compare model performance.

### Weeks 7-8: Final Analysis and Presentation
- Compare basketball-only models with models that include betting data.
- Complete additional analysis if time permits.
- Prepare the final report and presentation.