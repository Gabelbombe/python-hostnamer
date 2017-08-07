#!/usr/bin/env python
import pika
import argparse

argp = argparse.ArgumentParser()
argp.add_argument('-s', '--server', metavar='server',
                  help='Magic!.',
                  default='localhost')
args = argp.parse_args()

connection = pika.BlockingConnection(pika.ConnectionParameters(host=args.server))
channel = connection.channel()

channel.queue_declare(queue='hello')

method_frame, header_frame, body = channel.basic_get(queue='hello')

if method_frame.NAME == 'Basic.GetEmpty':
    connection.close()
else:
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    connection.close()
print body
