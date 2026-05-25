import pandas as pd
import networkx as nx

class TopologicalGraphAnalyser:
    def __init__(self):
        self.graph = nx.DiGraph()
        
    def construct_network(self, df: pd.DataFrame):
        """
        Builds a Directed Network Topology map out of transactional ledgers.
        """
        self.graph.clear()
        for _, row in df.iterrows():
            self.graph.add_edge(
                row['source_id'], 
                row['destination_id'], 
                amount=row['amount'],
                anomaly_flag=row['anomaly_flag']
            )
            
    def isolate_syndicate_rings(self, min_node_threshold=3) -> list:
        """
        Extracts interconnected sub-graph structures representing organized coordination.
        """
        # Isolate only edges flagged as anomalous by the Vector Processing Layer
        subgraph_edges = [
            (u, v, d) for u, v, d in self.graph.edges(data=True) 
            if d.get('anomaly_flag') == 1
        ]
        
        # Create a temporary anomaly-only graph
        anomaly_graph = nx.DiGraph()
        anomaly_graph.add_edges_from(subgraph_edges)
        
        # Convert to undirected graph structure to trace connected structural components
        undirected_anomaly = anomaly_graph.to_undirected()
        components = list(nx.connected_components(undirected_anomaly))
        
        # Filter for systemic syndicates based on node count size threshold
        syndicates = [comp for comp in components if len(comp) >= min_node_threshold]
        
        return syndicates
