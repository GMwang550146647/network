#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
maze=[
    [1,'s',1,1,1,1,1,1,0,1],
    [0,0,0,0,0,0,1,0,0,1],
    [0,1,0,1,1,1,1,1,0,1],
    [0,1,0,0,0,0,0,0,0,0],
    [1,1,0,1,1,0,1,1,1,1],
    [0,0,0,0,1,0,0,0,0,1],
    [0,1,1,1,1,1,1,1,0,1],
    [0,0,0,0,1,0,0,0,0,0],
    [0,1,1,1,1,0,1,1,1,0],
    [0,0,0,0,1,0,0,0,'g',1]
]
maze2=[
    [1,'s',1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,1,0,1],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,0,0,0,'g']
]
road=[]
def search_road_digui(maze,position,pre):
    global road
    road.append(position)
    state=maze[position[0]][position[1]]
    if state=='g':
        print road
        return
    if state==1:
        return
    if position[0]<len(maze)-1 and pre!=2:
        p1=[position[0]+1,position[1]+0]  #前
        search_road_digui(maze,p1,1)
        road.pop()
    if position[0]>0 and pre!=1:
        p2=[position[0]-1,position[1]+0]   #后
        search_road_digui(maze,p2,2)
        road.pop()
    if position[1]>0 and pre!=4:
        p3=[position[0]+0,position[1]-1]    #上
        search_road_digui(maze,p3,3)
        road.pop()
    if position[1]<len(maze[0])-1 and pre!=3:
        p4=[position[0]+0,position[1]+1]    #下
        search_road_digui(maze,p4,4)
        road.pop()
    return
search_road_digui(maze,[0,1],10)

# def search_road_stack_bfs(maze):
#     position=[0,1,10]
#     s1=[]
#     s2=[]
#     s1.append(position)
#     while s1:
#         position=s1.pop(0)
#         state=maze[position[0]][position[1]]
#         if state==1:
#             continue
#         if position[0]<len(maze[0])-1 and position[2]!=2:
#             p1=[position[0]+1,position[1]+0,1]  #前
#             s1.append(p1)
#         if position[0]>0 and position[2]!=1:
#             p2=[position[0]-1,position[1]+0,2]   #后
#             s1.append(p2)
#         if position[1]>0 and position[2]!=4:
#             p3=[position[0]+0,position[1]-1,3]    #上
#             s1.append(p3)
#         if position[1]<len(maze)-1 and position!=3:
#             p4=[position[0]+0,position[1]+1,4]    #下
#             s1.append(p4)
#
#         if state=='g':
#             return True
#     return False
#
#     return position
# def search_road_stack_dfs(maze):
#     position=[0,1,10]
#     s1=[]
#     s2=[]
#     s1.append(position)
#     while s1:
#         flag=0
#         position=s1.pop()
#         state=maze[position[0]][position[1]]
#         if state==1:
#             continue
#         if position[0]<len(maze[0])-1 and position[2]!=2:
#             p1=[position[0]+1,position[1]+0,1]  #前
#             s1.append(p1)
#             flag=1
#         if position[0]>0 and position[2]!=1:
#             p2=[position[0]-1,position[1]+0,2]   #后
#             s1.append(p2)
#             flag=1
#         if position[1]>0 and position[2]!=4:
#             p3=[position[0]+0,position[1]-1,3]    #上
#             s1.append(p3)
#             flag=1
#         if position[1]<len(maze)-1 and position!=3:
#             p4=[position[0]+0,position[1]+1,4]    #下
#             s1.append(p4)
#             flag=1
#         if flag==1:
#             continue
#
#         if state=='g':
#             return True
#     return False
#
#     return position
# print search_road_stack_bfs(maze)
# print search_road_stack_dfs(maze)