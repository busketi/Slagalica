#%%
from numpy import random
import pandas as pd
import numpy as np
import nltk
import sklearn
import matplotlib.pyplot as plt
import itertools
from itertools import combinations_with_replacement
from itertools import product
import math
import random



#%%

class Mastermind():
    
    
    
    def __init__(self,xplace=4,xsign=6,xanswer=0):
        """inicijalizacija sa opcionim argumentima za broj polja i znakova"""
        self.sign=xsign
        self.place=xplace
        self.num_guess=0
        self.initial_solutions()
        self.previous_guess=list()
        self.feedbacks=list()
        'Postavljanje tacnog RESENJA ako je ubacen u konstruktorn ako ne stavlja se random kombinacija od mogucih RESENJA'
        if (xanswer == 0):
            self.answer=random.choice(self.solutions)
        else:
            self.answer=xanswer
        
        
        'Inicijalizacija mogucih RESENJA'
    def initial_solutions(self):
        temp_list=list()
        self.solutions=list()
        temp=product(range(1,self.sign+1),repeat=self.place)
        temp_list=[list(ele) for ele in temp]
        self.solutions=temp_list.copy()
        self.num_solutions=len(self.solutions)
        self.all_solutions=temp_list.copy()
        self.num_all_solutions=len(self.all_solutions)
        # for ele in temp_list:self.solutions.append(np.array(ele))
        'Metoda za redukovanje mogucih RESENJA posle GUESSA'
    def new_solutions(self,xguess,redyellow):
        i=0
        while (i != len(self.solutions)):
            
            if (self.compare(self.solutions[i],xguess)!=redyellow):
                del self.solutions[i]
                i-=1
            i+=1
        self.num_solutions=len(self.solutions)
                
        'Metoda za GUESS koja redukuje resenja i vraca broj RED i YELLOW'        
    def guess(self,xguess):
        self.previous_guess.append(xguess)
        self.num_guess+=1
        # if(self.num_guess==6):
        #     print(self.answer)
        red=0
        yellow=0
        tempG=xguess.copy()
        tempA=self.answer.copy()
        for i in range (0,self.place):
            if (tempG[i]==tempA[i]):
                red+=1
                tempG[i]=0
                tempA[i]=0

        for i in range (0,self.place):
            if (tempG[i] != 0) and (tempG[i] in tempA):
                yellow+=1
                tempA[tempA.index(tempG[i])]=0
        
        self.feedbacks.append([red, yellow])
        self.new_solutions(xguess, [red,yellow])
        return [red,yellow]
        'Slicna metodi GUESS samo ne redukuje broj resenja, samo vraca broj RED i YELLOW'
    def compare(self,xguess,yguess):
        red=0
        yellow=0
        tempG=xguess.copy()
        tempA=yguess.copy()
        for i in range (0,self.place):
            if (tempG[i]==tempA[i]):
                red+=1
                tempG[i]=0
                tempA[i]=0
                
        for i in range (0,self.place):
            if (tempG[i] != 0) and (tempG[i] in tempA):
                yellow+=1
                tempA[tempA.index(tempG[i])]=0       
        return [red,yellow]
        'P je broj svih mogucih RESENJA, posle GUESSA i feedbacka([RED,YELLOW]) broj resenja se redukuje na p1,p2,p3'
    def firstGuess(self,xguess):
        redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
        for i in range(0,len(self.all_solutions)):
            [r,y]=self.compare(self.all_solutions[i],xguess)
            redyellow[r,y]+=1
        return redyellow
        
        
    def solveKnuth(self):
        'Algoritam koji uzima resenje koje ima minimalan maksimalan broj mogucnosti posle GUESSA'
        'Knuthov algoritam(NIJE sredjeno da uzima minimalniju drugu particiju ako su prve jednakog broja)'

        self.num_guess=0
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,1,2,2])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(self.solutions)):
                for j in range(0,len(self.solutions)):
                    if (i!=j):
                        [r,y]=self.compare(self.solutions[i],self.solutions[j])
                        redyellow[r,y]+=1
                redyellow=redyellow.flatten()
                redyellow=np.sort(redyellow)[::-1]
                minimax.append(redyellow)        
                redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
            index=self.Knuth(minimax)
            [r,y]=self.guess(self.solutions[index])
            if (r==4):
                T=False

    def solveKnuthMax(self):
        
        
        'Algoritam koji uzima resenje koje ima minimalan maksimalan broj mogucnosti posle GUESSA'
        'Knuthov algoritam(NIJE sredjeno da uzima minimalniju drugu particiju ako su prve jednakog broja)'

        self.num_guess=0
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,1,2,2])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
        solucije=self.all_solutions.copy()
        T=True
        if(r1==4):
            T=False
        while (T):
            minimax=list()
            for i in range(0,len(solucije)):
                for j in range(0,len(self.solutions)):
                    if (solucije[i]!=self.solutions[j]):
                        [r,y]=self.compare(solucije[i],self.solutions[j])
                        redyellow[r,y]+=1
                redyellow=redyellow.flatten()
                redyellow=np.sort(redyellow)[::-1]
                minimax.append(redyellow)        
                redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
            
            index=self.Knuth(minimax)
            [r,y]=self.guess(solucije[index].copy())
            if ((r==4)):
                T=False
                
                
    def solveMaxEnt(self):
        '(p1^2+p2^2+...)/UkupanBrojSolucija'
        self.num_guess=0
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,2,3,4])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(self.solutions)):
                for j in range(0,len(self.solutions)):
                    if (i!=j):
                        [r,y]=self.compare(self.solutions[i],self.solutions[j])
                        redyellow[r,y]+=1
                    else:
                        redyellow[4,0]=0.95
                temp=redyellow.flatten()
                temp=temp[np.nonzero(temp)]
                temp1=temp.copy()
                temp1=np.ceil(temp1)/len(self.solutions)
                temp=temp/len(self.solutions)
                minimax.append(np.sum(temp1*np.log2(temp)))
                redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
            min_value = min(minimax)
            index=minimax.index(min_value)
            [r,y]=self.guess(self.solutions[index])
            if (r==4):
                T=False
            else:
                if (len(self.solutions)==1):
                    [r,y]=self.guess(self.solutions[0])
                    T=False
        
    def solveMaxEntMax(self):
        '(p1^2+p2^2+...)/UkupanBrojSolucija'
        self.num_guess=0   
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,2,3,4])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
        solucije=self.all_solutions.copy()
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(solucije)):
                for j in range(0,len(self.solutions)):
                    if (solucije[i]!=self.solutions[j]):
                        [r,y]=self.compare(solucije[i],self.solutions[j])
                        redyellow[r,y]+=1
                    else:
                        redyellow[4,0]=0.95
                temp=redyellow.flatten()
                temp=temp[np.nonzero(temp)]
                temp1=temp.copy()
                temp1=np.ceil(temp1)/len(self.solutions)
                temp=temp/len(self.solutions)
                minimax.append(np.sum(temp1*np.log2(temp)))
                redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
            min_value = min(minimax)
            index=minimax.index(min_value)
            [r,y]=self.guess(solucije[index])
            
            if (r==4):
                T=False
            else:
                if (len(self.solutions)==1):
                    [r,y]=self.guess(self.solutions[0])
                    T=False
        print('new guess',self.num_guess)
    
    def solveIrving(self):
        '(p1^2+p2^2+...)/UkupanBrojSolucija'
        self.num_guess=0
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,2,3,4])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(self.solutions)):
                for j in range(0,len(self.solutions)):
                    if (i!=j):
                        [r,y]=self.compare(self.solutions[i],self.solutions[j])
                        redyellow[r,y]+=1
                minimax.append(np.sum(np.power(redyellow,2)))
                redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
            min_value = min(minimax)
            index=minimax.index(min_value)
            [r,y]=self.guess(self.solutions[index])
            if (r==4):
                T=False
        
    def solveIrvingMax(self):
        '(p1^2+p2^2+...)/UkupanBrojSolucija'
        self.num_guess=0   
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,2,3,4])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
        solucije=self.all_solutions.copy()
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(solucije)):
                for j in range(0,len(self.solutions)):
                    if (solucije[i]!=self.solutions[j]):
                        [r,y]=self.compare(solucije[i],self.solutions[j])
                        redyellow[r,y]+=1
                minimax.append(np.sum(np.power(redyellow.copy(),2)))
                redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
            min_value = min(minimax)
            index=minimax.index(min_value)
            [r,y]=self.guess(solucije[index])
            if (r==4):
                T=False
     
                
    def solveIrving3(self):
        '(p1^3+p2^3+...)/UkupanBrojSolucija'
        self.num_guess=0
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,1,2,3])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(self.solutions)):
                for j in range(0,len(self.solutions)):
                    if (i!=j):
                        [r,y]=self.compare(self.solutions[i],self.solutions[j])
                        redyellow[r,y]+=1
                minimax.append(np.sum(np.power(redyellow,3)))
                redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
            min_value = min(minimax)
            index=minimax.index(min_value)
            [r,y]=self.guess(self.solutions[index])
            if (r==4):
                T=False
      
    def solveIrvingMax3(self):
        '(p1^3+p2^3+...)/UkupanBrojSolucija'
        self.num_guess=0
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,1,2,3])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
        solucije=self.all_solutions.copy()
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(solucije)):
                for j in range(0,len(self.solutions)):
                    if (solucije[i]!=self.solutions[j]):
                        [r,y]=self.compare(solucije[i],self.solutions[j])
                        redyellow[r,y]+=1
                minimax.append(np.sum(np.power(redyellow.copy(),3)))
                redyellow=np.zeros((self.place+1,self.place+1), dtype=int)
            min_value = min(minimax)
            index=minimax.index(min_value)
            [r,y]=self.guess(solucije[index])
            if (r==4):
                T=False
                
      
                
    def solveMaxPartKnuth(self):
        'Maksimalan broj particija nakon GUESSA'
        self.num_guess=0      
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,1,2,3])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(self.solutions)):
                for j in range(0,len(self.solutions)):
                    if (i!=j):
                        [r,y]=self.compare(self.solutions[i],self.solutions[j])
                        redyellow[r,y]+=1
                    else:
                        redyellow[4,0]=0.95
                redyellow=redyellow.flatten()
                redyellow=np.sort(redyellow)[::-1]
                minimax.append(redyellow)
                redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
            index=self.MaxPartKnuth(minimax)
            [r,y]=self.guess(self.solutions[index])
            if (r==4):
                T=False
        
    def solveMaxPartKnuthMax(self):
        'Maksimalan broj particija nakon GUESSA'
        self.num_guess=0
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,1,2,3])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
        solucije=self.all_solutions.copy()
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(solucije)):
                for j in range(0,len(self.solutions)):
                    if (solucije[i]!=self.solutions[j]):
                        [r,y]=self.compare(solucije[i],self.solutions[j])
                        redyellow[r,y]+=1
                    else:
                        redyellow[4,0]=0.95
                redyellow=redyellow.flatten()
                redyellow=np.sort(redyellow)[::-1]
                minimax.append(redyellow)
                redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
            index=self.MaxPartKnuth(minimax)
            [r,y]=self.guess(solucije[index].copy())
            if (r==4):
                T=False
                
    def solveMaxPartIrving(self):
        'Maksimalan broj particija nakon GUESSA'
        self.num_guess=0      
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,1,2,3])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(self.solutions)):
                for j in range(0,len(self.solutions)):
                    if (i!=j):
                        [r,y]=self.compare(self.solutions[i],self.solutions[j])
                        redyellow[r,y]+=1
                    else:
                        redyellow[4,0]=0.95
                redyellow=redyellow.flatten()
                redyellow=np.sort(redyellow)[::-1]
                minimax.append(redyellow)
                redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
            index=self.MaxPartIrving(minimax)
            [r,y]=self.guess(self.solutions[index])
            if (r==4):
                T=False
        
    def solveMaxPartIrvingMax(self):
        'Maksimalan broj particija nakon GUESSA'
        self.num_guess=0
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,1,2,3])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
        solucije=self.all_solutions.copy()
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(solucije)):
                for j in range(0,len(self.solutions)):
                    if (solucije[i]!=self.solutions[j]):
                        [r,y]=self.compare(solucije[i],self.solutions[j])
                        redyellow[r,y]+=1
                    else:
                        redyellow[4,0]=0.95
                redyellow=redyellow.flatten()
                redyellow=np.sort(redyellow)[::-1]
                minimax.append(redyellow)
                redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
            index=self.MaxPartIrving(minimax)
            [r,y]=self.guess(solucije[index].copy())
            if (r==4):
                T=False
                
    def solveMaxPartIrving3(self):
        'Maksimalan broj particija nakon GUESSA'
        self.num_guess=0      
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,1,2,3])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(self.solutions)):
                for j in range(0,len(self.solutions)):
                    if (i!=j):
                        [r,y]=self.compare(self.solutions[i],self.solutions[j])
                        redyellow[r,y]+=1
                    else:
                        redyellow[4,0]=0.95
                redyellow=redyellow.flatten()
                redyellow=np.sort(redyellow)[::-1]
                minimax.append(redyellow)
                redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
            index=self.MaxPartIrving3(minimax)
            [r,y]=self.guess(self.solutions[index])
            if (r==4):
                T=False
        
    def solveMaxPartIrving3Max(self):
        'Maksimalan broj particija nakon GUESSA'
        self.num_guess=0
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,1,2,3])
        minimax=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
        solucije=self.all_solutions.copy()
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            for i in range(0,len(solucije)):
                for j in range(0,len(self.solutions)):
                    if (solucije[i]!=self.solutions[j]):
                        [r,y]=self.compare(solucije[i],self.solutions[j])
                        redyellow[r,y]+=1
                    else:
                        redyellow[4,0]=0.95
                redyellow=redyellow.flatten()
                redyellow=np.sort(redyellow)[::-1]
                minimax.append(redyellow)
                redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
            index=self.MaxPartIrving3(minimax)
            [r,y]=self.guess(solucije[index].copy())
            if (r==4):
                T=False
                
    def solveMaxPartMaxEnt(self):
        'Maksimalan broj particija nakon GUESSA'
        self.num_guess=0      
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,1,2,3])
        minimax=list()
        maxent=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
        T=True
        if(r1==4):T=False
        while (T):
            minimax=list()
            maxent=list()
            for i in range(0,len(self.solutions)):
                for j in range(0,len(self.solutions)):
                    if (i!=j):
                        [r,y]=self.compare(self.solutions[i],self.solutions[j])
                        redyellow[r,y]+=1
                    else:
                        redyellow[4,0]=0.95
                temp=redyellow.flatten().copy()
                temp=temp[np.nonzero(temp)]
                temp1=temp.copy()
                temp1=np.ceil(temp1)/len(self.solutions)
                temp=temp/len(self.solutions)
                redyellow=redyellow.flatten()
                redyellow=np.sort(redyellow)[::-1]
                maxent.append(np.sum(temp1*np.log2(temp)))
                minimax.append(redyellow)
                redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
            index=self.MaxPartMaxEnt(minimax,maxent)
            [r,y]=self.guess(self.solutions[index])
            if (r==4):
                T=False
                
    def solveMaxPartMaxEntMax(self):
        'Maksimalan broj particija nakon GUESSA'
        self.num_guess=0      
        if (self.num_guess==0):
            [r1,y1]=self.guess([1,1,2,3])
        minimax=list()
        maxent=list()
        redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
        T=True
        if(r1==4):T=False
        solucije=self.all_solutions.copy()
        while (T):
            minimax=list()
            maxent=list()
            for i in range(0,len(solucije)):
                for j in range(0,len(self.solutions)):
                    if (solucije[i]!=self.solutions[j]):
                        [r,y]=self.compare(solucije[i],self.solutions[j])
                        redyellow[r,y]+=1
                    else:
                        redyellow[4,0]=0.95
                temp=redyellow.flatten().copy()
                temp=temp[np.nonzero(temp)]
                temp1=temp.copy()
                temp1=np.ceil(temp1)/len(self.solutions)
                temp=temp/len(self.solutions)
                redyellow=redyellow.flatten()
                redyellow=np.sort(redyellow)[::-1]
                maxent.append(np.sum(temp1*np.log2(temp)))
                minimax.append(redyellow)
                redyellow=np.zeros((self.place+1,self.place+1), dtype=float)
            index=self.MaxPartMaxEnt(minimax,maxent)
            [r,y]=self.guess(solucije[index])
            
            if (r==4):
                T=False
         
            
            
    def Knuth(self,minimax):
        temp=minimax[len(minimax)-1].copy()
        index=len(minimax)-1
        for i,elem in enumerate(minimax):
            j=0
            T=True
            while(T and (j<20)):
                if (elem[j]<temp[j]):
                    temp=elem.copy()
                    index=i
                    T=False
                elif (elem[j]==temp[j]):
                    if (j==19):
                        if (self.all_solutions[i] in self.solutions):
                            temp=elem.copy()
                            index=i
                            T=False         
                    j+=1
                else:
                    T=False 
        return index
    
    def MaxPartKnuth(self,minimax):
        temp=minimax[-1].copy()
        index=len(minimax)-1
        indexPart=np.count_nonzero(minimax[-1])
        for i,elem in enumerate(minimax):
            j=0
            T=True           
            if (np.count_nonzero(elem)>indexPart):
                temp=elem.copy()
                index=i
                indexPart=np.count_nonzero(elem)
            elif (np.count_nonzero(elem)==indexPart):
                while(T and (j<20)):
                    if (elem[j]<temp[j]):
                        temp=elem.copy()
                        index=i
                        indexPart=np.count_nonzero(elem)
                        T=False
                    elif (elem[j]==temp[j]):
                        if (j==19):
                            if (self.all_solutions[i] in self.solutions):
                                temp=elem.copy()
                                index=i
                                indexPart=np.count_nonzero(elem)
                                T=False
                        j+=1
                    else:
                        T=False 
        return index    
   
    def MaxPartIrving(self,minimax):
        index=len(minimax)-1
        indexPart=np.count_nonzero(minimax[-1])
        irving=np.sum(np.power(minimax[-1],2))
        for i,elem in enumerate(minimax):       
            if (np.count_nonzero(elem)>indexPart):
                index=i
                indexPart=np.count_nonzero(elem)
                irving=np.sum(np.power(elem,2))
            elif (np.count_nonzero(elem)==indexPart):
                if (irving>np.sum(np.power(elem,2))):
                    index=i
                    indexPart=np.count_nonzero(elem)
                    irving=np.sum(np.power(elem,2))           
        return index 
    
    def MaxPartIrving3(self,minimax):
        
        index=len(minimax)-1
        indexPart=np.count_nonzero(minimax[-1])
        irving=np.sum(np.power(minimax[-1],3))
        for i,elem in enumerate(minimax):       
            if (np.count_nonzero(elem)>indexPart):
                index=i
                indexPart=np.count_nonzero(elem)
                irving=np.sum(np.power(elem,3))
            if (np.count_nonzero(elem)==indexPart):
                if (irving>np.sum(np.power(elem,3))):
                    index=i
                    indexPart=np.count_nonzero(elem)
                    irving=np.sum(np.power(elem,3))           
        return index 
    

                
    def MaxPartMaxEnt(self,minimax,maxent):
        index=len(minimax)-1
        indexPart=np.count_nonzero(minimax[-1])
        temp=maxent[-1]
        for i,elem in enumerate(minimax):       
            if (np.count_nonzero(elem)>indexPart):
                index=i
                indexPart=np.count_nonzero(elem)
                temp=maxent[i] 
            elif (np.count_nonzero(elem)==indexPart):
                if (temp>maxent[i]):
                    index=i
                    indexPart=np.count_nonzero(elem)
                    temp=maxent[i]           
        return index 
    
    def initial_parents(self):
        indexes=np.random.permutation(len(self.all_solutions))
        indexes=indexes[0:100]
        parents=list()
        fit=list()
        for i in indexes:
            temp=self.all_solutions[i].copy()
            parents.append(temp)
            fit.append(self.fitness(temp, 1, 1))
            
        return parents,fit
        
        
        
    def fitness(self,x,a,b):
        fit=0
        x_temp=x.copy()
        for i, elem in enumerate(self.previous_guess):
            [r,y]=self.compare(elem,x_temp)
            # fit=fit + a/(1+abs(r-self.feedbacks[i][0])) + b/(1+abs(y-self.feedbacks[i][1]))
            fit=fit + a*abs(r-self.feedbacks[i][0]) + b*abs(y-self.feedbacks[i][1]) + 1
        return 1/fit 
    
    def crossover1(self,x,y):
        y1=y.copy()
        x1=x.copy()
        point=math.ceil(self.place/2)
        temp = y1[:point].copy()
        y1[:point]=x1[:point].copy()
        x1[:point]=temp.copy()
        return [x1,y1]
    
    def crossover2(self,x,y):
        temp1=x.copy()
        temp2=y.copy()
        point1 = math.ceil(self.place/3)
        point2 = math.ceil(self.place/3*2)
        temp1[:point1]=x[:point1].copy()
        temp1[point1:point2]=y[point1:point2].copy()
        temp1[point2:]=x[point2:].copy()
        
        temp2[:point1]=y[:point1].copy()
        temp2[point1:point2]=x[point1:point2].copy()
        temp2[point2:]=y[point2:].copy()    
        return [temp1,temp2] 
    
    def crossover(self,x,y):
        if random.random()<0.5 :
            temp=self.crossover1(x, y)
        else:
            temp=self.crossover2(x, y)
        return temp
    
    def mutation(self,x):
        temp=x.copy()
        if (random.random()<0.1):
            index=random.randint(0, self.place-1)
            T=True
            while(T):
                color=random.randint(1,self.sign)
                if (color!=temp[index]):
                    T=False
                    temp[index]=color
        return temp
    
        
    def permutation(self,x):
        temp1=x.copy()
        if (random.random()<0.1):
            temp=np.random.permutation(self.place)
            a=temp1[temp[0]]
            temp1[temp[0]]=temp1[temp[1]]
            temp1[temp[1]]=a
        return temp1
        
        
    
    def inversion(self,x):
        temp1=x.copy()
        if (random.random()<0.1):
            temp=np.random.permutation(self.place)
            a=min(temp[0],temp[1])
            b=max(temp[0],temp[1])
            temp=temp1.copy()
            temp[a:b]=np.flip(temp1[a:b].copy())
            temp1=temp
        return temp1
    
    def eligible(self,x):
        if (self.fitness(x, 1, 1)==self.num_guess):
            return True
        return False
      
        
    def solveGA(self,a1,b1):
        if (self.num_guess==0):
            self.guess([1,1,2,3])
        r=0
        a=a1
        b=b1
        while(r<4):
            population,fit=self.initial_parents()
            
            eligible_guesses=list()
            fit_eligible_guesses=list()
            
            population_temp=list()
            fit_temp=list()
            gen=0
            while((gen<100) and (len(eligible_guesses)<50)):
                gen=gen+1
                while((len(population_temp)<100) and (len(eligible_guesses)<50)):
                    'while za generacije'
                    # print('pop',len(population_temp))
                    # print('el',len(eligible_guesses))
                    
                    [parent1,parent2]=random.choices(population,weights=fit,k=2)
                    [child1,child2]=self.crossover(parent1, parent2)
                    child1=self.mutation(child1)
                    child1=self.permutation(child1)
                    child1=self.inversion(child1)
                    child2=self.mutation(child2)
                    child2=self.permutation(child2)
                    child2=self.inversion(child2)
                    parent1fit=self.fitness(parent1, a, b)
                    parent2fit=self.fitness(parent2, a, b)
                    child1fit=self.fitness(child1, a, b)
                    child2fit=self.fitness(child2, a, b)
                    s=0
                    if ((child1 in self.solutions) and (child1 not in eligible_guesses)):
                        eligible_guesses.append(child1)
                        fit_eligible_guesses.append(1/child1fit)
                        s=2
                        
                    if ((child2 in self.solutions) and (child2 not in eligible_guesses)):
                        eligible_guesses.append(child2)
                        fit_eligible_guesses.append(1/child2fit)
                        s=s+1
                        
                    if (s==0):
                        temp_guesses=[parent1,parent2,child1,child2]
                        temp_fit_guesses=[parent1fit,parent2fit,child1fit,child2fit]
                        i=0
                        k=0
                        while (i<2 and k<4):
                            max_value=max(temp_fit_guesses)
                            max_index=temp_fit_guesses.index(max_value)
                            if (temp_guesses[max_index] not in population_temp):
                                 population_temp.append(temp_guesses[max_index])
                                 fit_temp.append(temp_fit_guesses[max_index])
                                 i=i+1
                            k=k+1
                            temp_fit_guesses[max_index]=0
                    if (s==1):
                        temp_guesses=[parent1,parent2,child1]
                        temp_fit_guesses=[parent1fit,parent2fit,child1fit]
                        i=0
                        k=0
                        while (i<2 and k<3):
                            max_value=max(temp_fit_guesses)
                            max_index=temp_fit_guesses.index(max_value)
                            if (temp_guesses[max_index] not in population_temp):
                                 population_temp.append(temp_guesses[max_index])
                                 fit_temp.append(temp_fit_guesses[max_index])
                                 i=i+1
                            k=k+1
                            temp_fit_guesses[max_index]=0
                    if (s==2):
                        temp_guesses=[parent1,parent2,child2]
                        temp_fit_guesses=[parent1fit,parent2fit,child2fit]
                        i=0
                        k=0
                        while (i<2 and k<3):
                            max_value=max(temp_fit_guesses)
                            max_index=temp_fit_guesses.index(max_value)
                            if (temp_guesses[max_index] not in population_temp):
                                 population_temp.append(temp_guesses[max_index])
                                 fit_temp.append(temp_fit_guesses[max_index])
                                 i=i+1
                            k=k+1
                            temp_fit_guesses[max_index]=0
                    if (s==3):
                        temp_guesses=[parent1,parent2]
                        temp_fit_guesses=[parent1fit,parent2fit]
                        i=0
                        k=0
                        while (i<2 and k<2):
                            max_value=max(temp_fit_guesses)
                            max_index=temp_fit_guesses.index(max_value)
                            if (temp_guesses[max_index] not in population_temp):
                                 population_temp.append(temp_guesses[max_index])
                                 fit_temp.append(temp_fit_guesses[max_index])
                                 i=i+1
                            k=k+1
                            temp_fit_guesses[max_index]=0
                    while(i<2):
                        temp=random.choice(self.all_solutions)
                        if (temp not in population_temp):
                            population_temp.append(temp)
                            fit_temp.append(self.fitness(temp, a, b))
                            i=i+1
                        

                population=population_temp.copy()
                fit=fit_temp.copy()
                population_temp=list()
                fit_temp=list()
            if (len(eligible_guesses)==0):
                guess=random.choices(population,weights=fit,k=1)
            else:
                guess=random.choices(eligible_guesses,weights=fit_eligible_guesses,k=1)
            # if (len(eligible_guesses)==1 and self.num_solutions==1):
            #     print(eligible_guesses)
            #     print(self.answer)
            # print('s',self.num_solutions)
            # print('e',len(eligible_guesses))
            # print(self.num_guess)
            [r,y]=self.guess(guess[0])
            
            
    
        # print('num_guess = ',self.num_guess)
        return self.num_guess      
             
            
