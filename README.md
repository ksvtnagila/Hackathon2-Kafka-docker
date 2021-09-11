The hackathon2.ipynb file is given in the repo

Steps:
*Open a cmd promt from the location where the docker-compose
* run the command 'docker compose build'
*run 'docker-compose up'

*In new cmd, do a 'docker ps'
* In new cmd do a 'docker exec -it kafka-consumer bash'
Open a new command prompt and run 
docker exec -it kafka-producer bash
Open a new command prompt and run 
![image](https://user-images.githubusercontent.com/35005254/132939157-b0d912f8-3ddb-47aa-84c8-4d332ad43cc7.png)

docker exec -it zookeeper-1 bash
![image](https://user-images.githubusercontent.com/35005254/132939169-cd93982f-bf98-4fc6-9eb8-c45f8c554e1c.png)
*In zookeeper cmd
/kafka/bin/kafka-topics.sh \
--describe \
--topic PricePrediction \
--zookeeper zookeeper-1:2181
![image](https://user-images.githubusercontent.com/35005254/132939173-a160854f-c4f1-4e19-9808-37f6051528ad.png)

![image](https://user-images.githubusercontent.com/35005254/132939548-735b2218-15e6-42f3-9084-830a00bc79af.png)


In consumer cmd do a 
/kafka/bin/kafka-console-consumer.sh \
--bootstrap-server kafka-1:9092,kafka-2:9092,kafka-3:9092 \
--topic PricePrediction --from-beginning

![image](https://user-images.githubusercontent.com/35005254/132939185-aafd9502-65b4-4d52-bf9a-c528be4b343c.png)

To send a message to the consumer 
In producer cmd run

echo " 1461,20,RH,80,11622,Pave,NA,Reg,Lvl,AllPub,Inside,Gtl,NAmes,Feedr,Norm,1Fam,1Story,5,6,1961,1961,Gable,CompShg,VinylSd,VinylSd,None,0,TA,TA,CBlock,TA,TA,No,Rec,468,LwQ,144,270,882,GasA,TA,Y,SBrkr,896,0,0,896,0,0,1,0,2,1,TA,5,Typ,0,NA,Attchd,1961,Unf,1,730,TA,TA,Y,140,0,0,0,120,0,NA,MnPrv,NA,0,6,2010,WD,Normal" | \
/kafka/bin/kafka-console-producer.sh \
--broker-list kafka-1:9092,kafka-2:9092,kafka-3:9092 \
--topic PricePrediction > /dev/null

In a new cmd do-
*docker exec -it kafka_spark_worker2_1 bash
*pip install findspark
* pip install pandas
*![image](https://user-images.githubusercontent.com/35005254/132939489-e2e35fc7-bc04-4a27-abe9-22106338b76d.png)
* pip install seaborn
* then run the following command
*  ./bin/spark-submit --class org.apache.spark.examples.SparkPi --master yarn --deploy-mode cluster --num-executors 1 --driver-memory 1024m --executor-memory 1024m --executor-cores 1
lib/spark-examples*.jar 10

![image](https://user-images.githubusercontent.com/35005254/132939599-11c643f3-b651-4e24-9426-a428032a3b78.png)
