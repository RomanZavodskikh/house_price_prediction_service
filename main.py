from regressor import Regressor
from codecs import open
import time
from flask import Flask, render_template, request
app = Flask(__name__)

print("Load regressor")
start_time = time.time()
regressor = Regressor()
print("Regressor is successfully loaded")
print(time.time() - start_time, "seconds")

@app.route("/", methods = ["GET"])
def index_page():
    return render_template('index.html')

@app.route("/predict-hata-price", methods = ["POST", "GET"])
def predict_page(host_is_superhost = False,
    host_has_profile_pic = False, host_identity_verified = False,
    require_guest_profile_picture = False,
    require_guest_phone_verification = False,
    latitude = 51.5423, longitude = -0.1285, accommodates = "",
    bathrooms = "", bedrooms = "", beds = "",
    square_feet = "", security_deposit = "", cleaning_fee = "",
    guests_included = "", extra_people = "", minimum_nights = "",
    predicted_price = ""):
    if request.method == "POST":
        host_is_superhost = int(bool(request.form.get("host_is_superhost")))
        host_has_profile_pic = int(bool(request.form.get("host_has_profile_pic")))
        host_identity_verified = int(bool(request.form.get("host_identity_verified")))
        require_guest_profile_picture = int(bool(request.form.get("require_guest_profile_picture")))
        require_guest_phone_verification = int(bool(request.form.get("require_guest_phone_verification")))
        latitude = float(request.form.get("latitude"))
        longitude = float(request.form.get("longitude"))
        accommodates = int(request.form.get("accommodates"))
        bathrooms = int(request.form.get("bathrooms"))
        bedrooms = int(request.form.get("bedrooms"))
        beds = int(request.form.get("beds"))
        square_feet = int(request.form.get("square_feet"))
        security_deposit = int(request.form.get("security_deposit"))
        cleaning_fee = int(request.form.get("cleaning_fee"))
        guests_included = int(request.form.get("guests_included"))
        extra_people = int(request.form.get("extra_people"))
        minimum_nights = int(request.form.get("minimum_nights"))

        logfile = open("hata_otsenyator_logs.txt", "ab", "utf-8")
        logfile.write("<response>\n")

        predicted_price = regressor.predict_price(
                [[host_is_superhost, host_has_profile_pic,
                host_identity_verified, 1, # consider location is always exact
                require_guest_profile_picture, require_guest_phone_verification,
                latitude, longitude, accommodates, bathrooms,
                bedrooms, beds,
                square_feet, security_deposit, cleaning_fee,
                guests_included, extra_people, minimum_nights]]
        )

        logfile.write(str(predicted_price))
        logfile.write("<response>\n")
        logfile.close()

    time.sleep(3)
    return render_template('simple_page.html',
        host_is_superhost = host_is_superhost,
        host_has_profile_pic = host_has_profile_pic,
        host_identity_verified = host_identity_verified,
        require_guest_profile_picture = require_guest_profile_picture,
        require_guest_phone_verification = require_guest_phone_verification,
        latitude = latitude, longitude = longitude, accommodates = accommodates,
        bathrooms = bathrooms, bedrooms = bedrooms, beds = beds, square_feet = square_feet,
        security_deposit = security_deposit, cleaning_fee = cleaning_fee,
        guests_included = guests_included, extra_people = extra_people,
        minimum_nights = minimum_nights,
        predicted_price = predicted_price)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 44445, debug = True)