#%%
M=Mastermind(4,6)
#%%     
ry1111=M.firstGuess([1,1,1,1])
ry1112=M.firstGuess([1,1,1,2])
ry1122=M.firstGuess([1,1,2,2])
ry1123=M.firstGuess([1,1,2,3])
ry1234=M.firstGuess([1,2,3,4])


    

#%%
'Knuth: Samo validna resenja'
num_of_guessesKnuth=np.zeros(10)
num_of_guessesKnuthstd=np.zeros(1296)
for i in range(0,1296):
    print(i,'k')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveKnuth()
    num_of_guessesKnuth[temp.num_guess]+=1
    num_of_guessesKnuthstd[i]=temp.num_guess
all_guessesKnuth=0   
for i in range (0,8):
    all_guessesKnuth=all_guessesKnuth+i*num_of_guessesKnuth[i]

    
#%%
'Knuth: SVA resenja'
num_of_guessesKnuthMax=np.zeros(10)
num_of_guessesKnuthMaxstd=np.zeros(1296)
for i in range(0,1296):
    print(i,'km')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveKnuthMax()
    num_of_guessesKnuthMax[temp.num_guess]+=1
    num_of_guessesKnuthMaxstd[i]=temp.num_guess
all_guessesKnuthMax=0   
for i in range (0,8):
    all_guessesKnuthMax=all_guessesKnuthMax+i*num_of_guessesKnuthMax[i]


