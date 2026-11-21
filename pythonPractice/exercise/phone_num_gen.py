#phone number generator

#country = country code (+1,+4, +8 , etc..)
def get_phone(country, area, first, last):
    return(f"{country}-{area}-{first}-{last}")

phone_num = get_phone(country= 1, area = 288, first= 338, last= 8558 )