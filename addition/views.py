from django.http import HttpResponse, Http404, JsonResponse
from .models import AdditionData as Sum
from .consumer_queue import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

'''
index view handles "/" Route
'''


@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        # start Thread
        if isAlive() == False:
            print(isAlive())
            addTask().start()
        # connection established
        message = {"message": "Hi from test Api", "status": "200"}
        stat = status.HTTP_200_OK
    else:
        # connection not established or wrong method
        message = {"message": "Supports only GET", "status": "500"}
        stat = status.HTTP_500
    return Response(message, status=stat)


'''
 getNumbers handles "/calculate/number1/number2/" route
'''


@api_view(['GET'])
def getNumbers(request, number1, number2):
    if request.method == 'GET':
        # create instance to get unique identifier

        numbersInstance = Sum.objects.create()
        id = numbersInstance.pk
        numbersInstance.save()

        # create payload and add it to consumer queue
        payload = {
            "number1": number1,
            "number2": number2,
            "unique_identifier": id
        }

        # adding payload to cunsumer queue
        addIntoQueue(payload)
        data = {"identifier": id, "status": "200"}
        return Response(data, status=status.HTTP_200_OK)


'''
getAnswer Handles Route("/get_answer/identifier")
'''


@api_view(['GET'])
def getAnswer(request, identifier):
    if request.method == 'GET':
        try:
            # check for existence of identifier
            answerInstance = Sum.objects.get(pk=identifier)
        except Sum.DoesNotExist:
            # return not found
            data = {'message': 'identifier does not exist',
                    'status': 'HTTP_404_NOT_FOUND'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        # check for answer if completed the task get answer
        answer = answerInstance.answer
        data = {'message': answer, 'status': '200'}
        # task was not completed i.e answer was not computed
        if answer is None:
            data = {'message': 'Please Wait...............', 'status': '200'}
        return Response(data, status=status.HTTP_200_OK)