#%%

num_of_guessesMaxEnt=np.zeros(10)
num_of_guessesMaxEntstd=np.zeros(1296)
for i in range(0,1296):
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveMaxEnt()
    num_of_guessesMaxEnt[temp.num_guess]+=1
    num_of_guessesMaxEntstd[i]=temp.num_guess
all_guessesMaxEnt=0   
for i in range (0,8):
    all_guessesMaxEnt=all_guessesMaxEnt+i*num_of_guessesMaxEnt[i]
#%%
num_of_guessesMaxEntMax=np.zeros(10)
num_of_guessesMaxEntMaxstd=np.zeros(1296)
for i in range(0,1296):
    print(i,'mem')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveMaxEntMax()
    num_of_guessesMaxEntMax[temp.num_guess]+=1
    num_of_guessesMaxEntMaxstd[i]=temp.num_guess
all_guessesMaxEntMax=0   
for i in range (0,8):
    all_guessesMaxEntMax=all_guessesMaxEntMax+i*num_of_guessesMaxEntMax[i]
 #%%
num_of_guessesIrving=np.zeros(10)
num_of_guessesIrvingstd=np.zeros(1296)
for i in range(0,1296):
    print(i,'irv')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveIrving()
    num_of_guessesIrving[temp.num_guess]+=1
    num_of_guessesIrvingstd[i]=temp.num_guess
