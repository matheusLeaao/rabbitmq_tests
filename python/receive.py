#!/usr/bin/env python

import pika

#credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
#parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
#connection = pika.BlockingConnection(parameters)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


print "connection created"


channel.queue_declare(queue='hello', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()