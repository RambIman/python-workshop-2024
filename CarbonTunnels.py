import pandas as pd
import numpy as np

def calculate_shaft_co2(data, concrete_emission_factor, excavation_emission_factor, transport_emissions_factor):
  """Calculates CO2 emissions for each tunnel shaft.

  Args:
    data: Pandas DataFrame containing shaft data.
    concrete_emission_factor: CO2 emissions per cubic metre of concrete.
    excavation_emission_factor: CO2 emissions per cubic metre of excavated material.
    transport_emissions_factor: CO2 emissions per ton-km travelled

  Returns:
    Pandas Series with CO2 emissions for each shaft.
  """

  # Calculate concrete volume
  data['concrete_volume'] = np.pi * ((data['diameter'] / 2) ** 2) * (data['thickness'] + data['base_slab_thickness'])

  # Estimate excavated material (assuming cylindrical shape for simplicity)
  data['excavated_volume'] = np.pi * ((data['diameter'] / 2) ** 2) * data['thickness']
  # Assuming density of excavated material as 2.5 tons/m^3
  data['excavated_mass'] = data['excavated_volume'] * 2.5

  # Calculate CO2 emissions
  data['concrete_co2'] = data['concrete_volume'] * concrete_emission_factor
  data['excavation_co2'] = data['excavated_volume'] * excavation_emission_factor
  data['transport_co2'] = data['excavated_mass'] * data['excavation_distance'] * transport_emissions_factor
  data['total_co2'] = data['concrete_co2'] + data['excavation_co2'] + data['transport_co2']

  return data['total_co2']

# Example usage
data = pd.read_csv('./data/tunnel_data.csv')
concrete_emission_factor = 0.2  # Example value, adjust based on region and concrete mix
excavation_emission_factor = 0.05  # Example value, adjust based on transport mode and distance
transport_emissions_factor = 3 

co2_emissions = calculate_shaft_co2(data, concrete_emission_factor, excavation_emission_factor, transport_emissions_factor)
print(co2_emissions)
