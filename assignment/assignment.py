import pandas as pd
from pyspark import SparkConf
from pyspark.sql import SparkSession

BUCKET = "dmacademy-course-assets"
KEYpre = "vlerick/pre_release.csv"
KEYafter = "vlerick/after_release.csv"

config = {
    "spark.jars.packages": "org.apache.hadoop:hadoop-aws:3.3.1",
    "spark.hadoop.fs.s3a.aws.credentials.provider": "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider",
}
conf = SparkConf().setAll(config.items())
spark = SparkSession.builder.config(conf=conf).getOrCreate()

dfpre = spark.read.csv(f"s3a://{BUCKET}/{KEYpre}", header=True)
dfafter = spark.read.csv(f"s3a://{BUCKET}/{KEYafter}", header=True)
dfpre.show()
dfafter.show()

df_pre = dfpre.toPandas()
df_after = dfafter.toPandas()