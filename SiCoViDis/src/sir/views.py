
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from itertools import product

def sir(request):
	return render(request,"sir.html")


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        sepal_length = float(request.POST.get('sucep1'))
        suceptibles = float(request.POST.get('sepal_length'))
        recovered = float(request.POST.get('petal_length'))
        time = str(request.POST.get('petal_width'))
        
        beta = 0.16793
        gamma = 0.0378
        S0=suceptibles
        R0 = recovered
        I0=sepal_length
        t0=0
        t1=100
    #def SIR(S0,I0,R0,t0, t1, beta, gamma):
        N=S0+R0+I0; #initialization
        S=S0; 
        R=R0; 
        I=I0;
        
        SS=[S0]; #updating the function
        RR=[R0]; 
        II=[I0];
        tt=[t0];
        
        dt=1; #time step
        t=t0
        
        State = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chattisgarh',  'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Jammu Kashmir', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharastra', 'Punjab', 'Rajasthan', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarkhand','West Bengal']

 

        beta_all= [0.1886, 0.4279, 0.26218,0.27587, 0.35894, 0.311457, 0.422205, 0.223834, 0.517132, 0.543636, 0.156651, 0.23459, 0.305371, 0.144906, 0.281642, 0.236326, 0.257371, 0.387441, 0.211837, 0.314778, 0.106325, 0.082836]

 

        gamma_all = [0.017403, 0.07614, 0.05717, 0.03675, 0.05753, 0.042076, 0.097788, 0.08258, 0.111523, 0.161885, 0.02344, 0.091493, 0.07342, 0.0796, 0.0466199, 0.01789, 0.05313, 0.06771, 0.01594, 0.093505, 0.0305335, 0.020959]

        for i in range(len(State)):
            if State[i] == time:
                beta = beta_all[i]
                gamma = gamma_all[i]


        while t <= t1:
            dS=-beta*S*I/N
            dI=beta*S*I/N-gamma*I
            dR=gamma*I
            S=S+dt*dS;
            I=I+dt*dI;
            R=R+dt*dR;
            SS.append(S); II.append(I); RR.append(R)
            t=t+dt;
            tt.append(t)
        #return(SS,II,RR,tt)
        oo=II.index(max(II));
        N=(II[0]+RR[0]+SS[0]);
        tmax=tt[oo]; Imax=II[oo];
        inftot = RR[-1]/N;

        tmax, Imax/N*100,inftot*100
            
                
                
        return JsonResponse({'sepal_length': int(Imax/N*100) ,
                                'sepal_width': tmax,'petal_length': int(inftot*100)})


    