from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

spark = SparkSession.builder.appName("BatchLayer").getOrCreate()

# Lire les données historiques
df = spark.read.json("/app/datasets/transactions.json")

# Agréger les montants par client
batch_result = df.groupBy("customer").agg(spark_sum("amount").alias("total_amount"))

batch_result.show()

# Sauvegarder les résultats batch
batch_result.coalesce(1).write.mode("overwrite").json("/app/batch_results")
spark.stop()
