import pandas as pd
import tempfile
import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Tworzenie danych (1 mln wierszy)
num_rows = 100_000_000
data = {
    "name": [f"User{i}" for i in range(num_rows)],
    "age": [i % 60 + 20 for i in range(num_rows)],
    "salary": [3000 + (i % 5000) * 0.75 for i in range(num_rows)]
}
df = pd.DataFrame(data)

# Zapis do tymczasowego pliku CSV
tmp_csv = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
df.to_csv(tmp_csv.name, index=False)

print("CSV zapisany jako:", tmp_csv.name)

# Uruchomienie SparkSession
spark = SparkSession.builder.appName("PySparkSalaryAvg").getOrCreate()

# Wczytanie danych i obliczenie średniej pensji > 30 lat
start_time = time.time()
df_spark = spark.read.csv(tmp_csv.name, header=True, inferSchema=True)
avg_salary = (
    df_spark.filter(col("age") > 30)
    .select(avg("salary"))
    .collect()[0][0]
)
end_time = time.time()

print(f"Średnia pensja (>30 lat): {avg_salary:.2f}")
print(f"Czas wykonania: {end_time - start_time:.4f} s")

spark.stop()
