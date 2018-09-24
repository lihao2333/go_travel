from django.shortcuts import render
from navigation.models import Section
def index(request):
    #res = []
    #for line in open("map/text.txt").readlines():
    #    _ = line.strip().split("|")
    #    temp = {}
    #    temp['ip'] = _[1].strip()
    #    temp['title'] = _[0].strip()
    #    res.append(temp)
    #ctx = {"res":res}
    #print(ctx)
    ctx = {"sections":Section.objects.all()}
    return render(request, "index.html",ctx)
