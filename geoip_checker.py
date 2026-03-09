import geoip2.database

suspicious_countries = ["Russia", "China", "North Korea"]

def check_country(ip):

    try:
        reader = geoip2.database.Reader("GeoLite2-City.mmdb")
        response = reader.city(ip)
        country = response.country.name

        if country in suspicious_countries:
            print(f"Suspicious country login attempt from {ip} ({country})")

    except:
        pass