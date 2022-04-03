# AssetRentalAPI  
  
Using Django and django-rest-framework 
  
> Written in  [StackEdit](https://stackedit.io/).  
  
  
# Index  
   
 1. Technologies  
 2. Setup  
 3. Usage  
 4. API short overview
 5. Design Diagram
 6. Spoilers

  
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

  <br><br>

## Models/Persistence Design Diagram
Please click the below diagram to view the interactive chart @ LucidCharts.com
[![models design at lucidcharts](https://user-images.githubusercontent.com/51651537/161448146-a4fc0fd9-462e-434b-9f21-ded8c7c358a8.png)](https://lucid.app/documents/embeddedchart/6406df98-dffa-4297-bbce-cd3bad194d15 "Diagram at LucidCharts")


 <br><br>

## Spoilers
![Screenshot 2022-04-03 at 21 22 44](https://user-images.githubusercontent.com/51651537/161444537-a41dca7b-6a8c-42ca-8c23-e4ccc14b0092.png)

 <br>


  
