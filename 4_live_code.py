# %%
import numpy as np
import openap
import pandas as pd
from openap import top

# %%
origin = "WSSS"
destination = "ZSHC"
mass = 0.85

# %%
optimizer = top.CompleteFlight("A320", origin, destination, mass)
flight = optimizer.trajectory()

# %%
top.vis.trajectory(flight)

# %%
import fastmeteo

# %%

latitudes = np.linspace(-10, 40, 20)
longitudes = np.linspace(100, 130, 20)
altitudes = np.linspace(1000, 45000, 30)
timestamps = pd.date_range("2024-01-01 08:00:00", "2024-01-01 15:00:00", freq="1H")

latitudes, longitudes, altitudes, times = np.meshgrid(
    latitudes, longitudes, altitudes, timestamps
)

grid = pd.DataFrame().assign(
    latitude=latitudes.flatten(),
    longitude=longitudes.flatten(),
    altitude=altitudes.flatten(),
    timestamp=times.flatten(),
)

grid


# %%
fmg = fastmeteo.Grid(local_store="/tmp/era5-zarr")
wind = fmg.interpolate(grid)

# %%
wind = (
    wind.rename(columns={"u_component_of_wind": "u", "v_component_of_wind": "v"})
    .assign(ts=lambda x: (x.timestamp - x.timestamp.iloc[0]).dt.total_seconds())
    .eval("h=altitude * 0.3048")
)

# %%
optimizer = top.CompleteFlight("A320", origin, destination, mass)
optimizer.enable_wind(wind)
flight = optimizer.trajectory()

# %%
top.vis.trajectory(flight)
