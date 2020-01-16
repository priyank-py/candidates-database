from django.contrib import admin
from .models import CandidateDatabase, TaskDone
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, \
    SliderNumericFilter
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.

class CustomSliderNumericFilter(SliderNumericFilter):
    # MAX_DECIMALS = 2
    STEP = 5


class TaskDoneInline(admin.TabularInline):
    model = TaskDone
    extra = 1



@admin.register(CandidateDatabase)
class CandidateDatabaseAdmin(NumericFilterModelAdmin):
    list_display = ['id', 'filename', 'db_for', 'database_size']
    list_display_links = ['id', 'filename']
    list_filter = ['db_for', ('database_size', CustomSliderNumericFilter)]
    search_fields = ['id', 'filename', 'db_for']
    inlines = (TaskDoneInline,)
    


@admin.register(TaskDone)
class TaskDoneAdmin(admin.ModelAdmin):

    def database_info(self, instance):
        return instance.database.filename

    list_display = ['date', 'database_info', 'activity', 'quantity']
    list_display_links = ['date', 'database_info']
    list_filter = ['activity', ('date', DateRangeFilter), 'database__filename', 'date']
    autocomplete_fields = ['database']
