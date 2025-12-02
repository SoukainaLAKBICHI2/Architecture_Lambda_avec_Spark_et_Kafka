from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, sum as spark_sum
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder.appName("StreamingLayer").getOrCreate()

schema = StructType() \
    .add("customer", StringType()) \
    .add("amount", IntegerType())

# Lire le flux Kafka
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "real-time-orders") \
    .option("startingOffsets", "latest") \
    .load()

# Convertir la valeur en JSON
df_parsed = df.selectExpr("CAST(value AS STRING) as json").select(from_json("json", schema).alias("data")).select("data.*")

# Agréger les montants par client
agg = df_parsed.groupBy("customer").agg(spark_sum("amount").alias("total_amount"))

# Afficher le résultat en console (pour démo)
query = agg.writeStream.outputMode("complete").format("console").start()

query.awaitTermination()
