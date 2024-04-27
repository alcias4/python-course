




class Coordenas:
    def __init__(self, lat , lon):
        self.lat = lat
        self.lon = lon
    
    def __eq__(self, otro): # sirve para comprar clases
        return self.lat == otro.lat and self.lon == otro.lon
    
    def __lt__(self, otro): # cuando se compare cuando uno del otro <>
        return self.lat + self.lon < otro.lat + otro.lon

    def __le__(self, otro):# cuando se compare cuando uno del otro <=
        return self.lat + self.lon <= otro.lat + otro.lon

       
coords = Coordenas(44, 47)
coords2  = Coordenas(45, 47)

print(coords <= coords2)