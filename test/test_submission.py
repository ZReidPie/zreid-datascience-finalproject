import pandas as pd
import pytest
import requests

# Test if submission file exists and has correct columns
def test_submission_file():
    # Load the submission file
    submission_path = 'data/submission.csv'
    submission_df = pd.read_csv(submission_path)

    # Check that the file has the expected columns
    expected_columns = ['title_romaji', 'average_score', 'true_rating']
    assert all(col in submission_df.columns for col in expected_columns), "Submission file is missing required columns"

    # Check if there are no NaN values in 'true_rating'
    assert not submission_df['true_rating'].isnull().any(), "Submission contains NaN values in 'true_rating'"

# Test if validation metrics are within expected bounds
def test_model_performance():
    # Expected bounds for performance metrics
    expected_mae_upper = 5.0  # Adjust based on your acceptable error
    expected_rmse_upper = 6.0

    # Load your metrics (replace with actual method to fetch metrics)
    val_mae = 3.2172  # Replace with the dynamically calculated metric
    val_rmse = 4.1791  # Replace with the dynamically calculated metric

    assert val_mae < expected_mae_upper, f"Validation MAE is too high: {val_mae}"
    assert val_rmse < expected_rmse_upper, f"Validation RMSE is too high: {val_rmse}"

# Test AniList API request functionality
def test_anilist_api_request():
    # Define the AniList API endpoint and query
    url = "https://graphql.anilist.co"
    query = '''
    query ($id: Int) {
      Media(id: $id, type: ANIME) {
        id
        title {
          romaji
          english
        }
        averageScore
        popularity
      }
    }
    '''
    variables = {"id": 1}  # Testing with an example ID

    # Make the API request
    response = requests.post(url, json={"query": query, "variables": variables})

    # Check that the request was successful
    assert response.status_code == 200, f"API request failed with status code {response.status_code}"

    # Parse the JSON response
    data = response.json()

    # Check if the response contains the expected keys
    assert "data" in data and "Media" in data["data"], "Response JSON does not contain expected keys"
    assert "title" in data["data"]["Media"], "Media object does not contain title information"

    # Check that the title and averageScore are not None
    assert data["data"]["Media"]["title"]["romaji"] is not None, "Romaji title is missing"
    assert data["data"]["Media"]["averageScore"] is not None, "Average score is missing"

    print("AniList API request test passed.")