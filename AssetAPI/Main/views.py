from django.shortcuts import render
from rest_framework.views import APIView


class Customer(APIView):
    '''
    View, Create, Update a single Customer
    '''

    def get(self, request):
        pass
    def post(self, request):
        pass
    def put(self, request):
        pass

class Personnel(APIView):
    '''
    View, Create, Update a single Customer
    '''
    def get(self, request):
        pass
    def post(self, request):
        pass
    def put(self, request):
        pass

class Asset(APIView):
    '''
    View, Create, Update a single Asset of type Vehicle of Generic
    '''
    def get(self, request):
        pass
    def post(self, request):
        pass
    def put(self, request):
        pass

class FleetRental(APIView):
    '''
    View, Create, Update a single Fleet of assets rental
    '''
    def get(self, request):
        pass
    def post(self, request):
        # check for cross customer asset assignment
        pass
    def put(self, request):
        pass

class Trip(APIView):
    '''
    View, Create, Update a single Trip of a vehicle asset
    '''
    def get(self, request):
        pass
    def post(self, request):
        pass
    def put(self, request):
        pass








