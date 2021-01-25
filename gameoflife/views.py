from django.http import JsonResponse
import json
from .logic import przelicz_plansze, wyswietl_plansze

def przelicz_z_binarnego(request):
    post_data = json.loads(request.body)
    plansza = []
    for line in post_data["data"]:
        plansza_line = []
        converted_line = str(bin(line))[2:].zfill(post_data["size"])
        for char in converted_line:
            if char == "0":
                plansza_line.append(False)
            else:
                plansza_line.append(True)
            plansza.append(plansza_line)
    wyswietl_plansze(plansza)
    przeliczona = przelicz_plansze(plansza)
    wyswietl_plansze(przeliczona)
    return JsonResponse({"przeliczona_plansza":przeliczona,})

def przelicz_normalnie(request):
    post_data = json.loads(request.body)
    plansza = post_data.get("plansza")
    # for line in post_data["data"]:
    #     plansza_line = []
    #     converted_line = str(bin(line))[2:].zfill(post_data["size"])
    #     for char in converted_line:
    #         if char == "0":
    #             plansza_line.append(False)
    #         else:
    #             plansza_line.append(True)
    #         plansza.append(plansza_line)
    wyswietl_plansze(plansza)
    przeliczona = przelicz_plansze(plansza)
    wyswietl_plansze(przeliczona)
    return JsonResponse({"rozmiar":len(przeliczona), "przeliczona_plansza":przeliczona,})
