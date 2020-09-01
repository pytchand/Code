from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# range of numbers

#numbers_to_add=list(range(1000000001))
#k=0

# only 3 numbers


def list_addition(request):
    numbers_to_add = [1, 2, 3,4,5,6,7,8,9,10]
    #numbers_to_add = list(range(1000000001)) ==> getting memory error due to my system configuration
    k = 0
    for i in numbers_to_add:
         k=k+i
    return HttpResponse(" Range addition numbers are  :"+str(k))

# Create your views here.
