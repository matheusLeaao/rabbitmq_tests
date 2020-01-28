#!/usr/bin/env python

import pika

# this queue is the destination queue
#credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
#parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
#connection = pika.BlockingConnection(parameters)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


print " connection created"

channel = connection.channel()
channel.queue_declare(queue='hello', durable=True)

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()