from django.shortcuts import render
def index(request):
    res = []
    for line in open("map/text.txt").readlines():
        _ = line.strip().split("|")
        temp = {}
        temp['ip'] = _[1].strip()
        temp['title'] = _[0].strip()
        res.append(temp)
    ctx = {"res":res}
    print(ctx)
    return render(request, "index.html",ctx)
