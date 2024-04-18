import pandas as pd 
file_path = '1981_2020_ktm_pkr.xlsx'
from scipy.stats import gamma
import numpy as np 

# Use the sheet_name parameter to specify the sheet index (zero-based)
# For sheet index 2, use sheet_name=1
df = pd.read_excel(file_path, sheet_name=1)

df['Time'] = pd.to_datetime(df['Time'])

df.set_index('Time',inplace=True)
df['Kathmandu Airport'] = df['Kathmandu Airport'].astype(float)


all_historical_values = df['Kathmandu Airport'].values 
all_historical_values = df['Kathmandu Airport'].values

# Create a boolean mask for finite values
finite_mask = np.isfinite(all_historical_values)

# Filter the finite values using the mask
finite_values = all_historical_values[~finite_mask]
print(finite_values)
print(element for element in all_historical_values if type(element)!=float)

shape,loc,scale = gamma.fit(finite_values)

print(shape,loc,scale)

last_28_days = all_historical_values[-35:-7].sum()
print(last_28_days)
def calculate_spi(observed_precipitation, shape, loc, scale):
    # Ensure observed_precipitation is a NumPy array
    observed_precipitation = np.asarray(observed_precipitation)

    # Check for valid parameter values
    if shape <= 0 or scale <= 0:
        raise ValueError("Shape and scale parameters must be positive.")

    # Calculate CDF
    cdf = gamma.cdf(observed_precipitation, shape, loc=loc, scale=scale)

    # Check for CDF values close to 1
    if np.any(np.isclose(cdf, 1)):
        print("Warning: CDF values close to 1. Check parameter values and data range.")

    # Calculate SPI
    spi = 1 / shape * (1 / (1 - cdf) - 1)

    return spi

spi_values = calculate_spi(last_28_days, shape, loc, scale)
print(spi_values)






