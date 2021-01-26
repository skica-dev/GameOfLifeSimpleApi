from django.http import JsonResponse
import json

from django.shortcuts import render

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
    przeliczona_bin = []
    for line in przeliczona:
        line_bin = "".join([str(int(x)) for x in line])
        line_decimal = int(line_bin, 2)
        przeliczona_bin.append(line_decimal)
    print(przeliczona_bin)
    return JsonResponse({"rozmiar": len(przeliczona), "przeliczona_plansza-binarnie": przeliczona_bin, })


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
    # wyswietl_plansze(plansza)
    przeliczona = przelicz_plansze(plansza)
    # wyswietl_plansze(przeliczona)
    return JsonResponse({"rozmiar": len(przeliczona), "przeliczona_plansza": przeliczona, })


def homepage(request):
    return render(request, "index.html")
