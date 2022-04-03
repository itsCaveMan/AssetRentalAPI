from django.db import models


# ==============   Models   ==============
class BaseModel(models.Model):
    created_on_utc = models.DateTimeField(auto_now_add=True, editable=False) # set to now on record creation, never changed
    last_modified_utc = models.DateTimeField(auto_now=True,) # set to now on creation, re-set on each update
    active = models.BooleanField(default=True)
    class Meta:
        abstract = True

DRIVER = 'DRIVER'
STAFF = 'STAFF'
EXECUTIVE = 'EXECUTIVE'
UNDEFINED_ROLE = 'UNDEFINED_ROLE'
PERSONNEL_ROLE_CHOICES = (
    (DRIVER , 'Driver role'),
    (STAFF , 'Staff related role'),
    (EXECUTIVE , 'Executive related role'),
    (UNDEFINED_ROLE , 'Undefined personnel role'),
)

EDUCATION_LOWER = 'EDUCATION_LOWER'                 # primary school
EDUCATION_HIGHER = 'EDUCATION_HIGHER'               # high school
EDUCATION_TERTIARY = 'EDUCATION_TERTIARY'           # university associates
EDUCATION_DEGREE = 'EDUCATION_DEGREE'               # university undergraduate
EDUCATION_MASTER = 'EDUCATION_MASTER'               # university postgraduate
EDUCATION_DOCTORATE = 'EDUCATION_DOCTORATE'         # university docterate
TRAINING_CERTIFICATION = 'TRAINING_CERTIFICATION'   # training course certificate
UNDEFINED_LEVEL = 'UNDEFINED_LEVEL'                 # undefined
QUALIFICATION_LEVEL_CHOICES = (
    (EDUCATION_LOWER, 'EDUCATION_LOWER'),
    (EDUCATION_HIGHER, 'EDUCATION_HIGHER'),
    (EDUCATION_TERTIARY, 'EDUCATION_TERTIARY'),
    (TRAINING_CERTIFICATION, 'TRAINING_CERTIFICATION'),
    (UNDEFINED_LEVEL, 'UNDEFINED_LEVEL'),
)

