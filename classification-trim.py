#from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

#sc = SparkContext()

spark = SparkSession \
	.builder \
	.appName("Python Spark SQL basic example")\
	.getOrCreate()

bInput = spark.read.format("parquet").load("./binary-classification")\
  .selectExpr("features", "cast(label as double) as label")

