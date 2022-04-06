from django.db import models
from django.utils.text import slugify

# Create your models here.
class Project(models.Model):
    # project status, default value is submitted, professor role can change status, organisation can only edit
    SUBMITTED = 'Submitted'
    # project status 'admitted' means that project can be seen globally and can be voted on by students
    ACCEPTED = 'Accepted'
    # project denied means that project is not fitting for the service learning course
    DENIED = 'Denied'
    # project on hold means that project organisation maybe needs to add in additional information
    ON_HOLD = 'On Hold'
    
    PROJECT_STATUS_CHOICES = [
        (SUBMITTED, 'Eingereicht'),
        (ACCEPTED, 'Akzeptiert'),
        (DENIED, 'Abgelehnt'),
        (ON_HOLD, 'Im Wartezustand')
    ]

    title = models.CharField(max_length=120)
    organisation = models.CharField(max_length=120, default="")
    description = models.TextField()
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(max_length=128, null=True)
    status = models.CharField(
        max_length=128,
        choices=PROJECT_STATUS_CHOICES, 
        default=SUBMITTED)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title