# Summer 2023
This repository contains Python scripts for simulating and analyzing Agrobacterium-mediated plant transformations, focusing on the efficiency of kanamycin resistance and GUS staining.

### 1. Data Simulation
`generate_input.py` creates a simulated dataset reflecting realistic experimental conditions:

- **Probabilities:** Based on typical transformation success rates observed in the literature and experimental data:
  - **pCAMBIA2301:** 90% kanamycin resistance, 80% GUS staining
  - **pSSK6A:** 85% kanamycin resistance, 75% GUS staining
  - **Non-Transformed:** 5% kanamycin resistance, 2% GUS staining

### 2. Automated Analysis
`process_data.py` reads the generated data, calculates mean success rates, and visualizes the results in bar charts.

![image](https://github.com/user-attachments/assets/2b0c30e2-395a-4d26-b0a1-bd37b066b1cd)
