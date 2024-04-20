from django.db import models
from django.utils import timezone

class Country(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'country'


class State(models.Model):

    id = models.BigAutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'state'


class City(models.Model):

    id = models.BigAutoField(primary_key=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'


# -------------------------------------------------------------------- Job Category --------#
class Job_category(models.Model):

    id = models.BigAutoField(primary_key=True)
    category_image = models.ImageField(upload_to='job', blank=True, null=True)
    job_category_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.job_category_name

    class Meta:
        db_table = 'job_category'

# -------------------------------------------------------------------- Company Details --------#

class Company_details(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_logo = models.ImageField(upload_to='company_logo', blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    email_address = models.EmailField(unique=True)
    job_role = models.ForeignKey(Job_category, on_delete=models.CASCADE, related_name='company_details_job_role', blank=True, null=True)
    url = models.URLField(unique=True)
    company_description = models.TextField()
    req_knowledge_skills_abilities = models.TextField()
    education_experience = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    vacancy = models.IntegerField(blank=True, null=True)
    JOB_VACANCY = (
        ('part time', 'Part Time'),
        ('full time', 'Full Time'),
    )
    job_nature = models.CharField(max_length=9, choices=JOB_VACANCY)
    salary_yearly_range = models.CharField(max_length=100, blank=True, null=True)
    last_date_apply_application = models.DateField()

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        # If you want to update the posted_date even when the object is updated
        self.posted_date = timezone.now()
        super(Company_details, self).save(*args, **kwargs)  # Call the superclass's save method

    class Meta:
        db_table = 'company_details'

class Job_apply(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    passed_out_year = models.CharField(max_length=30)
    skills = models.CharField(max_length=100)
    resume = models.FileField(upload_to='job_apply')
    posted_date = models.DateTimeField(auto_now_add=True)
    job_category = models.ForeignKey(Job_category, on_delete=models.CASCADE)
    company_details = models.ForeignKey(Company_details, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'job_apply'

