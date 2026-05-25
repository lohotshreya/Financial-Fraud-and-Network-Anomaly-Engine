import streamlit as st
import plotly.express as px
import pandas as pd
from data_generator import generate_synthetic_ledger
from anomaly_engine import VectorAnomalyEngine
from network_analyser import TopologicalGraphAnalyser

# Set webpage configuration configurations
st.set_page_config(layout="wide", page_title="Structural Outlier Detector Architecture")

st.title("🛡️ The Structural Outlier Detector")
st.subtitle = "Financial Fraud & Network Anomaly Engine"
st.markdown("---")

# 1. Initialize Pipeline Execution
@st.cache_data
def run_pipeline():
    raw_data = generate_synthetic_ledger(n_normal=3000)
    
    # Vector Engine Extraction
    engine = VectorAnomalyEngine(contamination=0.012)
    vector_processed_data = engine.fit_predict(raw_data)
    
    # Topological Graph Analysis
    analyser = TopologicalGraphAnalyser()
    analyser.construct_network(vector_processed_data)
    syndicates = analyser.isolate_syndicate_rings(min_node_threshold=3)
    
    return vector_processed_data, syndicates

data, syndicates = run_pipeline()

# 2. Executive KPI Dashboard Metrics Layer
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Transaction Ledger Logs Audited", value=f"{len(data)}")
with col2:
    st.metric(label="Total Geometric Vector Anomalies Isolated", value=f"{data['anomaly_flag'].sum()}")
with col3:
    st.metric(label="Systemic Coordinated Syndicates Identified", value=f"{len(syndicates)}")

st.markdown("---")

# 3. High-Dimensional Interactive Vector Chart Visualization
st.subheader("📈 Multi-Dimensional Vector Clustering Space")
st.markdown(
    "This scatter plot maps out where standard operational traffic ends and anomalous risk begins based on random hyperplane space partitions."
)

fig = px.scatter(
    data, 
    x="time_delta", 
    y="amount", 
    color="anomaly_flag",
    color_discrete_map={0: '#00CC96', 1: '#EF553B'},
    hover_data=['source_id', 'destination_id', 'amount'],
    labels={'time_delta': 'Execution Time Delta (Seconds)', 'amount': 'Transaction Amount ($)'},
    title="Isolation Space Mapping Matrix"
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# 4. Cryptic Incident Report Center (Coordinated Syndicates Tracking)
st.subheader("🕵️ Network Security Incident Center")

if len(syndicates) > 0:
    for idx, ring in enumerate(syndicates):
        st.error(f"🚨 ALERT: Coordinated Syndicate Ring #{idx + 1} Extracted From Graph Topology")
        st.write(f"**Identified Network Compromised Node Accounts:** {list(ring)}")
        
        # Display underlying transaction data inside this ring
        ring_data = data[data['source_id'].isin(ring) | data['destination_id'].isin(ring)]
        st.dataframe(ring_data[['timestamp', 'source_id', 'destination_id', 'amount', 'anomaly_score']], use_container_width=True)
else:
    st.success("✅ No systemic multi-node network fraud syndicates discovered in the current network configuration.")