all_guessesIrving=0   
for i in range (0,8):
    all_guessesIrving=all_guessesIrving+i*num_of_guessesIrving[i]
#%%
num_of_guessesIrvingMax=np.zeros(10)
num_of_guessesIrvingMaxstd=np.zeros(1296)
for i in range(0,1296):
    print(i,'irvm')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveIrvingMax()
    num_of_guessesIrvingMax[temp.num_guess]+=1
    num_of_guessesIrvingMaxstd[i]=temp.num_guess
all_guessesIrvingMax=0   
for i in range (0,8):
    all_guessesIrvingMax=all_guessesIrvingMax+i*num_of_guessesIrvingMax[i]


#%%
num_of_guessesIrving3=np.zeros(10)
num_of_guessesIrving3std=np.zeros(1296)
for i in range(0,1296):
    print(i,'irv3')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveIrving3()
    num_of_guessesIrving3[temp.num_guess]+=1
    num_of_guessesIrving3std[i]=temp.num_guess
all_guessesIrving3=0   
for i in range (0,8):
    all_guessesIrving3=all_guessesIrving3+i*num_of_guessesIrving3[i]
    
        #%%
num_of_guessesIrvingMax3=np.zeros(10)
num_of_guessesIrvingMax3std=np.zeros(1296)
for i in range(0,1296):
    print(i,'irv3m')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveIrvingMax3()
    num_of_guessesIrvingMax3[temp.num_guess]+=1
    num_of_guessesIrvingMax3std[i]=temp.num_guess
