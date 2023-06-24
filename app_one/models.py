from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        x = User.objects.filter(email=postData['email'])    
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['fname']) < 3:
            errors["fname"] = "First Name should be at least 2 characters"
        if len(postData['lname']) < 3:
            errors["lname"] = "last Name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password description should be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors["confirm_password"] = "Password conformation didn't match"
        if  len(x)>0:
            errors['emaill'] = "Email Already Used!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class PieManager(models.Manager):
    def book_validator(self, postData):
        errors = {}


        if len(postData['pie_name']) < 1:
            errors["pie_name"] = "Name is required"
        if len(postData['filling']) < 1:
            errors["filling"] = "Fillings is required"
        if len(postData['crust']) < 1:
            errors["crust"] = "Crust is required"


        return errors

class Pie(models.Model):
    name = models.CharField(max_length=45)
    filling = models.CharField(max_length=45)
    crust = models.CharField(max_length=45)
    votes= models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    made_by = models.ForeignKey(User, related_name="pies", on_delete = models.CASCADE)
    users_who_voted= models.ManyToManyField(User, related_name="liked_pies")
    objects = PieManager()


def register(request):
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name = request.POST['fname'] ,last_name = request.POST['lname'] , email = request.POST['email'] , 
                        password= pw_hash )
    

def login(request):
    user = User.objects.get(email = request.POST['email'])
    if user :
        logged_user = user.email
    
    if bcrypt.checkpw(request.POST['password_email'].encode(), logged_user.password.encode()):
        request.sessuion['userid'] = logged_user.id



def get_specific_user(request):
    return User.objects.get(id=request.session['userid'])


def create_a_book(request):
    return Pie.objects.create(name=request.POST['pie_name'],filling=request.POST['filling'],crust=request.POST['crust'],made_by=User.objects.get(id =request.session['userid']))


def shows_pecificpie(num):
    return Pie.objects.get(id=num)

def update_pie(request):
    pie_to_update=Pie.objects.get(id=request.POST['hidden_id'])
    pie_to_update.name=request.POST['pie_name']
    pie_to_update.filling=request.POST['filling']
    pie_to_update.crust=request.POST['crust']
    pie_to_update.save()

def delete_piee(ip):
    pie_to_delete=Pie.objects.get(id=ip)
    pie_to_delete.delete()

def show_all_users():
    return User.objects.all()


def show_all_pies():
    return Pie.objects.all().order_by("-votes")

def show_specific_pie(ic):
    return Pie.objects.get(id=ic)

def vote_update_pie(request):
    piee_to_update=Pie.objects.get(id=request.POST['vote_id'])
    piee_to_update.votes= piee_to_update.votes+1
    piee_to_update.save()
    cc=Pie.objects.get(id=request.POST['vote_id'])
    user = User.objects.get(id=request.session['userid'])
    user.liked_pies.add(cc)
    

    
    



