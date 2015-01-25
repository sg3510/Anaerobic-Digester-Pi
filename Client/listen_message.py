#!/usr/bin/env python
import pika

host = raw_input("What is the host you want to listen to?")

credentials = pika.PlainCredentials('anaeropi', 'D1g3sting!')
parameters = pika.ConnectionParameters(host, 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()


channel.queue_declare(queue='adigester')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()