all_guessesIrvingMax3=0   
for i in range (0,8):
    all_guessesIrvingMax3=all_guessesIrvingMax3+i*num_of_guessesIrvingMax3[i]

#%%
num_of_guessesMaxPartKnuth=np.zeros(10)
num_of_guessesMaxPartKnuthstd=np.zeros(1296)
for i in range(0,1296):
    print(i,'irv3m')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveMaxPartKnuth()
    num_of_guessesMaxPartKnuth[temp.num_guess]+=1
    num_of_guessesMaxPartKnuthstd[i]=temp.num_guess
all_guessesMaxPartKnuth=0   
for i in range (0,8):
    all_guessesMaxPartKnuth=all_guessesMaxPartKnuth+i*num_of_guessesMaxPartKnuth[i]
#%%
num_of_guessesMaxPartKnuthMax=np.zeros(10)
num_of_guessesMaxPartKnuthMaxstd=np.zeros(1296)
for i in range(0,1296):
    print(i,'irv3m')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveMaxPartKnuthMax()
    num_of_guessesMaxPartKnuthMax[temp.num_guess]+=1
    num_of_guessesMaxPartKnuthMaxstd[i]=temp.num_guess
all_guessesMaxPartKnuthMax=0   
for i in range (0,8):
    all_guessesMaxPartKnuthMax=all_guessesMaxPartKnuthMax+i*num_of_guessesMaxPartKnuthMax[i]
