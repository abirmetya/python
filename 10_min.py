Content-Type: text/enriched
Text-Width: 70

'''
This code is able to calculate average of any time (i.e. 1min,
30 min, 1 hour, 1 day etc.) from a high frequency dataset- 
like- per second data, given in a text format '''


### <x-color><param>Firebrick</param>Created by- Abirlal Metya (27-AUG-2018)

</x-color>

#<x-color><param>Firebrick</param>import pandas as pd
</x-color>#<x-color><param>Firebrick</param>import numpy as np

</x-color>

'''
data=pd.io.parsers.read_csv('jun_co2_dry.dat')
data.shape
data[1:10]


#date=pd.io.parsers.read_csv('jun_dates.dat')
dd=pd.read_csv('jun_dates.dat',parse_dates=[0],index_col=[0])
dd.shape
dd[0:10]


#dd=np.concatenate((dd,data),axis=1)


ddd=pd.concat((dd,data),axis=1)
sum=ddd.resample('30Min').sum()
#dddd=(dd.set_index('timestamps'))


'''
<x-color><param>Purple</param>import</x-color> pandas <x-color><param>Purple</param>as</x-color> pd


<x-color><param>sienna</param>dd</x-color>=pd.read_csv(<x-color><param>VioletRed4</param>'jun_dates.dat'</x-color>)


<x-color><param>sienna</param>data</x-color>=pd.read_csv(<x-color><param>VioletRed4</param>'jun_co2_dry.dat'</x-color>)


<x-color><param>sienna</param>peakflow</x-color>=pd.concat((dd,data),axis=1)


<x-color><param>sienna</param>peakflow</x-color>[<x-color><param>VioletRed4</param>'Datetime'</x-color>] = pd.to_datetime(peakflow.Datetime)


peakflow.set_index(<x-color><param>VioletRed4</param>'Datetime'</x-color>, inplace=<x-color><param>dark cyan</param>True</x-color>)  
<x-color><param>sienna</param>peakflow.index</x-color> = pd.to_datetime(peakflow.index)    
<x-color><param>sienna</param>min_1</x-color>=peakflow.resample(rule = <x-color><param>VioletRed4</param>'1Min'</x-color>).mean()
<x-color><param>sienna</param>min_30</x-color>=peakflow.resample(rule=<x-color><param>VioletRed4</param>'30Min'</x-color>).mean()
<x-color><param>sienna</param>day_1</x-color>=peakflow.resample(rule=<x-color><param>VioletRed4</param>'1D'</x-color>).mean()



   

   

   

   


