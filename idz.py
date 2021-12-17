#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = (2, 2.1, 4, 7.8, 3.2, 2.1, 7.9, 4.2, 8.4, 33.8, 2, 4.2, 2.1)
    B = (560, 790, 1500, 2300, 1200, 790, 2500, 1500, 3000, 8550, 610, 1450, 950)

    s = float(input("Введите сумму s: "))
    
    d =[(volume) for volume, price in zip (A, B) if price > s]
    print (d)
