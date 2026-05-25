import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

class VectorAnomalyEngine:
    def __init__(self, contamination=0.01):
        self.scaler = StandardScaler()
        # Explicit hyperparameter tuning for low contamination and high velocity matrices
        self.model = IsolationForest(
            n_estimators=150, 
            contamination=contamination, 
            random_state=42,
            n_jobs=-1
        )
        
    def fit_predict(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardizes feature vectors and isolates sparse multi-dimensional geometric risks.
        """
        processed_df = df.copy()
        
        # Isolate numerical signals from structural string identifiers
        features = ['amount', 'time_delta']
        
        # Z-score scaling to eliminate magnitude dominance
        scaled_features = self.scaler.fit_transform(processed_df[features])
        
        # Fit and predict with Isolation Forest
        # -1 indicates anomaly, 1 indicates normal baseline in scikit-learn
        predictions = self.model.fit_predict(scaled_features)
        
        # Map back to intuitive binary flags (1 for risk anomaly, 0 for normal execution)
        processed_df['anomaly_flag'] = [1 if pred == -1 else 0 for pred in predictions]
        
        # Extract anomaly decision score paths for granular tracking
        processed_df['anomaly_score'] = self.model.decision_function(scaled_features)
        
        return processed_df
