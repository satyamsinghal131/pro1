from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status as httpstatus

from services.test_service import TestService

import json

# import logging
# import traceback
#
# logger = logging.getLogger("pro1")


def api_response(status, data=None, error=None, code=None):
    if code is None:
        if data:
            code = '200'
        elif error:
            # logger.error(error)
            code = '400'
        else:
            code = '200'
    return Response({'code': code, 'data': data, 'error': (error or "")}, status)


@api_view(['POST'])
def create(request):
    print("Request: {}".format(request.data))
    # logger.info('[{}] Request - {} API with data {}'.format(request.method, request.path, request.data))
    try:
        name = request.data.get('name')
        TestService.create_test(name)
        res = {"message": "Done!"}
        print("Response: {}".format(res))
        return api_response(data=res, status=httpstatus.HTTP_200_OK)
    except Exception as e:
        print("Exception occured: {}".format(e.message))
        # logger.error(
        #     '[{}] Request - {} API failed due to: {} - Traceback: {}'.format(request.method, request.path, e.message,
        #                                                                      traceback.format_exc()))
        return api_response(error='Something went wrong', status=httpstatus.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def find(request):
    print("Request: {}".format(request))
    # logger.info('[{}] Request - {} API with data {}'.format(request.method, request.path, request.data))
    try:
        name = request.GET.get('name')
        resp = TestService.filter_by_name(name)
        print("Response: {}".format(resp))
        return api_response(data=resp, status=httpstatus.HTTP_200_OK)
    except Exception as e:
        print("Exception occured: {}".format(e.message))
        # logger.error(
        #     '[{}] Request - {} API failed due to: {} - Traceback: {}'.format(request.method, request.path, e.message,
        #                                                                      traceback.format_exc()))
        return api_response(error='Something went wrong', status=httpstatus.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_all(request):
    print("Request: {}".format(request))
    # logger.info('[{}] Request - {} API with data {}'.format(request.method, request.path, request.data))
    try:
        resp = TestService.get_all()
        print("Response: {}".format(resp))
        return api_response(data=resp, status=httpstatus.HTTP_200_OK)
    except Exception as e:
        print("Exception occured: {}".format(e.message))
        # logger.error(
        #     '[{}] Request - {} API failed due to: {} - Traceback: {}'.format(request.method, request.path, e.message,
        #                                                                      traceback.format_exc()))
        return api_response(error='Something went wrong', status=httpstatus.HTTP_500_INTERNAL_SERVER_ERROR)
