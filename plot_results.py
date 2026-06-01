import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "reports/results.csv"
)

summary = (

    df.groupby(
        ["model","persona"]
    )["score"]

    .mean()

    .unstack()
)

summary.plot(
    kind="bar"
)

plt.title(
    "Average Benchmark Score"
)

plt.ylabel(
    "Average Score"
)

plt.tight_layout()

plt.savefig(
    "reports/benchmark_plot.png"
)

print(
    "Saved reports/benchmark_plot.png"
)