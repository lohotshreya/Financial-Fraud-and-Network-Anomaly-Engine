import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_synthetic_ledger(n_normal=5000, seed=42):
    """
    Generates a synthetic financial ledger with normal corporate baselines
    and injected multi-dimensional macro fraud vectors.
    """
    np.random.seed(seed)
    base_time = datetime(2026, 5, 25, 0, 0, 0)
    
    # ---------------------------------------------------------
    # 1. NORMAL BASELINE: Exponentially distributed expenditures
    # ---------------------------------------------------------
    normal_amounts = np.random.exponential(scale=200.0, size=n_normal) + 5.0
    # Evenly distribute transactions over a 24-hour delta spectrum
    normal_times = [base_time + timedelta(seconds=int(np.random.uniform(0, 86400))) for _ in range(n_normal)]
    
    # Generate account IDs (dense, repetitive corporate accounts)
    src_pool = [f"ACC-CORP-{i:03d}" for i in range(1, 21)]
    dest_pool = [f"ACC-VEND-{i:03d}" for i in range(1, 50)]
    
    df_normal = pd.DataFrame({
        'timestamp': normal_times,
        'source_id': [np.random.choice(src_pool) for _ in range(n_normal)],
        'destination_id': [np.random.choice(dest_pool) for _ in range(n_normal)],
        'amount': normal_amounts,
        'label': 0  # Clean baseline
    })

    # ---------------------------------------------------------
    # 2. FRAUD VECTOR A: Liquidity Extraction Spikes
    # ---------------------------------------------------------
    # Massive capital movements inside an engineered tight time-window
    n_vector_a = 15
    spike_amounts = np.random.uniform(25000.0, 75000.0, size=n_vector_a)
    spike_time_base = base_time + timedelta(hours=14) # Occurs at 2:00 PM
    spike_times = [spike_time_base + timedelta(seconds=int(np.random.uniform(0, 45))) for _ in range(n_vector_a)]
    
    df_vector_a = pd.DataFrame({
        'timestamp': spike_times,
        'source_id': [f"ACC-MAL-ERR" for _ in range(n_vector_a)],
        'destination_id': [f"ACC-OFFSHORE-{i:02d}" for i in range(n_vector_a)],
        'amount': spike_amounts,
        'label': 1  # Structural Anomaly
    })

    # ---------------------------------------------------------
    # 3. FRAUD VECTOR B: Structuring / Smurfing Network Rings
    # ---------------------------------------------------------
    # Coordinated attack: single source node rapid-fires tiny fragmented amounts 
    # milliseconds apart to multiple destination nodes to evade manual detection thresholds
    n_vector_b = 8  # 1 source to 8 distinct nodes in a tightly clustered group
    smurf_amounts = np.random.uniform(5.0, 15.0, size=n_vector_b)
    smurf_time_base = base_time + timedelta(hours=3) # Occurs at 3:00 AM (unusual hour)
    smurf_times = [smurf_time_base + timedelta(milliseconds=int(i * 15)) for i in range(n_vector_b)]
    
    df_vector_b = pd.DataFrame({
        'timestamp': smurf_times,
        'source_id': ["ACC-SHELL-RING" for _ in range(n_vector_b)],
        'destination_id': [f"ACC-SMURF-DEST-{i:02d}" for i in range(n_vector_b)],
        'amount': smurf_amounts,
        'label': 1  # Coordinated Network Anomaly
    })

    # Combine, sort by time execution, and reset index
    ledger = pd.concat([df_normal, df_vector_a, df_vector_b], ignore_index=True)
    ledger = ledger.sort_values(by='timestamp').reset_index(drop=True)
    
    # Feature Engineering: Calculate transactional velocity (Time Delta in seconds from start)
    ledger['time_delta'] = (ledger['timestamp'] - base_time).dt.total_seconds()
    
    return ledger

if __name__ == "__main__":
    df = generate_synthetic_ledger()
    print(f"📊 Synthesized Ledger Status: Complete.")
    print(f"Total Logs Audited: {len(df)} | Underlying Anomalous Imbalance: {df['label'].sum()} records.")





    
