from django.conf import settings
import json
import pymongo 
from bson import ObjectId 
from bson.json_util import dumps
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myclient["database"] 
cartdata = mydb['cartdata'] 
userdata=mydb['userdata']
mendata=mydb['proddata']
womendata=mydb['womenprod']
prevorders=mydb['prevorders']
# products = prdColl.find() 
# print([p for p in products])


DB = settings.DB

def writeDB(obj,loc,filename=DB):
    userdata.insert_one({'name':obj["name"],'email':obj["email"],'password':obj['password'],'mobile':obj["mobile"]})
    # with open(filename, 'r') as dbjson : 
    #     datadict= json.loads(dbjson.read()) 
    #     dbjson.close()
    #     temp=datadict['database'][loc]
    #     temp.append(obj)
    
    # with open(filename, 'w') as jsondb:
    #     json.dump(datadict, jsondb )
    #     jsondb.close()


def readDB(loc,filename=DB):
    #return userdata.find_one(['loc'])
    database
    with open(filename,'r') as dbjson:
        datadict=json.loads(dbjson.read())
        dbjson.close()
        temp=datadict['database'][loc]
        return temp

def findDB(userobj,filename=DB):
 
    return userdata.find_one({'email':userobj["email"],'password':userobj['password']})
    # with open(filename,'r') as dbd:
    #     dbdict=json.loads(dbd.read())
    #     dbd.close()
    #     j=0
    #     for i in range(len(dbdict['database']['userdata'])):
    #         if userobj['email']==dbdict['database']['userdata'][i]['email'] and userobj['password']==dbdict['database']['userdata'][i]['password']:
    #             return True 
    #         j+=1
    #     if j== len(dbdict['database']['userdata']):return False
            

def addcart(obj):
    #userdata.find_one
    e=mendata.find_one({'_id': ObjectId(obj["id"])})
    #a['_id'] = str(a['_id'])    
    #return a
    cartdata.insert_one({'email':obj['email'],'title':e["title"],'price':e["price"],'image':e["image"]}) 
    # a=mendata.find_one({'_id':obj['id']})  
    # b={}
    # c=list(a)
    # for i in c:
def addcartwomen(obj):
    #userdata.find_one
    e=womendata.find_one({'_id': ObjectId(obj["id"])})
    #a['_id'] = str(a['_id'])    
    #return a
    cartdata.insert_one({'email':obj['email'],'title':e["title"],'price':e["price"],'image':e["image"]}) 
             

        
def getfromcart(obj):
    returnData = []
    for i in cartdata.find({'email':obj['email']}):
        i['_id']=str(i['_id'])

        returnData.append(i)
    return returnData
   #return cartdata.find({'email':obj})
#    for i in d:
#         d['_id'] = str(d['_id']) 
#    b=list(a)
#    c={}
#    for i in b:
#        c.append(b)
#    return c 

    # for i in a:
    #     i['_id']=str(i['_id'])
    # b=list(a)
    # c={}
    # for j in b:
    #     c.append(j)
    # return c




    
    
    # b={}
    # c=list(a)
    # # i['_id'] = str(i['_id'])
    # for i in c:
    #     i['_id'] = str(i['_id'])
    # #    # str(cartdata['_id'])
    # # for i in a:
    # #     b.append(i)
 
    # d={}
    # for i in c:
    #     d['email']=str(i['email'])
    #     #b.append(d)
    #     d={}
    # return c
    
def ordernow(obj):
    cart_items=cartdata.find({'email':obj['email']})
    order={"items":[],"email":obj["email"]}
    
    for i in cart_items:
        #delete _id from here
        cartdata.delete_one({'_id': i['_id']}) 
        i['_id'] = str(i['_id'])
        order["items"].append(i) 
    prevorders.insert_one(order)
#delete items from cart

def orderhistory(obj):
    returnData = []
    for i in prevorders.find({'email':obj['email']}):
        returnData.append(i)
    return returnData

    # return [i for i in prevorders.find({'email': obj['email']})]

# //api ordernow,copy cart ,move to order
# //orderhistory returns from order

def menproducts():
    p=mendata.find()
    q=list(p)
    for a in q:
        a['_id'] = str(a['_id'])
    return q

def menproductinfo(obj):
    a=mendata.find_one({'_id': obj})
    a['_id'] = str(a['_id'])    
    return a



    # a=mendata.find_one({'_id': ObjectId(obj['_id'])})
    # a['_id'] = str(a['_id'])     {WORKING}
    # return a








    # p=mendata.find_one({'_id':obj['_id']})
    # q=list(p)
    # for a in q:
    #     a['_id'] = str(a['_id'])
    #     #a['_id'].encode('utf-8')
    # return q
    








    # p=mendata.find_one({'title':obj['title']})
    # q=list(p)
    # for a in q:
    #     a['_id'] = str(a['_id'])
    
    
    
    
    # try:
    #     print(q)
    #     return q
    # except KeyError:
    #      print ("error") 

def womenproducts():
    p=womendata.find()
    q=list(p)
    for a in q:
        a['_id'] = str(a['_id'])
    return q

def womenproductinfo(obj):
    a=womendata.find_one({'_id': obj})
    a['_id'] = str(a['_id'])    
    return a


def getprofiledetails(obj):
    a=userdata.find_one({'email':obj['email']})
    a['_id'] = str(a['_id'])    
    return a