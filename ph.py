import numpy as np
import matplotlib.pyplot as plt

# Read data from text file
data = np.loadtxt("ph_data.txt", delimiter= '\t')
vol_naoh = data[:,0]
pH = data[:,1]

# Calculate first and second derivatives
deriv1 = np.gradient(pH)
deriv2 = np.gradient(deriv1)

# Find local maxima of first derivative
maxima = np.where(np.r_[False, deriv1[1:] > deriv1[:-1]] & np.r_[deriv1[:-1] > deriv1[1:], False])[0]

# Sort maxima by the amplitude of the first derivative
maxima = maxima[np.argsort(-deriv1[maxima])]

# Take only the 3 largest peaks
maxima = maxima[:3]

# Plot data
plt.figure(figsize=(5, 5))
plt.plot(vol_naoh, pH, '-', marker = 'o')
plt.xlabel("Volume of NaOH (ml)")
plt.ylabel("pH")
plt.title('Titration of Phosphoric Acid with NaOH')


# Add annotations for peaks
for i in maxima:
    plt.annotate(f"End Point: pH {pH[i]} \n Vol. of NaOH: {vol_naoh[i]}", (vol_naoh[i], pH[i]), xytext=(40, -30),
            textcoords='offset points', arrowprops=dict(arrowstyle='->',
            connectionstyle='arc3,rad=.2'))

plt.show()

plt.figure(figsize=(5, 5))
plt.plot(vol_naoh, deriv1, '-', marker ='o' )
plt.xlabel("Volume of NaOH (ml)")
plt.ylabel("First derivative of pH")
plt.title('First Derivative of Titration of Phosphoric Acid with NaOH')


# Add annotations for peaks
for i in maxima:
    plt.annotate(f"Peak : pH {pH[i]} ", (vol_naoh[i], deriv1[i]), xytext=(15, 5),
            textcoords='offset points', arrowprops=dict(arrowstyle='->',
            connectionstyle='arc3,rad=.2'))

plt.show()

plt.figure(figsize=(5, 5))
plt.plot(vol_naoh, deriv2, '-', marker = 'o')
plt.xlabel("Volume of NaOH (ml)")
plt.ylabel("Second derivative of pH")
plt.title('Second Derivative of Titration of Phosphoric Acid with NaOH')


plt.show()

# Store data in new text file
with open("titration_data.txt", "w") as f:
    f.write("Volume of NaOH (ml)\tpH\tFirst derivative of pH\tSecond derivative of pH\n")
    for i in range(len(vol_naoh)):
        f.write("{}\t{}\t{}\t{}\n".format(vol_naoh[i], pH[i], deriv1[i], deriv2[i]))
