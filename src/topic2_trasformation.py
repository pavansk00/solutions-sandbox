from test import spark_session
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

def trasformation_task():
    """
    Transformation Task: Create a SparkSession, perform transformations on a DataFrame, and display the results.

    """
    spark = spark_session()

    Employee_data = [
        (1, "Pav", "Support", 50000, 100),
        (2, "Mad", "Data", 60000, 500),
        (3, "cha", "Marketing", 45000, 200)
    ]
    Employee_schema = StructType([
        StructField("emp_id", IntegerType(), True),
        StructField("emp_name", StringType(), True),
        StructField("department", StringType(), True),
        StructField("baseSalary", IntegerType(), True),
        StructField("bonus", IntegerType(), True)
    ])

    emp_df = spark.createDataFrame(Employee_data, schema=Employee_schema)
    print("===================Initial Employee DataFrame:========================")
    emp_df.show()
    emp_df = emp_df.withColumn("Total_compansation", F.col("baseSalary") + F.col("bonus"))
    print("===================After adding Total_compansation column========================")
    emp_df.show()
    emp_df = emp_df.withColumn("Status", F.when(F.col("Total_compansation") > 60000, "Senior").otherwise("Junior"))
    print("===================After adding Status column========================")
    emp_df.show()
    emp_df = emp_df.filter(F.col("Department") == "Data")
    print("===================After filtering for Data department========================")
    emp_df.show()
    emp_df = emp_df.withColumnRenamed("baseSalary", "base_pay").drop("bonus")
    print("===================After renaming baseSalary to base_pay and dropping bonus column========================")
    emp_df.show()
    spark.stop()

trasformation_task()