#%%
num_of_guessesMaxPartIrving=np.zeros(10)
num_of_guessesMaxPartIrvingstd=np.zeros(1296)
for i in range(0,1296):
    print(i,'irv3m')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveMaxPartIrving()
    num_of_guessesMaxPartIrving[temp.num_guess]+=1
    num_of_guessesMaxPartIrvingstd[i]=temp.num_guess
all_guessesMaxPartIrving=0   
for i in range (0,8):
    all_guessesMaxPartIrving=all_guessesMaxPartIrving+i*num_of_guessesMaxPartIrving[i]

#%%
num_of_guessesMaxPartIrvingMax=np.zeros(10)
num_of_guessesMaxPartIrvingMaxstd=np.zeros(1296)
for i in range(0,1296):
    print(i,'irv3m') 
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveMaxPartIrvingMax()
    num_of_guessesMaxPartIrvingMax[temp.num_guess]+=1
    num_of_guessesMaxPartIrvingMaxstd[i]=temp.num_guess
all_guessesMaxPartIrvingMax=0   
for i in range (0,8):
    all_guessesMaxPartIrvingMax=all_guessesMaxPartIrvingMax+i*num_of_guessesMaxPartIrvingMax[i]
#%%
num_of_guessesMaxPartIrving3=np.zeros(10)
num_of_guessesMaxPartIrving3std=np.zeros(1296)
for i in range(0,1296):
    print(i,'irv3m')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveMaxPartIrving3()
    num_of_guessesMaxPartIrving3[temp.num_guess]+=1
    num_of_guessesMaxPartIrving3std[i]=temp.num_guess
