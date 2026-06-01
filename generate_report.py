import pandas as pd

df = pd.read_csv(
    "reports/results.csv"
)

leaderboard = (

    df.groupby(
        ["model","persona"]
    )["score"]

    .mean()

    .reset_index()

    .sort_values(
        by="score",
        ascending=False
    )
)

html = f"""

<html>

<head>

<title>
LLM Benchmark Dashboard
</title>

<style>

body {{
    font-family:Arial;
    margin:40px;
}}

h1 {{
    color:#1a73e8;
}}

table {{
    border-collapse:collapse;
    width:100%;
}}

th,td {{
    border:1px solid #ccc;
    padding:10px;
    text-align:center;
}}

th {{
    background:#222;
    color:white;
}}

.pass {{
    background:#b6f5b6;
}}

.fail {{
    background:#ffb3b3;
}}

</style>

</head>

<body>

<h1>
LLM Benchmark Dashboard
</h1>

<h2>
Leaderboard
</h2>

{leaderboard.to_html(index=False)}

<h2>
Benchmark Graph
</h2>

<img src="benchmark_plot.png" width="900">

<h2>
Detailed Results
</h2>

{df.to_html(index=False)}

</body>

</html>

"""

with open(

    "reports/dashboard.html",

    "w"

) as f:

    f.write(
        html
    )

print(
    "Saved reports/dashboard.html"
)