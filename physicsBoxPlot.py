#i have constant data and gotta make plot of those
#think box is the best
import numpy as np
import matplotlib.pyplot as plt

measurments = ["Bez obciążników", "Z obciążnikami \njak najbliżej \nśrodka", "Z obciążnikami \nna końcach"]
xax = np.arange(len(measurments))+1
#2 periods of vibration each
#Rod 1
rod_1 = np.array([[1.65, 1.57, 1.55, 1.65, 1.62],       #w/o weights
                  [1.84, 1.81, 1.85, 1.81, 1.78],       #central weights
                  [3.60, 3.68, 3.60, 3.69, 3.54],])     #wide weights
rod_1 /= 2
rod_1_avg = [round(np.average(row),3) for row in rod_1]
#Rod 2
rod_2 = np.array([[1.20, 1.22, 1.22, 1.23, 1.32],       #w/o weights
                  [1.38, 1.34, 1.38, 1.34, 1.29],       #central weights
                  [2.68, 2.64, 2.50, 2.73, 2.79]])      #wide weights
rod_2 /= 2
rod_2_avg = [round(np.average(row),3) for row in rod_2]
plt.bar(xax - 0.2 ,rod_1_avg, 0.4, label="Pręt 1")
plt.bar(xax + 0.2 ,rod_2_avg, 0.4, label="Pręt 2")
plt.xticks(xax, measurments)
plt.title("Średni czas pomiaru jednego okresu")
plt.legend()
plt.ylabel("[t]")
plt.grid()


plt.show()

