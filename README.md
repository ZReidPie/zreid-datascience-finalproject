# BU CS 506: Final Project 

## Project Proposal: Predicting Consensus Anime Ratings

### 1. Description of the Project

This project aims to predict a consensus "true" anime rating by aggregating scores from multiple platforms, such as MyAnimeList (MAL) and AniList. I need to see—no, I need to know—if people have voted correctly or if they statistically have trash taste. This is no laughing matter; Trash Taste Disease has plagued review sites for decades, with people writing emotional reviews after watching just one episode. 

*"You don’t know if the show is good or bad—you've only watched one episode; keep your opinions to yourself you uncultured swine!"*

I'm sorry, I got off on a tangent. Anyway, a Terminal Case of Bad Reviews is a very bad disease to suffer from. I really hope all you people get cured. But until then my project will help you. I have searched far and wide for datasets with the best taste and I will use them to cure you. The same way we created braille for the blind, wheelchairs for the disabled, I have created this program to calibrate your taste. No need to thank me.

**(serious)**

This project aims to predict a consensus "true" anime rating by aggregating scores from multiple platforms, such as MyAnimeList (MAL) and AniList. Anime ratings often vary across platforms due to differences in user demographics and rating systems. By combining these ratings, the project seeks to provide an unbiased score that reflects the general sentiment toward an anime. 

The goal at the end of this project is to find the objective score of any piece of anime. *(For those unfamiliar, anime refers to Japanese animated media—similar to cartoons but often encompassing a wide range of genres and complexities.)*

---

### 2. Clear Goal(s)

- Successfully predict a consensus rating for anime titles based on features like genre, studio, episode count, and airing season.
- Use aggregated ratings as the target variable to provide a platform-independent score to eliminate bias.

---

### 3. Data Collection

**Data Sources**:
- MyAnimeList API
- AniList API

**Data to Collect**:
- Anime titles, ratings, and user counts per platform.
- Features: genres, studios, episode count, airing season and year, source material, popularity metrics (e.g., review count).

Data will be collected via API calls and cleaned to ensure consistency across platforms.

---

### 4. Modeling Approach

**Model Selection**:
- Baseline: Linear Regression.
- Advanced: Tree-based models like XGBoost or LightGBM.

The target variable will be the weighted average of ratings across platforms, with weights based on the number of users.

---

### 5. Data Visualization

#### a. Rating Distribution Across Platforms
**Purpose**: Compare how ratings differ between MyAnimeList (MAL) and AniList.

**Visualization**:
- Histogram or Kernel Density Plot for ratings from each platform.
- Overlay histograms to show differences in rating distributions.

#### b. Rating Discrepancies
**Purpose**: Highlight differences between ratings for the same anime on different platforms.

**Visualization**:
- Scatter Plot: Plot MAL ratings on the x-axis and AniList ratings (normalized) on the y-axis.
  - Include a 45° reference line to easily spot discrepancies.
- Bar Plot: Show the average rating difference for various genres or studios.

---

### 6. Testing & Reproducibility

**Test Plan**:
- Train-test split: Use 80% of data for training and 20% for testing.
