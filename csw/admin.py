from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Person
from .models import Work_contact
from .models import  education_and_training
from .models import pst_five_work
from .models import character_ref
from .models import practise_outside
from .models import rivate_practice
from .models import Contact
# from .models import Person

admin.site.register(Person)
admin.site.register(Work_contact)
admin.site.register( education_and_training)
admin.site.register(pst_five_work)
admin.site.register(character_ref)
admin.site.register(practise_outside)
admin.site.register(rivate_practice)
admin.site.register(Contact)
# admin.site.register(Person)
# class PersonAdmin(ImportExportModelAdmin):
#     list_display = ('name', 'email', 'location')
