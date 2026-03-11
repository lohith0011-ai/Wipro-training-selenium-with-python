import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps": [4000,5000,6000,7000,5500]
}

df = pd.DataFrame(data)
df.plot(x="Day", y="Steps", kind="bar")
plt.xlabel('Day')
plt.ylabel('Steps')
plt.title('Daily Steps Count')

# save as image -jpg
plt.savefig("BarChart.jpg")
# save as pdf
plt.savefig("bar.pdf", format="pdf")