all_guessesMaxPartIrving3=0   
for i in range (0,8):
    all_guessesMaxPartIrving3=all_guessesMaxPartIrving3+i*num_of_guessesMaxPartIrving3[i]
    
#%%
num_of_guessesMaxPartIrving3Max=np.zeros(10)
num_of_guessesMaxPartIrving3Maxstd=np.zeros(1296)
for i in range(0,1296):
    print(i,'irv3m')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveMaxPartIrving3Max()
    num_of_guessesMaxPartIrving3Max[temp.num_guess]+=1
    num_of_guessesMaxPartIrving3Maxstd[i]=temp.num_guess
all_guessesMaxPartIrving3Max=0   
for i in range (0,8):
    all_guessesMaxPartIrving3Max=all_guessesMaxPartIrving3Max+i*num_of_guessesMaxPartIrving3Max[i]
    

#%%
num_of_guessesMaxPartMaxEnt=np.zeros(10)
num_of_guessesMaxPartMaxEntstd=np.zeros(1296)
for i in range(0,1296):
    print(i,'mpme')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveMaxPartMaxEnt()
    num_of_guessesMaxPartMaxEnt[temp.num_guess]+=1
    num_of_guessesMaxPartMaxEntstd[i]=temp.num_guess
all_guessesMaxPartMaxEnt=0   
for i in range (0,8):
    all_guessesMaxPartMaxEnt=all_guessesMaxPartMaxEnt+i*num_of_guessesMaxPartMaxEnt[i]

