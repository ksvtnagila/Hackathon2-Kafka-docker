import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from pyspark.ml.regression import LinearRegression
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
from pyspark import SparkContext
from  pyspark.sql  import SQLContext
from pyspark.sql.functions import mean, min, max, avg, stddev, desc, isnull, col, log, lit
from pyspark.mllib.stat import Statistics
from pyspark.sql.types import DoubleType

from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler, PolynomialExpansion, VectorIndexer
import pricePrediction as pp

if __name__=="__main__":
    sc=SparkContext(appName="PricePrediction")
    
    ssc=StreamingContext(sc,60)
    message=KafkaUtils.createDirectStream(ssc, topics=['PricePrediction'], kafkaParams = {"metadata.broker.list": "localhost:9092"})
    message.pprint()
    pp.mainPricePrediction()
    ssc.start()
    ssc.awaitTermination()
    
