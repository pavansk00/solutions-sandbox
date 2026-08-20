from pyspark.sql import SparkSession
import os
import sys 
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

def spark_session():
    """
    Create a SparkSession for testing purposes.

    """
    spark = SparkSession.builder.appName("TestApp").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    print(f"SparkSession created successfully.{spark.version}")

    return spark



