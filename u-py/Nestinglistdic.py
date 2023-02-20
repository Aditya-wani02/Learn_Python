# Nesting 

capitals ={
    "France": "Paris",
    "Germany": "Berlin"
}

# travel_log ={
#     "France":{ "city_visited": ["paris", "lille" ,"Dijon"] , "total_visits":12 },
#     "Germany":{ "city_visited": ["Barlin","Hamburg","Stuttgrat"] ,"total_visits":5}
# }


travel_log = [
    {"country":"France" ,
    "city": ["paris", "lille" ,"Dijon"] ,
     "visits": 12 
    },
    {"country":"Germany" ,
    "city": ["Barlin","Hamburg","Stuttgrat"] ,
    "visits":5
    },
] 


def add_new_country(country,visits,city):
    new_country={}
    new_country["country"]=country
    new_country["visits"]=visits
    new_country["city"]=city
    travel_log.append(new_country)

add_new_country("Russia",2,["Moscow","Saint petersburg"])
print(travel_log)



