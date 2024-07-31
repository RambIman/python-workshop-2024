import pandas as pd
import numpy as np

# Generate mock data
np.random.seed(0)

# tunnel_data.csv
tunnel_data = pd.DataFrame({
    'tunnel_id': range(1, 6),
    'tunnel_name': [f'Tunnel_{i}' for i in range(1, 6)]
})

# materials.csv
materials = pd.DataFrame({
    'material_name': ['Concrete', 'Steel', 'Asphalt'],
    'embodied_carbon_kg_per_ton': [200, 1500, 50]
})

# equipment.csv
equipment = pd.DataFrame({
    'equipment_id': range(1, 6),
    'fuel_consumption_liters_per_hour': np.random.uniform(10, 50, 5),
    'energy_consumption_kWh_per_hour': np.random.uniform(20, 100, 5),
    'hours_used': np.random.uniform(100, 500, 5)
})

# excavation_data.csv
excavation_data = pd.DataFrame({
    'tunnel_id': np.random.choice(range(1, 6), 10),
    'material_excavated': np.random.choice(['Concrete', 'Steel', 'Asphalt'], 10),
    'volume_m3': np.random.uniform(100, 1000, 10),
    'transport_distance_km': np.random.uniform(10, 50, 10)
})

# energy_consumption.csv
energy_consumption = pd.DataFrame({
    'tunnel_id': np.random.choice(range(1, 6), 10),
    'energy_consumption_kWh': np.random.uniform(1000, 10000, 10)
})

# Save data to CSV files
tunnel_data.to_csv("./data/tunnel_data.csv", index=False)
materials.to_csv("./data/materials.csv", index=False)
equipment.to_csv("./data/equipment.csv", index=False)
excavation_data.to_csv("./data/excavation_data.csv", index=False)
energy_consumption.to_csv("./data/energy_consumption.csv", index=False)
