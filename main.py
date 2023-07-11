import geocoder
import ephem


def get_current_location():
    g = geocoder.ip('me')
    if g.latlng:
        return g.latlng
    else:
        return None

location = get_current_location()
if location:
    ulatitude, ulongitude = location
    print(f"Latitude: {ulatitude}, Longitude: {ulongitude}")
else:
    print("Unable to retrieve current location.")


# root.mainloop()