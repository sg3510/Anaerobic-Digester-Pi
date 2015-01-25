#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('anaeropi', 'D1g3sting!')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='adigester')

message = raw_input("What do you want to tell the other Pis?")
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print " [x] Sent '%s'" % message
connection.close()