#%%
num_of_guessesMaxPartMaxEntMax=np.zeros(10)
num_of_guessesMaxPartMaxEntMaxstd=np.zeros(1296)
for i in range(0,1296):
    print(i,'mpmem')
    temp=Mastermind(4,6,M.solutions[i].copy())
    temp.solveMaxPartMaxEntMax()
    num_of_guessesMaxPartMaxEntMax[temp.num_guess]+=1
    num_of_guessesMaxPartMaxEntMaxstd[i]=temp.num_guess
all_guessesMaxPartMaxEntMax=0   
for i in range (0,8):
    all_guessesMaxPartMaxEntMax=all_guessesMaxPartMaxEntMax+i*num_of_guessesMaxPartMaxEntMax[i]


#%% 
M1=Mastermind(4,6)
abmean=np.zeros([4,4])
abstd=np.zeros([4,4])
broj=np.zeros(1296)
a1=0
for a in [0.5,1,2]:

    b1=0
    for b in [0.5,1,2]:
        broj=np.zeros(1296)
        for i in range(0,1296):
            Mga=Mastermind(4,6,M1.all_solutions[i].copy())
            broj[i]=Mga.solveGA(a,b)
            abmean[a1,b1]=broj.mean()
            abstd[a1,b1]=broj.std()
            print(sum(broj)/(i+1),a,b,i)
        b1+=1
    a1+=1
    





        
        
        
        
          
                