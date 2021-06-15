#from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession


#conf = SparkConf()
#conf.setAppName('my application name')
#conf.set('spark.executor.memory', '14g')
#conf.set('spark.executor.cores', 2)	
#sc = SparkContext(conf=conf)

spark = SparkSession \
	.builder \
	.appName("Python Spark SQL basic example")\
	.getOrCreate()


bInput = spark.read.format("parquet").load("./binary-classification")\
  .selectExpr("features", "cast(label as double) as label")



from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression()
print lr.explainParams() # see all parameters
lrModel = lr.fit(bInput)

print lrModel.coefficients
print lrModel.intercept

summary = lrModel.summary
print summary.areaUnderROC
summary.roc.show()
summary.pr.show()

summary.objectiveHistory

from pyspark.ml.classification import DecisionTreeClassifier
dt = DecisionTreeClassifier()
print dt.explainParams()
dtModel = dt.fit(bInput)


from pyspark.ml.classification import RandomForestClassifier
rfClassifier = RandomForestClassifier()
print rfClassifier.explainParams()
trainedModel = rfClassifier.fit(bInput)

from pyspark.ml.classification import GBTClassifier
gbtClassifier = GBTClassifier()
print gbtClassifier.explainParams()
trainedModel = gbtClassifier.fit(bInput)

from pyspark.ml.classification import NaiveBayes
nb = NaiveBayes()
print nb.explainParams()
trainedModel = nb.fit(bInput.where("label != 0"))

from pyspark.mllib.evaluation import BinaryClassificationMetrics
out = model.transform(bInput)\
  .select("prediction", "label")\
  .rdd.map(lambda x: (float(x[0]), float(x[1])))
metrics = BinaryClassificationMetrics(out)

print metrics.areaUnderPR
print metrics.areaUnderROC
print "Receiver Operating Characteristic"
metrics.roc.toDF().show()
