'''
    Here is the actual implementation of consumer_queue
    It works of threading handles mutiple clients
    Celery is large process for this mini task
    addINtoQueue  :  New payload can be added to consumer queue
    addTask class : This implementation creates Thread to compute answer for payload in consumer queue
    All cases are handled and followed PEP-8 Standards
'''

import time
from threading import Thread
from .models import AdditionData as db
from queue import Queue

consumerQueue = Queue()
isalive = False

# condition to chekc whether thread is running or not
# It stops creating mutiple Threads


def isAlive():
    return isalive

# every new payload is added to queue


def addIntoQueue(payload):
    consumerQueue.put(payload)
    # debugging
    print("New Task " + str(payload.get("unique_identifier")) + " added")

# long running consumer Queue additon task
# Usage of celery is overkill for this porject
# So i used threading


class addTask(Thread):

    def __init__(self):
        global isalive
        if not isalive:
            Thread.__init__(self)
        isalive = True

    def run(self):
        print("Queue Consumer is started listening in background")
        while(True):
            # check for new tasks
            if not consumerQueue.empty():
                # Sleep 10 seconds
                time.sleep(10)
                payload = consumerQueue.get()
                # computer answer and add into database using unique_identifier
                dbInstance = db.objects.get(
                    pk=payload.get("unique_identifier"))
                dbInstance.number1 = payload.get("number1")
                dbInstance.number2 = payload.get("number2")
                dbInstance.answer = dbInstance.number1 + dbInstance.number2
                dbInstance.save()
                # debugging
                print(str(dbInstance.pk)+" Task Finished")
