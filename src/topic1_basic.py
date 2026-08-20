from test import spark_session
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

def task1():
    """
    Task 1: Create a SparkSession and perform a simple operation.

    """
    spark = spark_session()

    product_data = [
        (1, "Laptop", "Electronics", 45000),
        (2, "Smartphone", "Electronics", 15000),
        (3, "Tablet", "Electronics", 25000),
        (4, "Movie", "Entertainment", 400),
        (5, "Pizza", "Food", 500)
    ]
    product_schema = StructType([
        StructField("product_id", IntegerType(), True),
        StructField("product_name", StringType(), True),
        StructField("category", StringType(), True),
        StructField("price", IntegerType(), True)
    ])

    product_df = spark.createDataFrame(product_data, schema=product_schema)
    product_df.show()
    spark.stop()


task1()