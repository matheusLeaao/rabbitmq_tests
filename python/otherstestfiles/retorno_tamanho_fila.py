#!/usr/bin/env python

# Retorno tamanho da fila rabbitmq , número de mensagens em determinada fila
#
# Github : matheusLeaao  <https://github.com/matheusLeaao>
# @author Matheus Leão <mathegiov@hotmail.com>


import pika
#Conexao
credentials     = pika.PlainCredentials('rabbitmq', 'rabbitmq') #...(user,pass)
parameters      = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection      = pika.BlockingConnection(parameters)
channel         = connection.channel()
print("Connection opened! :D\n")
queueName       = "hello" 
declarationQueue = channel.queue_declare(queueName, 
                                        passive=False,
                                        durable=True,
                                        exclusive=False,
                                        auto_delete=False,
                                        arguments=None,)
counter        = declarationQueue.method.message_count
print('A fila "'+str(queueName)+'" possui: '+str(counter)+'  mensagens\n')
connection.close()
print ("Connection closed! :D")
