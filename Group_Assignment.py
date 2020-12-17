"""
This program is to return the correct zodiac signs for 
the given birth month and day.
First we define what the zodiac signs day and month is. 
we check to see what month it falls in, and determine the 
day within the day that it cuts off.
if the month is "december", then the astro sign is Sagittarius.
    if the day is < 22 then the result will be Capricorn.
if the month is "January", then the astro sign is Capricorn.
    if the day is < 20 then the result will be Aquarius.
if the month is "Febuary", then the astro sign is Aquarius.
    if the day is < 19 then the result will be Pisces.
if the month is "March", then the astro sign is Pisces.
    if the day is < 21 then the result will be Aries.
if the month is "April", then the astro sign is Aries.
    if the day is < 20 then the result will be Taurus.
if the month is "May", then the astro sign is Taurus.
    if the day is < 21 then the result will be Gemini.
if the month is "June", then the astro sign is Gemini.
    if the day is < 22 then the result will be Cancer.
if the month is "July", then the astro sign is Cancer.
    if the day is < 22 then the result will be Leo.
if the month is "August", then the astro sign is Leo.
    if the day is < 22 then the result will be Virgo.
if the month is "September", then the astro sign is Virgo.
    if the day is < 22 then the result will be Libra.
if the month is "October", then the astro sign is Libra.
    if the day is < 22 then the result will be Scorpio.
if the month is "November", then the astro sign is Scorpio.
    if the day is <22 then the result will be sagittarius.
"""

"""
if month = 'December'
    then astro_sign = 'Satittarus'
    if else day < 22 results ='Capricorn'
if month = 'Januaray'
    then astro_sign = 'Capricorn'
    if else day < 20 results ='Aquarius'
if month = 'Febuary'
    then astro_sign = 'Satittarus'
    if else day < 19 results ='Capricorn'
if month = 'March'
    then astro_sign = 'Satittarus'
    if else day < 21 results ='Capricorn'
if month = 'April'
    then astro_sign = 'Satittarus'
    if else day < 20 results ='Capricorn'
if month = 'May'
    then astro_sign = 'Satittarus'
    if else day < 21 results ='Capricorn'
if month = 'June'
    then astro_sign = 'Satittarus'
    if else day < 21 results ='Capricorn'
if month = 'July'
    then astro_sign = 'Satittarus'
    if else day < 23 results ='Capricorn'
if month = 'August'
    then astro_sign = 'Satittarus'
    if else day < 23 results ='Capricorn'
if month = 'September'
    then astro_sign = 'Satittarus'
    if else day < 23 results ='Capricorn'
if month = 'October'
    then astro_sign = 'Satittarus'
    if else day < 23 results ='Capricorn'
if month = 'November'
    then astro_sign = 'Satittarus'
    if else day < 22 results ='Capricorn'

Print 
"""

def zodiac_sign(day, month): 
      
    if month == 'december': 
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
          
    elif month == 'january': 
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
          
    elif month == 'february': 
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
          
    elif month == 'march': 
        astro_sign = 'Pisces' if (day < 21) else 'aries'
          
    elif month == 'april': 
        astro_sign = 'Aries' if (day < 20) else 'taurus'
          
    elif month == 'may': 
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
          
    elif month == 'june': 
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
          
    elif month == 'july': 
        astro_sign = 'Cancer' if (day < 23) else 'leo'
          
    elif month == 'august': 
        astro_sign = 'Leo' if (day < 23) else 'virgo'
          
    elif month == 'september': 
        astro_sign = 'Virgo' if (day < 23) else 'libra'
          
    elif month == 'october': 
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
          
    elif month == 'november': 
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
          
    print(astro_sign) 
      
 
if __name__ == '__main__': 
    day = 16
    month = "october"
    zodiac_sign(day , month) 

