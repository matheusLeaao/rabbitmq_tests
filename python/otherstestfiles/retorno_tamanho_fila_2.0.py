#!/usr/bin/env python

import pika
import traceback

#Conexao

credentials     = pika.PlainCredentials('rabbitmq', 'rabbitmq') #...(user,pass)
parameters      = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection      = pika.BlockingConnection(parameters)
channel         = connection.channel()

print("Connection opened! :D\n")


queueName       = input("Qual o nome da fila?\n")
durable         = input("[DURABLE] A fila persiste ao reboot do servidor? (Only "'False'" ou "'True'")\n")


queueResult = channel.queue_declare(queue=queueName,
                                durable=durable,
                                passive=True,)
if (pika.exceptions.ChannelClosedByBroker == (404, "NOT_FOUND - no queue 'fila' in vhost '/'")):
    print("Queue '"+queueName+"' doesn't exist on vhost.")    

declarationQueue = channel.queue_declare(queueName, 
                                        passive=False,
                                        durable=durable,
                                        exclusive=False,
                                        auto_delete=False,
                                        arguments=None,)
counter        = declarationQueue.method.message_coun
print('A fila "'+str(queueName)+'" possui: '+str(counter)+'  mensagens\n')
connection.close()
print ("Connection closed! :D")
