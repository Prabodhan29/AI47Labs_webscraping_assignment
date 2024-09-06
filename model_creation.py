import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load your CSV 
df = pd.read_csv('hospital_data.csv')

label_encoder = LabelEncoder()
df['state_encoded'] = label_encoder.fit_transform(df['State'])

# Split data into features and target
X = df[['state_encoded']]
y = df['Awards']

# Training and testing data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the trained model 
model_path = 'model.pkl'
joblib.dump(model, model_path)

print(f"Model saved to {model_path}")
