import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from petzo_app.models import *


def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')


def login(request):
    return render(request,"admin/login.html")



def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    a=login_table.objects.filter(username=username,password=password)
    if a.exists():
        ab = login_table.objects.get(username=username, password=password)
        request.session['lid']=ab.id
        if ab.type=='admin':
            return HttpResponse('''<script>alert('login success');window.location='/adminhome'</script>''')
        elif  ab.type=='hospital':
            return HttpResponse('''<script>alert('login success');window.location='/hs_home'</script>''')
        elif  ab.type=='petshop':
            return HttpResponse('''<script>alert('login success');window.location='/petshop_home'</script>''')
        elif  ab.type=='user':
            return HttpResponse('''<script>alert('login success');window.location='/user_home'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid ');window.location='/'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid ');window.location='/'</script>''')

def view_vethostpital_search(request):

    n=request.POST['textfield']
    ob=hospital_table.objects.filter(name__istartswith=n)
    return render(request, "admin/accepted_vet_hospt.html", {'data':ob,"n":n})

def view_vethostpital(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    ob=hospital_table.objects.all()
    return render(request, "admin/accepted_vet_hospt.html", {'data':ob})

def vethostpital_block(request,id):
    a=login_table.objects.filter(id=id).update(type='blocked')

    return redirect('/view_vethostpital')

def vethostpital_unblock(request,id):
    a=login_table.objects.filter(id=id).update(type='hospital')
    return redirect('/view_vethostpital')




def hs_accept(request,id):
    a=login_table.objects.filter(id=id).update(type='hospital')
    return redirect('/view_hospital')



def hs_reject(request,id):
    a=login_table.objects.filter(id=id).update(type='pending')
    return redirect('/view_hospital')


def verifyhospital(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    return render(request,"admin/accepted_vet_hospt.html")



def sendreply(request):
    ob=complaints_table.objects.all()
    return render(request,"admin/send_reply.html",{'val':ob})



def viewpetshop(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    ob=petshop_table.objects.all()
    return render(request,'admin/verify_petshop.html',{'val':ob})


def verifypetshop(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    ob=petshop_table.objects.all()
    return render(request,"admin/verify_petshop.html",{"data":ob})


def accpet_petshop(request,id):
    a=login_table.objects.filter(id=id).update(type='petshop')
    return HttpResponse('''<script>alert('Approved');window.location='/verifypetshop'</script>''')
def reject_petshop(request,id):
    a=login_table.objects.filter(id=id).update(type='pending')
    return HttpResponse('''<script>alert('Rejected');window.location='/verifypetshop'</script>''')


def verifypetshop_search(request):

    n=request.POST['textfield']
    ob = petshop_table.objects.filter(name__istartswith=n)
    return render(request, "admin/verify_petshop.html",{'val':ob,"n":n})

def viewacceptedpetshop(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    ob= petshop_table.objects.filter(Q(LOGIN__type='petshop')|Q(LOGIN__type='Blocked'))
    return render(request,"admin/view accepted petshop.html",{'data':ob})


def block_shop(request,id):
    a=login_table.objects.filter(id=id).update(type='Blocked')
    return redirect('/viewacceptedpetshop')

def unblock_shop(request,id):
    a=login_table.objects.filter(id=id).update(type='petshop')
    return redirect('/viewacceptedpetshop')

def viewcomplaintandrating(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    ob = complaints_table.objects.all()
    return render(request,"admin/view_complaint&rating.html",{'data':ob})



def viewcomplaintandrating_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')
    f=request.POST['f']
    t=request.POST['t']
    ob = complaints_table.objects.filter(date__range=[f,t])
    return render(request,"admin/view_complaint&rating.html",{'data':ob,'f':f,'t':t})


def send_reply(request,id):
    a=complaints_table.objects.get(id=id)
    return render(request,'admin/send_reply.html',{'data':a})


def send_reply_post(request):
    id=request.POST['id']
    reply=request.POST['reply']

    a=complaints_table.objects.get(id=id)
    a.reply=reply
    a.save()
    return HttpResponse('''<script>alert('Replied');window.location='/viewcomplaintandrating'</script>''')


def viewpetshoprating(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    # ob=petshop_rating_table.objects.all()
    return render(request,"admin/view_petshop_rating.html",{'val':ob})


def viewuser(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    ob=user_table.objects.all()
    return render(request,"admin/view_user.html",{'val':ob})

def viewuser_search(request):
    n = request.POST['textfield']
    ob = user_table.objects.filter(name__istartswith=n)
    return render(request, "admin/view_user.html",{'val':ob,"n":n})

def adminhome(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    return render(request,"admin/index.html")



def view_hospital(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    a=hospital_table.objects.all()
    return render(request,'admin/verfy_vethosp.html',{'data':a})

def hospital_reg(request):
    if 'submit' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        district = request.POST['district']
        password = request.POST['password']

        aa=login_table.objects.filter(username=email)
        if aa.exists():
            return HttpResponse('''<script>alert('Already Taken');window.location='/hospital_reg'</script>''')

        a=login_table()
        a.username=email
        a.password=password
        a.type='pending'
        a.save()

        b=hospital_table()
        b.LOGIN=a
        b.name=name
        b.email=email
        b.phone=phone
        b.place=place
        b.post=post
        b.pin=pin
        b.district=district
        b.save()
        return HttpResponse('''<script>alert('Regiester');window.location='/'</script>''')
    return render(request,'hospital/register.html')


def hs_home(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    return render(request,'hospital/index.html')



def hospital_view_user(request):
    a=user_table.objects.all()
    return render(request,'hospital/view user.html',{'data':a})


def hsview_profile(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    a=hospital_table.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'hospital/view profile.html',{'hospital':a})


def hsedit_profile(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    a=hospital_table.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'hospital/edit profile.html',{'data':a})

def edit_profile_post(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    district = request.POST['district']
    id = request.POST['id']


    b=hospital_table.objects.get(id=id)

    if login_table.objects.filter(username=email).exclude(id=b.LOGIN.id).exists():
        return HttpResponse('''<script>alert('Email already taken');window.history.back();</script>''')

    b.name=name
    b.email=email
    b.phone=phone
    b.place=place
    b.post=post
    b.pin=pin
    b.district=district
    b.save()


    a=b.LOGIN
    a.username=email
    a.save()
    return HttpResponse('''<script>alert('Updated');window.location='/hsview_profile'</script>''')


def hs_view_rating(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    a=rating_table.objects.filter(HOSPITAL__LOGIN_id=request.session['lid'])
    print(a,'ratings=================')
    return render(request,'hospital/view hospital rating.html',{'data':a})


def add_vaccine(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    if 'submit' in request.POST:
        vaccinename=request.POST['vaccinename']
        details=request.POST['details']
        dateupto=request.POST['dateupto']

        a=vaccinedetails_table()
        a.uploadeddate=datetime.datetime.now().today().date()
        a.dateupto=dateupto
        a.details=details
        a.vaccinename=vaccinename
        a.HOSPITAL=hospital_table.objects.get(LOGIN_id=request.session['lid'])
        a.save()
        return HttpResponse('''<script>alert('Added');window.location='/add_vaccine'</script>''')

    return render(request,'hospital/add vaccine.html')


def view_vaccines(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    a=vaccinedetails_table.objects.filter(HOSPITAL__LOGIN_id=request.session['lid']).order_by('-id')
    return render(request,'hospital/view vaccine details.html',{'data':a})


def view_vaccines_post(request):
    f=request.POST['f']
    t=request.POST['t']
    a=vaccinedetails_table.objects.filter(HOSPITAL__LOGIN_id=request.session['lid'],uploadeddate__range=[f,t]).order_by('-id')
    return render(request,'hospital/view vaccine details.html',{'data':a,'f':f,'t':t})

def delete_vaccine(request,id):
    a=vaccinedetails_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script>alert('Deleted');window.location='/view_vaccines'</script>''')


def edit_vaccine(request,id):
    a=vaccinedetails_table.objects.get(id=id)
    return render(request,'hospital/edit vaccine.html',{'data':a})

def edit_vaccine_post(request):
    id=request.POST['id']
    vaccinename = request.POST['vaccinename']
    details = request.POST['details']
    dateupto = request.POST['dateupto']

    a = vaccinedetails_table.objects.get(id=id)
    a.dateupto = dateupto
    a.details = details
    a.vaccinename = vaccinename
    a.HOSPITAL = hospital_table.objects.get(LOGIN_id=request.session['lid'])
    a.save()
    return HttpResponse('''<script>alert('Updated');window.location='/view_vaccines'</script>''')


def shop_register(request):
    if 'submit' in request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        place=request.POST['place']
        pin=request.POST['pin']
        post=request.POST['post']
        district=request.POST['district']
        license=request.POST['license']
        password=request.POST['password']
        c=login_table.objects.filter(username=email)
        if c.exists():
            return HttpResponse('''<script>alert('Already taken');window.location='/shop_register'</script>''')

        a=login_table()
        a.username=email
        a.password=password
        a.type='pending'
        a.save()


        b=petshop_table()
        b.LOGIN=a
        b.name=name
        b.phone=phone
        b.email=email
        b.place=place
        b.pin=pin
        b.post=post
        b.district=district
        b.license=license
        b.save()
        return HttpResponse('''<script>alert('Registerd');window.location='/'</script>''')

    return render(request,'shop/register.html')


def petshop_home(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    return render(request,'shop/index.html')


def shopview_profile(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    a=petshop_table.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'shop/view profile.html',{'hospital':a})


def shopedit_profile(request):
    a=petshop_table.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'shop/edit profile.html',{'data':a})

def shopedit_profile_post(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    district = request.POST['district']
    licence = request.POST['licence']
    id = request.POST['id']


    b=petshop_table.objects.get(id=id)

    # if login_table.objects.filter(username=email).exclude(id=b.LOGIN.id).exists():
    #     return HttpResponse('''<script>alert('Email already taken');window.history.back();</script>''')

    b.name=name
    b.email=email
    b.phone=phone
    b.place=place
    b.post=post
    b.pin=pin
    b.licence=licence
    b.district=district
    b.save()


    a=b.LOGIN
    a.username=email
    a.save()
    return HttpResponse('''<script>alert('Updated');window.location='/shopview_profile'</script>''')


def add_service(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    if 'submit' in request.POST:
        servicename=request.POST['servicename']
        details=request.POST['details']

        a=services_table()
        a.details=details
        a.servicename=servicename
        a.PETSHOP=petshop_table.objects.get(LOGIN_id=request.session['lid'])
        a.save()
        return HttpResponse('''<script>alert('Added');window.location='/add_service'</script>''')
    return render(request,'shop/add services.html')

def shop_view_service(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    a=services_table.objects.filter(PETSHOP__LOGIN_id=request.session['lid']).order_by('-id')
    return render(request,'shop/view services.html',{'data':a})

def delete_service(request,id):
    a=services_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script>alert('Deleted');window.location='/shop_view_service'</script>''')

def edit_service(request,id):
    a=services_table.objects.get(id=id)
    return render(request,'shop/edit service.html',{'data':a})


def edit_service_post(request):
    servicename = request.POST['servicename']
    details = request.POST['details']
    id = request.POST['id']

    a = services_table.objects.get(id=id)
    a.details = details
    a.servicename = servicename
    a.PETSHOP = petshop_table.objects.get(LOGIN_id=request.session['lid'])
    a.save()
    return HttpResponse('''<script>alert('Updated');window.location='/shop_view_service'</script>''')


def view_request(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    a=request_table.objects.filter(SERVICES_id=id)
    return render(request,'shop/view request.html',{'data':a})


from django.shortcuts import render, redirect

def add_pet(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    if request.method == 'POST':
        petname = request.POST.get('petname')
        image = request.FILES.get('image')
        pet_type = request.POST.get('type')
        age = request.POST.get('age')
        price = request.POST.get('price')

        fs=FileSystemStorage()
        date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.jpg'
        fs.save(date,image)
        path=fs.url(date)

        # Create a new pet entry
        pet = pet_table(
            SHOP=petshop_table.objects.get(LOGIN_id=request.session['lid']),
            petname=petname,
            image=path,
            type=pet_type,
            age=age,
            price=price
        )
        pet.save()

        return HttpResponse('''<script>alert('Added');window.location='/add_pet'</script>''')

    return render(request, 'shop/add pet.html', )


def shop_view_pet(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    a=pet_table.objects.filter(SHOP__LOGIN_id=request.session['lid'])
    return render(request,'shop/view pet.html',{'data':a})

def delete_pet(request,id):
    a=pet_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script>alert('Deleted');window.location='/shop_view_pet'</script>''')

def edit_pet(request,id):
    a=pet_table.objects.get(id=id)
    return render(request,'shop/edit pet.html',{'data':a})


from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import pet_table, petshop_table
import datetime

def edit_pet_post(request):
    # Retrieve form data
    id = request.POST.get('id')
    petname = request.POST.get('petname')
    image = request.FILES.get('image')
    pet_type = request.POST.get('type')
    age = request.POST.get('age')
    price = request.POST.get('price')

    if image:
        fs = FileSystemStorage()

        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        fs.save(date, image)
        path = fs.url(date)  # Get the URL of the saved image
    else:
        path = pet_table.objects.get(id=id).image  # Get current image URL if not updated

    shop = petshop_table.objects.get(LOGIN_id=request.session['lid'])

    # Update the pet record
    pet = pet_table.objects.get(id=id)  # Retrieve the existing pet
    pet.SHOP = shop
    pet.petname = petname
    pet.image = path
    pet.type = pet_type
    pet.age = age
    pet.price = price

    # Save the updated pet record
    pet.save()

    # Redirect to the pet listing page or show success message
    return redirect('/shop_view_pet')  # Replace with the correct URL you want to redirect to


def update_service_request_status(request,id):
    a=request_table.objects.get(id=id)

    return render(request,'shop/update service request.html',{'data':a})

def update_service_request_status_post(request):
    id = request.POST['id']
    status = request.POST['status']
    a = request_table.objects.get(id=id)
    a.status = status
    a.save()
    return HttpResponse('''<script>alert('Updated');window.location='/petshop_home'</script>''')


def accept_sevice_request(request,id):
    a=request_table.objects.filter(id=id).update(status='Approved')
    return HttpResponse('''<script>alert('Approved');window.location='/petshop_home'</script>''')

def reject_sevice_request(request,id):
    a=request_table.objects.filter(id=id).update(status='Rejected')
    return HttpResponse('''<script>alert('Rejected');window.location='/petshop_home'</script>''')


def shop_view_request(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    a=petshoprequest_table.objects.filter(PETSHOP__LOGIN_id=request.session['lid'])
    return render(request,'shop/view shop request.html',{'data':a})


def shop_view_user(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Logouted');window.location='/'</script>''')

    a=user_table.objects.all()
    return render(request,'shop/view user.html',{'data':a})



def shop_view_vaccine_request(request,id):
    a=vaccine_request_table.objects.filter(VACCINE_id=id)
    print(a)
    return render(request,'shop/view vaccine_request.html',{'data':a})


def accept_vaccine_request(request,id):
    a=vaccine_request_table.objects.filter(id=id).update(status='Approved')
    return HttpResponse('''<script>alert('Approved');window.location='/hs_home'</script>''')

def reject_vaccine_request(request,id):
    a=vaccine_request_table.objects.filter(id=id).update(status='Rejected')
    return HttpResponse('''<script>alert('Rejected');window.location='/hs_home'</script>''')



def accept_request(request,id):
    a=petshoprequest_table.objects.filter(id=id).update(status='Approved')
    return HttpResponse('''<script>alert('Approved');window.location='/shop_view_request'</script>''')
def reject_request(request,id):
    a=petshoprequest_table.objects.filter(id=id).update(status='Rejected')
    return HttpResponse('''<script>alert('Rejected');window.location='/shop_view_request'</script>''')


def update_status(request,id):
    a=petshoprequest_table.objects.get(id=id)
    return render(request,'shop/update pt status.html',{'data':a})

def update_status_post(request):
    id=request.POST['id']
    status=request.POST['status']

    a=petshoprequest_table.objects.get(id=id)
    a.status=status
    a.save()
    return HttpResponse('''<script>alert('updated');window.location='/shop_view_request'</script>''')


# def shop_chat_to_user(request, id):
#     request.session["userid"] = id
#
#
#     qry = user_table.objects.get(LOGIN=id)
#     print(qry.LOGIN_id,'login----------')
#
#     # return render(request, "shop/add pet.html", { 'name': qry.name, 'toid': id})
#     return render(request, "shop/Chat.html", { 'name': qry.name, 'toid': id})




def shop_chat_to_user(request, id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = user_table.objects.get(LOGIN_id=cid)
    print(qry.LOGIN_id,'login----------')

    return render(request, "shop/Chat.html", { 'name': qry.name, 'toid': cid})
    # return render(request, "shop/Chat.html", {'photo': qry.image, 'name': qry.name, 'toid': cid})


def chat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = user_table.objects.get(LOGIN_id=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid)).order_by('id')
    l = []
    print(qry.name,'userssssssssss')

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TOID_id, "date": i.date, "from": i.FROMID_id})

    # return JsonResponse({'photo': qry.image, "data": l, 'name': qry.name, 'toid': request.session["userid"]})
    return JsonResponse({ "data": l, 'name': qry.name, 'toid': request.session["userid"]})



def chat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TOID_id = toid
    chatobt.FROMID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})







def flutter_login(request):
    username = request.POST['username']
    password = request.POST['psw']
    a = login_table.objects.filter(username=username, password=password)
    if a.exists():
        b = login_table.objects.get(username=username, password=password)
        if b.type == 'user':
            lid=b.id
            var=user_table.objects.get(LOGIN_id=str(lid))
            # name=var.name
            # photo=var.photo
            return JsonResponse({"status": "ok", "lid":str(lid),'type':'user'})


        else:
            return JsonResponse({"status": "no"})


    else:

        return JsonResponse({"status":"no"})


def user_reg(request):
    password=request.POST['password']
    name=request.POST['name']
    place=request.POST['place']
    # post=request.POST['post']
    phone=request.POST['phone']
    email=request.POST['email']



    aa=login_table.objects.filter(username=email)
    if aa.exists():
        return JsonResponse({"status": "not ok"})

    lobj = login_table()
    lobj.username = email
    lobj.password = password
    lobj.type = 'user'
    lobj.save()


    f = user_table()
    f.name = name
    f.place = place
    f.phone = phone
    f.email = email
    f.LOGIN = lobj
    f.save()

    return JsonResponse({"status": "ok"})


def user_profile(request):
    lid=request.POST['lid']
    a=user_table.objects.get(LOGIN_id=lid)
    print(a.phone)
    return JsonResponse({'status':'ok','name':a.name,'email':a.email,'phone':str(a.phone),'place':a.place})


def edit_profile(request):
    lid=request.POST['lid']
    name = request.POST['name']
    place = request.POST['place']
    # post=request.POST['post']
    phone = request.POST['phone']
    email = request.POST['email']
    f=user_table.objects.get(LOGIN_id=lid)
    f.name = name
    f.place = place
    f.phone = phone
    f.email = email
    f.save()

    return JsonResponse({"status": "ok"})


def send_complaint(request):
    lid=request.POST['lid']
    complaint=request.POST['complaint']

    a=complaints_table()
    a.USER=user_table.objects.get(LOGIN_id=lid)
    a.complaints=complaint
    a.date=datetime.datetime.now().today().date()
    a.reply='pending'
    a.save()
    return JsonResponse({"status": "ok"})


def user_view_reply(request):
    lid=request.POST['lid']
    a=complaints_table.objects.filter(USER__LOGIN_id=lid).order_by('-id')
    l=[]
    for i in a:
        l.append({'id': i.id,
                  'complaint': i.complaints,
                  'reply': i.reply,
                  'date': str(i.date) })
    return JsonResponse({"status": "ok",'data':l})


def user_view_pets(request):
    a=pet_table.objects.all()
    l=[]
    for i in a:
        l.append({'id': i.id,
                  'petname': i.petname,
                  'image': i.image,
                  'type': i.type,
                  'age': i.age,
                  'price': i.price,
                  })
    print(l)
    return JsonResponse({"status": "ok",'data':l})



def user_view_vaccine(request):
    a=vaccinedetails_table.objects.all()
    l=[]
    for i in a:
        l.append({
            'id':i.id,'HOSPITAL':i.HOSPITAL.name,'vaccinename':i.vaccinename,
                  'details':i.details,'dateupto':str(i.dateupto),'uploadeddate':str(i.uploadeddate)

                  })
    print(l)
    return JsonResponse({"status": "ok", 'data': l})



def user_vaccine_request(request):
    vid=request.POST['vid']
    a=request_table


def user_view_hospital(request):
    a=hospital_table.objects.all()
    l=[]
    for i in a:
        l.append({
            'id':i.id,'name':i.name,
                  'place':i.place,'district':i.district,'email':i.email,'LOGIN':str(i.LOGIN.id)

                  })
    print(l)
    return JsonResponse({"status": "ok", 'data': l})


def send_hs_rating(request):
    hid=request.POST['hid']
    lid=request.POST['lid']
    rating=request.POST['rating']
    feedback=request.POST['feedback']
    a=rating_table()
    a.feedback=feedback
    a.rating=rating
    a.date=datetime.datetime.now().today().date()
    a.USER=user_table.objects.get(LOGIN_id=lid)
    a.HOSPITAL=hospital_table.objects.get(id=hid)
    a.save()
    return JsonResponse({"status": "ok"})


def user_view_shop(request):
    a=petshop_table.objects.filter(LOGIN__type='petshop')
    l=[]
    for i in a:
        l.append({
            'id':i.id,'name':i.name,
                  'place':i.place,'district':i.district,'email':i.email,'LOGIN':str(i.LOGIN.id)

                  })
    print(l)
    return JsonResponse({"status": "ok", 'data': l})

def sent_v_request(request):
    hid=request.POST['vid']
    lid=request.POST['lid']
    request=request.POST['request']

    a=vaccine_request_table()
    a.request=request
    a.status='Requested'
    a.date=datetime.datetime.now().today().date()
    a.USER=user_table.objects.get(LOGIN_id=lid)
    a.VACCINE=vaccinedetails_table.objects.get(id=hid)
    a.save()
    return JsonResponse({"status": "ok"})


def user_view_vaccine_status(request):
    lid=request.POST['lid']
    a=vaccine_request_table.objects.filter(USER__LOGIN_id=lid).order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'VACCINE':i.VACCINE.vaccinename,
                  'HOSPITAL':i.VACCINE.HOSPITAL.name,
                  'status':i.status,
                  'request':i.request,
                  'date':str(i.date),

                  })
    print(l)
    return JsonResponse({"status": "ok", 'data': l})


def user_send_petcare_request(request):
    pid=request.POST['pid']
    lid=request.POST['lid']
    pettype=request.POST['pettype']
    age=request.POST['age']
    details=request.POST['details']

    a=petshoprequest_table()
    a.pettype=pettype
    a.USER=user_table.objects.get(LOGIN_id=lid)
    a.date=datetime.datetime.now().today().date()
    a.details=details
    a.status='Requested'
    a.age=age
    a.PETSHOP=petshop_table.objects.get(id=pid)
    a.save()
    return JsonResponse({"status": "ok"})

def user_view_petcare_request(request):
    lid=request.POST['lid']
    a=petshoprequest_table.objects.filter(USER__LOGIN_id=lid).order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'pettype':i.pettype,
                  'age':i.age,
                  'status':i.status,
                  'details':i.details,
                  'date':str(i.date),

                  })
    print(l)
    return JsonResponse({"status": "ok", 'data': l})




from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
import datetime

# def add_post(request):
#     files = request.FILES['files']
#     details = request.POST['details']
#     name = request.POST['name']
#     lid = request.POST['lid']
#
#     fs = FileSystemStorage()
#
#     if 'image' in files.content_type:  # If the file is a video
#         d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
#     else:
#         d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.mp4'
#
#     fs.save(d, files)
#     path = fs.url(d)
#
#     # Save post details to the database
#     a = post_table()
#     a.date = datetime.datetime.now().today().date()
#     a.file = path
#     a.details = details
#     a.name = name
#     a.USER = user_table.objects.get(LOGIN_id=lid)
#     a.save()
#
#     return JsonResponse({'status': 'ok', 'message': 'Post added successfully!'})

from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
import datetime
from .models import post_table, user_table
import mimetypes

def add_post(request):
    files = request.FILES['files']
    details = request.POST['details']
    name = request.POST['name']
    lid = request.POST['lid']

    fs = FileSystemStorage()

    file_extension = None
    if 'application/octet-stream' in files.content_type:
        file_name = files.name
        file_extension = mimetypes.guess_type(file_name)[0]

        if file_extension is None:
            # If we can't guess, return an error
            return JsonResponse({'status': 'error', 'message': 'Unable to determine file type. Please upload a valid image or video.'})

        # Set file extension to mime type's extension (e.g., image/jpeg -> .jpg)
        if 'image' in file_extension:
            file_extension = '.jpg'
        elif 'video' in file_extension:
            file_extension = '.mp4'
        else:
            # If it's neither an image nor a video, return an error
            return JsonResponse({'status': 'error', 'message': 'Invalid file type. Only images and videos are allowed.'})

    # If the content type is correctly identified, use it directly
    elif 'image' in files.content_type:
        file_extension = '.jpg'
    elif 'video' in files.content_type:
        file_extension = '.mp4'

    if not file_extension:
        return JsonResponse({'status': 'error', 'message': 'Invalid file type. Only images and videos are allowed.'})

    # Generate a unique filename based on the current date and time
    filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + file_extension

    # Save the file to the filesystem
    fs.save(filename, files)
    file_path = fs.url(filename)

    # Create a new post and save it to the database
    try:
        post = post_table()
        post.date = datetime.datetime.now().today().date()
        post.file = file_path
        post.details = details
        post.name = name
        post.USER = user_table.objects.get(LOGIN_id=lid)  # Assuming lid is a valid user ID
        post.save()

        # Return success response
        return JsonResponse({'status': 'ok', 'message': 'Post added successfully!'})

    except user_table.DoesNotExist:
        # If the user with the given lid doesn't exist, return an error response
        return JsonResponse({'status': 'error', 'message': 'User not found for the given lid.'})

    except Exception as e:
        # Catch any other exceptions and return an error message
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {str(e)}'})






def user_view_post(request):
    a=post_table.objects.all().order_by('-id')
    l=[]
    for i in a:
        l.append({'id':i.id,
                  'USER':i.USER.name,
                  'file':i.file,
                  'details':i.details,
                  'name':i.name,
                  'date':str(i.date),

                  })
    print(l)
    return JsonResponse({"status": "ok", 'data': l})


def user_send_comment(request):
    pid=request.POST['pid']
    lid=request.POST['lid']
    comment=request.POST['comment']
    a=comment_table()
    a.POST=post_table.objects.get(id=pid)
    a.USER=user_table.objects.get(LOGIN_id=lid)
    a.date = datetime.datetime.now().today().date()
    a.comment=comment
    a.save()
    return JsonResponse({"status": "ok", })



def user_view_comment(request):
    pid=request.POST['pid']
    a=comment_table.objects.filter(POST_id=pid).order_by('-id')
    l=[]
    for i in a:
        l.append({'id': i.id,
                  'USER': i.USER.name,
                  'comment': i.comment,

                  'date': str(i.date),

                  })
    print(l)
    return JsonResponse({"status": "ok", 'data': l})



def  user_view_services(request):
    lid=request.POST['pid']
    a=services_table.objects.filter(PETSHOP_id=lid)
    l=[]
    for i in a:
        l.append({'id':i.id,'servicename':i.servicename,'details':i.details})
    print(l)
    return JsonResponse({"status": "ok", 'data': l})


# def user_send_service_request(request):
#     lid=request.POST['lid']
#     sid=request.POST['sid']
#     request=request.POST['request']
#     a=request_table()
#     a.USER=user_table.objects.get(LOGIN_id=lid)
#     a.SERVICES=services_table.objects.get(id=sid)
#     a.date=datetime.datetime.now().today().date()
#     a.request=request
#     a.status='Requested'
#     a.save()
#     return JsonResponse({"status": "ok", })


from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import datetime


def user_send_service_request(request):
    try:
        # Ensure the inputs are integers
        lid = int(request.POST['lid'])
        sid = int(request.POST['sid'])
        service_request = request.POST['request']

        # Get the user and service objects
        user = user_table.objects.get(LOGIN_id=lid)
        service = services_table.objects.get(id=sid)

        # Check if a request already exists for today
        today = datetime.datetime.now().date()
        existing_request = request_table.objects.filter(USER=user, SERVICES=service, date=today).exists()

        if existing_request:
            return JsonResponse({"status": "error", "message": "You can only send one request per day."})

        # Create and save the new request
        a = request_table()
        a.USER = user
        a.SERVICES = service
        a.date = today
        a.request = service_request
        a.status = 'Requested'
        a.save()

        return JsonResponse({"status": "ok"})
    except ValueError as ve:
        return JsonResponse({"status": "error", "message": f"Invalid ID value: {ve}"})
    except ObjectDoesNotExist as ode:
        return JsonResponse({"status": "error", "message": str(ode)})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})


def user_view_service_request_status(request):
    lid=request.POST['lid']
    a=request_table.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in a:
        l.append({"id":i.id,
                  'SERVICES':i.SERVICES.servicename,
                  'SHOP':i.SERVICES.PETSHOP.name,
                  'date':str(i.date),'request':i.request,'status':i.status

                  })
    print(l)
    return JsonResponse({"status": "ok", 'data': l})




def user_viewchat(request):
    fromid = request.POST["from_id"]
    toid = request.POST["to_id"]

    # Filter and sort the queryset by date and time in ascending order
    res = Chat.objects.filter(Q(FROMID=fromid, TOID=toid) | Q(FROMID=toid, TOID=fromid)).order_by('id')

    l = []

    for i in res:
        l.append({
            "id": i.id,
            "msg": i.message,
            "from": i.FROMID.id,  # Convert to primary key
            "date": i.date.strftime('%Y-%m-%d %H:%M:%S'),  # Format date as a string
            "to": i.TOID.id  # Convert to primary key
        })
        print(l)

    return JsonResponse({"status": "ok", 'data': l})




def User_sendchat(request):
    FROM_id=request.POST['from_id']
    TOID_id=request.POST['to_id']
    print(FROM_id)
    print(TOID_id)
    msg=request.POST['message']

    from  datetime import datetime
    c=Chat()
    c.FROMID_id=FROM_id
    c.TOID_id=TOID_id
    c.message=msg
    c.date=datetime.now()
    c.save()
    return JsonResponse({'status':"ok"})



def user_add_pet(request):
    lid=request.POST['lid']
    petname = request.POST['petname']
    image = request.FILES['image']
    pet_type = request.POST['pet_type']
    age = request.POST['age']
    price = request.POST['price']

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
    fs.save(date, image)
    path = fs.url(date)
    a=user_pet_table()
    a.USER=user_table.objects.get(LOGIN_id=lid)
    a.price=price
    a.petname=petname
    a.type=pet_type
    a.image=path
    a.age=age
    a.save()
    return JsonResponse({'status':"ok"})


def user_view_user_pets(request):
    a=user_pet_table.objects.all().order_by('-id')
    l = []
    for i in a:
        l.append({"id": i.id,
                  'USER': i.USER.name,
                  'petname': i.petname,
                  'image': i.image,
                  'type': i.type,
                  'age': str(i.age),
                  'price': str(i.price),

                  })
    print(l)
    return JsonResponse({"status": "ok", 'data': l})




def hospital_chat_to_user(request, id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = user_table.objects.get(LOGIN_id=cid)
    print(qry.LOGIN_id,'login----------')

    return render(request, "hospital/Chat.html", { 'name': qry.name, 'toid': cid})
    # return render(request, "shop/Chat.html", {'photo': qry.image, 'name': qry.name, 'toid': cid})


def hs_chat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = user_table.objects.get(LOGIN_id=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid)).order_by('id')
    l = []
    print(qry.name,'userssssssssss')

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TOID_id, "date": i.date, "from": i.FROMID_id})

    # return JsonResponse({'photo': qry.image, "data": l, 'name': qry.name, 'toid': request.session["userid"]})
    return JsonResponse({ "data": l, 'name': qry.name, 'toid': request.session["userid"]})



def hs_chat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TOID_id = toid
    chatobt.FROMID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})



def user_viewchat_to_hs(request):
    fromid = request.POST["from_id"]
    toid = request.POST["to_id"]

    # Filter and sort the queryset by date and time in ascending order
    res = Chat.objects.filter(Q(FROMID=fromid, TOID=toid) | Q(FROMID=toid, TOID=fromid)).order_by('id')

    l = []

    for i in res:
        l.append({
            "id": i.id,
            "msg": i.message,
            "from": i.FROMID.id,  # Convert to primary key
            "date": i.date.strftime('%Y-%m-%d %H:%M:%S'),  # Format date as a string
            "to": i.TOID.id  # Convert to primary key
        })
        print(l)

    return JsonResponse({"status": "ok", 'data': l})


def hs_chat_User_sendchat(request):
    FROM_id=request.POST['from_id']
    TOID_id=request.POST['to_id']
    print(FROM_id)
    print(TOID_id)
    msg=request.POST['message']

    from  datetime import datetime
    c=Chat()
    c.FROMID_id=FROM_id
    c.TOID_id=TOID_id
    c.message=msg
    c.date=datetime.now()
    c.save()
    return JsonResponse({'status':"ok"})



def hs_add_tips(request):
    if 'submit' in request.POST:
        tips=request.POST['tips']
        details=request.POST['details']
        pet_type=request.POST['pet_type']
        age=request.POST['age']

        a=tips_table()
        a.HOSPITAL=hospital_table.objects.get(LOGIN_id=request.session['lid'])
        a.date=datetime.datetime.now().today().date()
        a.tips=tips
        a.details=details
        a.pet_type=pet_type
        a.age=age
        a.save()
        return HttpResponse('''<script>alert('Added');window.location='/hs_add_tips'</script>''')
    return render(request,'hospital/add tips.html')

def delete_tips(request,id):
    a=tips_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script>alert('Deleted');window.location='/hs_view_tips'</script>''')

def hs_view_tips(request):
    a=tips_table.objects.filter(HOSPITAL__LOGIN_id=request.session['lid'])
    return render(request,'hospital/view tips.html',{'data':a})



def user_view_tips(request):
    a=tips_table.objects.all().order_by('-id')
    l=[]

    for i in a:
        l.append({'id':i.id,'HOSPITAL':i.HOSPITAL.name,'date':str(i.date),
                  'tips':i.tips,
                  'details':i.details,
                  'pet_type':i.pet_type,
                  'age':i.age,
                  })
    print(l)

    return JsonResponse({"status": "ok", 'data': l})

