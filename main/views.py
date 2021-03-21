from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import json
import pymongo 
from bson import ObjectId 
from db import writeDB, readDB, findDB,addcart,addcartwomen,getfromcart,ordernow,menproducts,menproductinfo,womenproducts,womenproductinfo,getprofiledetails

DB=settings.DB
# Create your views here.
def register(request):
    if request.method =="GET":
        return HttpResponse("This is Registration api,use POST Method")


    
    elif request.method =="POST":
        data_obj=json.loads(request.body)
        #if data_obj['add']=='true':
        user_obj=data_obj['data']
        if not findDB(user_obj):
            writeDB(obj=user_obj,loc='userdata')
        if findDB(user_obj):
            return JsonResponse({"registrationStatus":"registered Successfully"})
        else:return JsonResponse({"registrationStatus":"registration failed,Please try again"})

    else:return HttpResponse("<h1>Invalid</h1>")

def login(request):

    if request.method == "POST":
        inobj=json.loads(request.body)
        #if inobj['add']=='false':
            
        if findDB(inobj['data']):
            return JsonResponse({"loginStatus":True})
        else:return JsonResponse({"loginStatus":False})
        #else:return JsonResponse({"loginStatus":False})
        

    elif request.method =="GET":
        return HttpResponse("This login api,use POST Method")

    else:return HttpResponse("<h1>Invalid</h1>")


def cart(request):
    if request.method== "POST":
        cartobj=json.loads(request.body)
        addcart(cartobj)
        return JsonResponse({"added":True})

def cartwomen(request):
    if request.method== "POST":
        cartobj=json.loads(request.body)
        addcartwomen(cartobj)
        return JsonResponse({"added":True})

def cartcontent(request):
    if request.method== "POST":
        cartobj=json.loads(request.body)
        return  JsonResponse(getfromcart(cartobj),safe=False)
        
def order(request):
    print(request.method)
    if  request.method=="POST":
        obj=json.loads(request.body)
        ordernow(obj)
        return JsonResponse({"status":True})
    

def productmen(request):
    if request.method=="GET":
        # obj=json.loads(request.body)
        menproducts()
        return JsonResponse(menproducts(),safe=False)


def mendetails(request):
    if request.method=="POST":
        obj=(json.loads(request.body))
        # _id=ObjectId(obj['_id'])
        k=menproductinfo(ObjectId(obj['myid']))
        return JsonResponse(k,safe=False)

def productwomen(request):
    if request.method=="GET":
        # obj=json.loads(request.body)
        womenproducts()
        return JsonResponse(womenproducts(),safe=False)

def womendetails(request):
    if request.method=="POST":
        obj=(json.loads(request.body))
        # _id=ObjectId(obj['_id'])
        k=womenproductinfo(ObjectId(obj['myid']))
        return JsonResponse(k,safe=False)

def profiledetails(request):
    if request.method=="POST":
        obj=(json.loads(request.body))   
        getprofiledetails(obj)
        return JsonResponse(getprofiledetails(obj),safe=False)