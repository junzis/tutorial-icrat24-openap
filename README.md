# ICRAT 2024 OpenAP Tutorial

This repository contains a set of notebooks for the OpenAP Tutorial.

You may clone the repository and run the notebooks locally, or use Google Colab to run the notebooks online.

To run the notebooks on Google Colab, click the "Open in Colab" button below each notebook.

# Dependencies

If you want to run the notebooks locally, you need to install the following library:

- `openap`
- `openap-top`
- `openap-polymer`

You can install the library using pip:

```bash
pip install --upgrade openap
pip install --upgrade openap-top
pip install --upgrade git+https://github.com/junzis/openap-polymer

# Optional dependencies for wind data in grib format
pip install cfgrib
pip install ecmwflibs
```

# Tutorials

## 1. Fuel and emission estimations

This tutorial provides examples of estimating fuel and emissions using the OpenAP library.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/junzis/tutorial-icrat24-openap/blob/master/1_openap_fuel_and_emissions.ipynb)

## 2. Fuel calculation with reduced order model

This tutorial provides examples of calculating fuel using the reduced order model `opeanap-polymer`.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/junzis/tutorial-icrat24-openap/blob/master/2_openap_reduced_order_model.ipynb)

## 3. Trajectory optimization

This tutorial provides examples of trajectory optimization using the `openap-top` library.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/junzis/tutorial-icrat24-openap/blob/master/3_openap_trajectory_optimization.ipynb)
