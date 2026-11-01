from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly
import json

app = Flask(__name__)


# Membaca dataset
def load_data():
    df = pd.read_csv("data/meteorites.csv", encoding="cp1252")
    df["year"] = pd.to_datetime(df["year"], errors="coerce").dt.year
    return df


@app.route("/")
def dashboard():
    df = load_data()

    # Ringkasan dataset
    total = len(df)
    rata_massa = round(df["mass (g)"].mean(), 2)
    fell = int((df["fall"] == "Fell").sum())
    found = int((df["fall"] == "Found").sum())

    # Grafik 1: Peta persebaran meteorit
    fig_map = px.scatter_geo(
        df,
        lat="reclat",
        lon="reclong",
        color="type",
        hover_name="name",
        title="Peta Persebaran Meteorit",
    )

    # Grafik 2: Jumlah meteorit per tahun
    per_tahun = df.groupby("year").size().reset_index(name="jumlah")
    fig_tahun = px.line(
        per_tahun,
        x="year",
        y="jumlah",
        title="Jumlah Meteorit per Tahun",
        labels={"year": "Tahun", "jumlah": "Jumlah Meteorit"},
    )

    # Grafik 3: Distribusi tipe meteorit
    tipe = df["type"].value_counts().reset_index()
    tipe.columns = ["type", "jumlah"]
    fig_tipe = px.pie(
        tipe,
        names="type",
        values="jumlah",
        hole=0.4,
        title="Distribusi Tipe Meteorit",
    )

    # Grafik 4: 10 kelas meteorit terbanyak
    kelas = df["class"].value_counts().reset_index()
    kelas.columns = ["class", "jumlah"]
    fig_kelas = px.bar(
        kelas,
        x="class",
        y="jumlah",
        title="Jumlah Meteorit per Kelas",
        labels={"class": "Kelas", "jumlah": "Jumlah Meteorit"},
    )

    # Konversi grafik menjadi JSON
    graphs = [
        json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        for fig in [fig_map, fig_tahun, fig_tipe, fig_kelas]
    ]

    return render_template(
        "dashboard.html",
        total=total,
        rata_massa=rata_massa,
        fell=fell,
        found=found,
        graphs=graphs,
    )


if __name__ == "__main__":
    app.run(debug=True)
