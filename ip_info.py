#!/usr/bin/python
# -*- coding=utf-8 -*-

import os

import requests
import termcolor

url = "http://ip.taobao.com/service/getIpInfo.php?ip="


def ip_detail():
    resp = requests.get(url + ip)
    datadict = resp.json()

    country = datadict["data"]["country"]
    region = datadict["data"]["region"]
    city = datadict["data"]["city"]
    isp = datadict["data"]["isp"]

    return termcolor.colored("IP:", 'cyan') + termcolor.colored(ip, 'yellow') + "\n" \
           + termcolor.colored("Country:", 'cyan') + termcolor.colored(country, 'yellow') + "\n" \
           + termcolor.colored("Region:", 'cyan') + termcolor.colored(region, 'yellow') + "\n" \
           + termcolor.colored("City:", 'cyan') + termcolor.colored(city, 'yellow') + "\n" \
           + termcolor.colored("Isp:", 'cyan') + termcolor.colored(isp, 'yellow')


if __name__ == "__main__":
    os.system("clear")
    response = requests.get('https://httpbin.org/ip')
    ip = response.json()["origin"]
    print(ip_detail())
