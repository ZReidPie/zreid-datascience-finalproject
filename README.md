
# BU CS 506: Final Project

  

## Project Proposal: Predicting Consensus Anime Ratings

  

### 1. Description of the Project

This project aims to predict a consensus "true" rating for anime by leveraging data from AniList, one of the largest anime rating platforms. The core objective is to develop a model capable of determining an objective score for any given anime, independent of subjective biases or emotional reviews.

For years, "Trash Taste Disease" has skewed online ratings, with users writing overly emotional or incomplete reviews—sometimes after watching just one episode. This project seeks to mitigate such biases by analyzing comprehensive features, such as popularity, genre, studio, season, and other metadata, to calculate a statistically grounded rating.

By the end of this project, the goal is to provide a clear, data-driven consensus score that offers an objective evaluation of anime titles. This approach not only aims to improve the accuracy of ratings but also helps address long-standing inconsistencies in user-generated scores on platforms like AniList.

*(For those unfamiliar, anime refers to Japanese animated media—a diverse and complex art form encompassing a wide range of genres and storytelling styles.)*

---
  
### 2. Clear Goal(s)

- Successfully predict a consensus rating for anime titles based on features like genre, studio, episode count, and airing season.
- Use aggregated ratings as the target variable to provide a platform-independent score to eliminate bias.

---

### 3. Data Collection

**Data Sources**:
- AniList API

**Data to Collect**:
- Anime titles, ratings, and user count per platform.
- Features: genres, studios, episode count, airing season and year, source material, popularity metrics (e.g., review count).

Data will be collected via API calls and cleaned to ensure consistency across platforms.

---
### 4. Modeling Approach

**Model Selection**:
- XGBoost: Chosen for its efficiency, scalability, and ability to handle high-dimensional data.
- Hyperparameter tuning will optimize parameters like learning rate, max depth, and subsample ratio to achieve the best performance.

The target variable will be the weighted average of ratings across platforms, with weights based on the number of users.

---
### 5. Data Visualization

#### a. Rating Distribution Across Platforms
**Purpose**: Understand how ratings vary between different anime and platforms, identifying patterns or outliers.

**Visualization**:
- Histogram or Kernel Density Plot: To display the overall distribution of ratings.
- Overlay histograms to show differences in rating distributions across genres or studios.

#### b. Rating Discrepancies
**Purpose**: Highlight discrepancies between user-generated ratings and the predicted consensus rating.

**Visualization**:
- Bar Plot: Show the average rating difference for various genres or studios.

---
### 6. Testing & Reproducibility

**Test Plan**:
- Train-test split: Use 80% of data for training and 20% for testing.
- Hyperparameter tuning will use cross-validation to ensure robustness.

**Reproducibility**:
- Ensure code is modular and well-documented for ease of replication.
- Include requirements.txt for environment setup.

---

## How to Build and Use the Code

1. **Setup Environment**:
   - Install required dependencies: `pip install -r requirements.txt`.
   - Ensure Python version 3.8 or higher.
2. **Data Collection, Model Training, and Visualizations**:
   - All in code.py 

## How to Contribute

1. Fork the repository and create a new branch.
2. Make your changes and test thoroughly.
3. Submit a pull request with a clear description of your changes.

## How to Test the Code

1. Run `pytest` to ensure all tests pass.
2. Use `test_model.py` to validate model performance.

## Supported Environment

- Python 3.8+
- Tested on Windows 10 
