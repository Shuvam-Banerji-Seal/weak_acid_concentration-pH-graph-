# Titration Analysis with Python

This Python script analyzes titration data, specifically the titration of phosphoric acid with sodium hydroxide. The data is read from a text file, and various plots are generated to visualize the titration curve and its derivatives.

## Usage

1. Ensure you have `numpy` and `matplotlib` installed:

   ```bash
   pip install numpy matplotlib
   ```

2. Run the script:

   ```bash
   python titration_analysis.py
   ```

## Analysis Steps

### 1. Read Data

```python
import numpy as np
import matplotlib.pyplot as plt

# Read data from text file
data = np.loadtxt("ph_data.txt", delimiter= '\t')
vol_naoh = data[:,0]
pH = data[:,1]
```

### 2. Calculate Derivatives

```python
# Calculate first and second derivatives
deriv1 = np.gradient(pH)
deriv2 = np.gradient(deriv1)
```

### 3. Find Local Maxima of First Derivative

```python
# Find local maxima of first derivative
maxima = np.where(np.r_[False, deriv1[1:] > deriv1[:-1]] & np.r_[deriv1[:-1] > deriv1[1:], False])[0]

# Sort maxima by the amplitude of the first derivative
maxima = maxima[np.argsort(-deriv1[maxima])]

# Take only the 3 largest peaks
maxima = maxima[:3]
```

### 4. Plot Data

```python
# Plot data
plt.figure(figsize=(5, 5))
plt.plot(vol_naoh, pH, '-', marker='o')
plt.xlabel("Volume of NaOH (ml)")
plt.ylabel("pH")
plt.title('Titration of Phosphoric Acid with NaOH')
```

### 5. Add Annotations for Peaks

```python
# Add annotations for peaks
for i in maxima:
    plt.annotate(f"End Point: pH {pH[i]} \n Vol. of NaOH: {vol_naoh[i]}", (vol_naoh[i], pH[i]), xytext=(40, -30),
            textcoords='offset points', arrowprops=dict(arrowstyle='->',
            connectionstyle='arc3,rad=.2'))

plt.show()
```

### 6. Plot First Derivative

```python
# Plot first derivative
plt.figure(figsize=(5, 5))
plt.plot(vol_naoh, deriv1, '-', marker ='o' )
plt.xlabel("Volume of NaOH (ml)")
plt.ylabel("First derivative of pH")
plt.title('First Derivative of Titration of Phosphoric Acid with NaOH')
```

### 7. Add Annotations for Peaks

```python
# Add annotations for peaks
for i in maxima:
    plt.annotate(f"Peak : pH {pH[i]} ", (vol_naoh[i], deriv1[i]), xytext=(15, 5),
            textcoords='offset points', arrowprops=dict(arrowstyle='->',
            connectionstyle='arc3,rad=.2'))

plt.show()
```

### 8. Plot Second Derivative

```python
# Plot second derivative
plt.figure(figsize=(5, 5))
plt.plot(vol_naoh, deriv2, '-', marker='o')
plt.xlabel("Volume of NaOH (ml)")
plt.ylabel("Second derivative of pH")
plt.title('Second Derivative of Titration of Phosphoric Acid with NaOH')

plt.show()
```

### 9. Store Data in a New Text File

```python
# Store data in a new text file
with open("titration_data.txt", "w") as f:
    f.write("Volume of NaOH (ml)\tpH\tFirst derivative of pH\tSecond derivative of pH\n")
    for i in range(len(vol_naoh)):
        f.write("{}\t{}\t{}\t{}\n".format(vol_naoh[i], pH[i], deriv1[i], deriv2[i]))
```

This script generates plots for the titration curve, first derivative, and second derivative. Annotations are added to highlight important points on the plots. The final titration data is stored in a new text file for further analysis.
