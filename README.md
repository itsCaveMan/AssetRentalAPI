# AssetRentalAPI  
  
Using Django and django-rest-framework 
  
> Written in  [StackEdit](https://stackedit.io/).  
  
  
# Index  
  
 1. Introduction   
 2. Technologies  
 3. Setup  
 4. Usage  
 5. API short overview
  
<br>  
  
## Technologies  
  
 - Python 🐍 - 3.9  
 - Django 📄 - 4.03  
 - djangorestframework 🧩 - 3.13.1  
  
  
<br>  
  
## Setup  
  
1. Clone repository  
2. Create and activate env of choice  
3. `pip install -r requirements.txt`  
4. `cd AssetRentalAPI/AssetAPI`  
5. `python3 manage.py migrate`  
6. `python3 manage.py runserver`  
  
 <br>  
  
## Usage  
  
hit `127.0.0.1:8000` to be redirected to the documentation  
 <br>  
hit `127.0.0.1:8000/swagger` to overview API's  
  
  
## API Short Overview  
1. `api/v1/customer/` - customer CRUD   
2. `api/v1/personnel/` - personnel CRUD    
3. `api/v1/asset/` - asset CRUD  
4. `api/v1/fleetrental/` - CRUD of customer fleet rentals  
5. `api/v1/trip/` - CRUD of vehicle trips   
6. more details in `api/v1/docs/`  
  