import datetime
from datetime import date,time, timedelta,datetime


now = datetime.now()
hour = now.hour
minute = now.minute
day_of_week =  now.weekday()


if day_of_week != 5 or day_of_week != 6:
 
    if 8 <= hour < 16:
        new_hour  = hour +1
        print(f'Resposta hoje até {new_hour}:{minute}h')
        
    elif hour == 16: 
        new_hour ='08'
        print( 'Resposta até  amanhã às 'f'{new_hour}:{minute}h')
    else:    
        print('Resposta até amanha às 09:00' )

else:
    print('Oferta feita no final de semana,resposta até 9:00h de segunda-feira')

    

#-----