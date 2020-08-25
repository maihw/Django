from django.shortcuts import render
from .models import Person

#文件包含了页面的业务逻辑。book_archive() 函数叫做视图。
#这里还用到了 year_archive.html 模板。
def book_archive(request, year):
    book_list =
Person.objects.filter(birth_year = year)
    context = {'year': year, 'book_list': book_list}
    return render(request,
'books/year_archive.html', context)