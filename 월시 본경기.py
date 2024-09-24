# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 00:51:59 2023

@author: kimyj
"""

import os
import math
import random
import matplotlib.pyplot as plt
import matplotlib.image as img

from matplotlib import font_manager, rc
font_path = "c:/Windows/Fonts/서울한강 장체M.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

class candidate:
    def __init__(self, pic, name):
        self.pic = pic
        self.name = name

route = 'C:\\Users\\kimyj\\Desktop\\유튜브\\이상형 월시'
all_file_list = os.listdir(route)
random.shuffle(all_file_list)

all_name_list = []
all_pic_list = []

for filename in all_file_list:
    all_name_list.append(filename[:-4])
    
    pic = img.imread(route+'\\'+filename)
    all_pic_list.append(pic)

all_cand_list = []

for i in range(len(all_file_list)):
    pic = all_pic_list[i]
    name = all_name_list[i]
    
    player = candidate(pic, name)
    
    all_cand_list.append(player)

tour = 2 ** math.floor(math.log2(len(all_cand_list)))
thre = 2*(len(all_cand_list) - tour)

list_prev = all_cand_list[:thre]
list_next = all_cand_list[thre:]

match = len(list_prev)//2
    
for i in range(match):
    next_step = input("Press any key. ")
    p1 = list_prev[2*i]
    p2 = list_prev[2*i+1]
    im1 = p1.pic
    im2 = p2.pic
    name1 = p1.name
    name2 = p2.name
    
    plt.rc('font', family='Malgun Gothic')
    fig = plt.figure(figsize=(16,12))
    fig.suptitle("기묭진의 이상형 월드 시리즈\n와일드카드 게임 %d경기 (%d/%d)" % (i+1, i+1, match), fontsize=25)
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)
    ax1.set_title(name1, fontsize=20)
    ax2.set_title(name2, fontsize=20)
    ax1.imshow(im1)
    ax2.imshow(im2)
    ax1.axis('off')
    ax2.axis('off')
    plt.grid('off')
    plt.show()
    
    winside = input("Left or Right? ")
    while not winside in ['l','ㅣ','r','ㄱ']:
        winside = input("Left or Right? ")
    
    if winside=='l' or winside=='ㅣ':
        winner = p1
    elif winside=='r' or winside=='ㄱ':
        winner = p2
    
    list_next.append(winner)
    
    fig = plt.figure(figsize=(8,9))
    plt.title("\n%s 본선 %d강 진출!\n" % (winner.name, tour), fontsize=25)
    plt.axis('off')
    plt.imshow(winner.pic)
    plt.show()

list_prev = list_next
list_next = []
random.shuffle(list_prev)

while len(list_prev) != 1:
    match = len(list_prev)//2
    
    for i in range(match):
        next_step = input("Press any key. ")
        p1 = list_prev[2*i]
        p2 = list_prev[2*i+1]
        im1 = p1.pic
        im2 = p2.pic
        name1 = p1.name
        name2 = p2.name
        
        plt.rc('font', family='Malgun Gothic') # 서울서체 안돼서 임시로
        fig = plt.figure(figsize=(16,12))
        if match > 2:
            match_title = "기묭진의 이상형 월드 시리즈\n%d강전 %d경기" % (match*2, i+1)
        elif match == 2:
            match_title = "기묭진의 이상형 월드 시리즈\n준결승전 %d경기" % (i+1)
        elif match == 1:
            match_title = "기묭진의 이상형 월드 시리즈\n결승전"
        fig.suptitle(match_title, fontsize=25)
        ax1 = fig.add_subplot(1,2,1)
        ax2 = fig.add_subplot(1,2,2)
        ax1.set_title(name1, fontsize=20)
        ax2.set_title(name2, fontsize=20)
        ax1.imshow(im1)
        ax2.imshow(im2)
        ax1.axis('off')
        ax2.axis('off')
        plt.grid('off')
        plt.show()
        
        winside = input("Left or Right? ")
        while not winside in ['l','ㅣ','r','ㄱ']:
            winside = input("Left or Right? ")
        
        if winside=='l' or winside=='ㅣ':
            winner = p1
        elif winside=='r' or winside=='ㄱ':
            winner = p2
        
        list_next.append(winner)
        
        fig = plt.figure(figsize=(8,9))
        if match > 4:
            next_title = "\n%s %d강 진출!\n" % (winner.name, match)
        elif match == 4:
            next_title = "\n%s 준결승전 진출!\n" % winner.name
        elif match == 2:
            next_title = "\n%s 결승전 진출!\n" % winner.name
        elif match == 1:
            next_title = "\n기묭진의 이상형 월드 시리즈\n%s 우승!\n" % winner.name
        plt.title(next_title, fontsize=25)
        plt.axis('off')
        plt.imshow(winner.pic)
        plt.show()
    list_prev = list_next
    list_next = []
    
    if len(list_prev) == 16:
        next_step = input("Press any key. ")
        plt.rc('font', family='Malgun Gothic') # 서울서체 안돼서 임시로
        fig = plt.figure(figsize=(16,12))
        fig.suptitle("기묭진의 이상형 월드 시리즈\n16강 진출자 명단\n", fontsize=25)
        
        lax1 = fig.add_subplot(3,6,1)
        lax2 = fig.add_subplot(3,6,2)
        lax3 = fig.add_subplot(3,6,5)
        lax4 = fig.add_subplot(3,6,6)
        lax5 = fig.add_subplot(3,6,7)
        lax6 = fig.add_subplot(3,6,8)
        lax7 = fig.add_subplot(3,6,9)
        lax8 = fig.add_subplot(3,6,10)
        lax9 = fig.add_subplot(3,6,11)
        lax10 = fig.add_subplot(3,6,12)
        lax11 = fig.add_subplot(3,6,13)
        lax12 = fig.add_subplot(3,6,14)
        lax13 = fig.add_subplot(3,6,15)
        lax14 = fig.add_subplot(3,6,16)
        lax15 = fig.add_subplot(3,6,17)
        lax16 = fig.add_subplot(3,6,18)
        
        lax1.set_title(list_prev[0].name, fontsize=15)
        lax2.set_title(list_prev[1].name, fontsize=15)
        lax3.set_title(list_prev[2].name, fontsize=15)
        lax4.set_title(list_prev[3].name, fontsize=15)
        lax5.set_title(list_prev[4].name, fontsize=15)
        lax6.set_title(list_prev[5].name, fontsize=15)
        lax7.set_title(list_prev[6].name, fontsize=15)
        lax8.set_title(list_prev[7].name, fontsize=15)
        lax9.set_title(list_prev[8].name, fontsize=15)
        lax10.set_title(list_prev[9].name, fontsize=15)
        lax11.set_title(list_prev[10].name, fontsize=15)
        lax12.set_title(list_prev[11].name, fontsize=15)
        lax13.set_title(list_prev[12].name, fontsize=15)
        lax14.set_title(list_prev[13].name, fontsize=15)
        lax15.set_title(list_prev[14].name, fontsize=15)
        lax16.set_title(list_prev[15].name, fontsize=15)
        
        lax1.imshow(list_prev[0].pic)
        lax2.imshow(list_prev[1].pic)
        lax3.imshow(list_prev[2].pic)
        lax4.imshow(list_prev[3].pic)
        lax5.imshow(list_prev[4].pic)
        lax6.imshow(list_prev[5].pic)
        lax7.imshow(list_prev[6].pic)
        lax8.imshow(list_prev[7].pic)
        lax9.imshow(list_prev[8].pic)
        lax10.imshow(list_prev[9].pic)
        lax11.imshow(list_prev[10].pic)
        lax12.imshow(list_prev[11].pic)
        lax13.imshow(list_prev[12].pic)
        lax14.imshow(list_prev[13].pic)
        lax15.imshow(list_prev[14].pic)
        lax16.imshow(list_prev[15].pic)
        
        lax1.axis('off')
        lax2.axis('off')
        lax3.axis('off')
        lax4.axis('off')
        lax5.axis('off')
        lax6.axis('off')
        lax7.axis('off')
        lax8.axis('off')
        lax9.axis('off')
        lax10.axis('off')
        lax11.axis('off')
        lax12.axis('off')
        lax13.axis('off')
        lax14.axis('off')
        lax15.axis('off')
        lax16.axis('off')
        
        plt.grid('off')
        plt.show()
    if len(list_prev) == 8:
        next_step = input("Press any key. ")
        plt.rc('font', family='Malgun Gothic') # 서울서체 안돼서 임시로
        fig = plt.figure(figsize=(16,12))
        fig.suptitle("기묭진의 이상형 월드 시리즈\n8강 진출자 명단\n", fontsize=25)
        
        lax1 = fig.add_subplot(2,4,1)
        lax2 = fig.add_subplot(2,4,2)
        lax3 = fig.add_subplot(2,4,3)
        lax4 = fig.add_subplot(2,4,4)
        lax5 = fig.add_subplot(2,4,5)
        lax6 = fig.add_subplot(2,4,6)
        lax7 = fig.add_subplot(2,4,7)
        lax8 = fig.add_subplot(2,4,8)
        
        lax1.set_title(list_prev[0].name, fontsize=15)
        lax2.set_title(list_prev[1].name, fontsize=15)
        lax3.set_title(list_prev[2].name, fontsize=15)
        lax4.set_title(list_prev[3].name, fontsize=15)
        lax5.set_title(list_prev[4].name, fontsize=15)
        lax6.set_title(list_prev[5].name, fontsize=15)
        lax7.set_title(list_prev[6].name, fontsize=15)
        lax8.set_title(list_prev[7].name, fontsize=15)
        
        lax1.imshow(list_prev[0].pic)
        lax2.imshow(list_prev[1].pic)
        lax3.imshow(list_prev[2].pic)
        lax4.imshow(list_prev[3].pic)
        lax5.imshow(list_prev[4].pic)
        lax6.imshow(list_prev[5].pic)
        lax7.imshow(list_prev[6].pic)
        lax8.imshow(list_prev[7].pic)
        
        
        lax1.axis('off')
        lax2.axis('off')
        lax3.axis('off')
        lax4.axis('off')
        lax5.axis('off')
        lax6.axis('off')
        lax7.axis('off')
        lax8.axis('off')
        
        plt.grid('off')
        plt.show()
    elif len(list_prev) == 4:
        next_step = input("Press any key. ")
        plt.rc('font', family='Malgun Gothic') # 서울서체 안돼서 임시로
        fig = plt.figure(figsize=(16,12))
        fig.suptitle("기묭진의 이상형 월드 시리즈\n준결승 진출자 명단\n", fontsize=25)
        
        lax1 = fig.add_subplot(2,2,1)
        lax2 = fig.add_subplot(2,2,2)
        lax3 = fig.add_subplot(2,2,3)
        lax4 = fig.add_subplot(2,2,4)
        
        lax1.set_title(list_prev[0].name, fontsize=20)
        lax2.set_title(list_prev[1].name, fontsize=20)
        lax3.set_title(list_prev[2].name, fontsize=20)
        lax4.set_title(list_prev[3].name, fontsize=20)
        
        lax1.imshow(list_prev[0].pic)
        lax2.imshow(list_prev[1].pic)
        lax3.imshow(list_prev[2].pic)
        lax4.imshow(list_prev[3].pic)
        
        
        lax1.axis('off')
        lax2.axis('off')
        lax3.axis('off')
        lax4.axis('off')
        
        plt.grid('off')
        plt.show()
    
    random.shuffle(list_prev)
