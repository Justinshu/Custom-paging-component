#下面是django中视图函数调用自定义插件
def publisher_list(request):
    # 从URL中取当前访问的页码数
    current_page = int(request.GET.get('page'))
    # 比len(models.Publisher.objects.all())更高效
    total_count = models.Publisher.objects.count()
    page_obj = Pagination(current_page, total_count, request.path_info)
    data = models.Publisher.objects.all()[page_obj.start:page_obj.end]
    page_html = page_obj.page_html()
    return render(request, "publisher_list.html", {"publisher_list": data, "page_html": page_html})
