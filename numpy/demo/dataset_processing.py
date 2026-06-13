import numpy as np

# Initialize the modern random generator
rng = np.random.default_rng(seed=42)

# 1. Continuous Sales Data (1000 rows, 3 features: Revenue, Expenses, Profit Margin)
sales_data = rng.normal(loc=5000, scale=1200, size=(1000, 3))

# 2. Discrete Customer Scores (500 entries with integer values from 1 to 10)
satisfaction_scores = rng.integers(low=1, high=11, size=500)

# 3. Binary Funnel Data (A/B testing conversion tracking for 10,000 users)
conversion_mask = rng.choice([0, 1], size=10000, p=[0.85, 0.15])

# Print shapes to verify structural configuration
print("Sales Data Shape:", sales_data.shape)
print("Scores Data Shape:", satisfaction_scores.shape)
print("Conversion Data Shape:", conversion_mask.shape)


#Reshaping the sales data to a 3D array (for example, 10 batches of 100 samples each)
reshaped_sales_data = sales_data.reshape(10, 100, 3)
# print("Reshaped Sales Data:\n", reshaped_sales_data)
print("Reshaped Sales Data Shape:", reshaped_sales_data.shape)

# check -1 
print("Last batch of reshaped sales data:\n", reshaped_sales_data[-1])
resized_scores_data = satisfaction_scores.reshape(-1, 10)  # Automatically determine the number of rows
print("Resized Scores Data Shape:", resized_scores_data.shape)


#Combining the sales data and scores data into a single dataset (for example, for a machine learning model)
# Note: This is just a demonstration; in practice, ensure that the number of samples matches
# For this example, we'll take the first 500 samples from sales_data to match the scores
combined_data = np.hstack((sales_data[:500], satisfaction_scores[:500].reshape(-1, 1)))  # Reshape scores to be a column vector
print("Combined Data Shape:", combined_data.shape)


#vstacking the conversion data with the combined data (for example, to analyze conversion rates alongside sales and scores)
# Note: Again, ensure that the number of samples matches; we'll take the first 500
conversion_data = conversion_mask[:500].reshape(-1, 1)  # Reshape conversion data to be a column vector
print("Conversion Data Shape:", conversion_data.shape)
