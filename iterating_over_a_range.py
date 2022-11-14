bacteria = "X"

for generation in range(0, 10):
  bacteria = bacteria + bacteria

print(bacteria)

#print with a 500 millisecond delay between generations
import time
generations = 10

for generation in range (0, generations):
  bacteria = bacteria * 2
  print(bacteria)
  time.sleep(0.5)