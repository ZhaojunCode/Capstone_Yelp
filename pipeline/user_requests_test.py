from kafka import KafkaProducer
import csv
import json

# Connect to Kafka
producer = KafkaProducer(bootstrap_servers='ec2-54-173-251-232.compute-1.amazonaws.com:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
topic = 'spark2sql'

with open('IUC-businesses.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict  = {}
    for rows in reader:
        mydict['id'] = rows[0]
        mydict['name'] = rows[1]
        mydict['longitude'] = rows[2]
        mydict['latitude'] = rows[3]
        producer.send(topic, mydict)
