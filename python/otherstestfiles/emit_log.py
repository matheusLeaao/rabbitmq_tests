#!/usr/bin/env python
# Teste logs rabbitmq 
#
# Github : matheusLeaao  <https://github.com/matheusLeaao>
# @author Matheus Leão <mathegiov@hotmail.com>

import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()
