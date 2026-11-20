# Exploring the relationship between qualifying and finishing positions in Formula 1.

This project aims to explore how qualifying position in F1 relates to a driver's race finishing position, and whether this changes depending on the circuit.

- **Student ID: 24000132614**
- **Repository:** M6006-ds2026-24000132614

This project lives in `project/`, alongside `requirements.txt`. The repository is the whole course folder: `.gitignore` is at the repository root, and the week folders hold the lab notebooks.

## Research question
To what extent does qualifying performance predict race results in F1, and how might this relationship change between circuits?

## The real-world problem and who it affects
Qualifying in Formula 1 is the primary determining factor in the starting order of a Grand Prix. The outcome of qualifying is therefore very important to constructors (teams), drivers and fans, and expands the strategy for winning a Grand Prix outside just the one race. As such, it is key to understand how close the relationship between qualifying position and finishing position is, as it may influence race strategy, performance analysis and expectations in order to maximize race results. This project seeks to provide a statistical backing for this relationship, and explore how it might change across different circuits. This is especially interesting as it may means team's should have different strategies depending specifically on the circuit itself. Formula 1 is built on details, and not a single stone can be left unturned. This exploration is a sliver of insight into the kind of information and predictions stakeholder's in F1 need to be aware of in order to produce results.

These stakeholder's are not just the drivers of the cars, as F1 is really a team sport. Race strategists, analysts and even engineers will need to have access to this kind of information in order to optimize performance. 

## Data

The data was sourced from Kaggle and is available at: https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020/data?select=qualifying.csv under a CC0: Public Domain license. 

Please download the data folder which contains the necessary CSV files and analysisData file. This dataset was selected due to it having extensive historical and modern data that would be versatile for a range of research questions. The dataset was easily accessible and manageable due to it being separated into multiple CSV files. As not all of these tables were necessary for this project, I was able to simply not include those files instead of having to edit one large table that included everything. This dataset also came well recommended on Kaggle with many users commenting on its quality and usefulness. 

## Cleaning and preprocessing
See notebooks 01_cleaning and 02_preprocessing

## Descriptive statistics and visualisation
See notebook 03_exploratory_analysis

## Analysis plan
I plan to use supervised regression to predict race finishing position based on qualifying position, and expand this to include per-circuit predictions. I will start by creating a simply linear regression model, and then use multiple regression to investigate difference between circuits, and whether this improves predictions. If within scope, I may be able to add more circuit specific information or other variables, such as length, number of corners etc to examine differences in prediction accuracy. The primary variables I will use will be qualifying posititon, position, positionDiff, absolutePositionDiff and circuit info. 

The data will be split into training and testing sets, ideally separated by seasons rather than random selection, so that the models can be evaluated on races they have not seen before. I will continually compare training and testing outputs to identify and mitigate potential over or undercutting, but I will favor simpler models where performance is retained.

I will use mean absolute error to evaluate the accuracy of predicted positions. This can be comapred against a simple baseline, such as predicting that drivers will finish where they qualified. 

Models performance will be compared to establish to what extent qualifying position predicts finishing position and how much introducing circuit-level data influences these predictions.


## How to run this

From the repository root: create and activate a virtual environment, download the data folder and open the notebooks in `project/`, then run `pip install -r requirements.txt` before running the notebook code.

## Use of AI (required)

- **Tool:** GitHub Copilot, Tutor agent (VS Code)
- **Model:** Automatic selection, including GPT-6 and MAI Code Flash 2
- **Used for:** basic debugging, and asking for assistance with python and terminal syntax.
- **Not used for:** Writing any code or text included in the final output. 

- - **Tool:** ChatGPT
- **Model:** GPT-6 and 6.1, OpenAI
- **Used for:** Recommendations for structuring notebooks and file tree, debugging discrepancies in merged tables, and assistance with debugging creating plots for the shiny app, including looking up syntax.
- **Not used for:** Writing any code or text included in the final output. 
