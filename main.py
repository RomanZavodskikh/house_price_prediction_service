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
def predict_page(host_id = 0, host_since = 0, host_is_superhost = False,
    host_has_profile_pic = False, host_identity_verified = False,
    is_location_exact = False, require_guest_profile_picture = False,
    require_guest_phone_verification = False,
    latitude = 0, longitude = 0, accommodates = 0,
    bathrooms = 0, bedrooms = 0, beds = 0,
    square_feet = 0, security_deposit = 0, cleaning_fee = 0,
    guests_included = 0, extra_people = 0, minimum_nights = 0,
    predicted_price = ""):
    if request.method == "POST":
        host_id = int(request.form["host_id"])
        host_since = int(request.form["host_since"])
        host_is_superhost = int(bool(request.form.get("host_is_superhost")))
        host_has_profile_pic = int(bool(request.form.get("host_has_profile_pic")))
        host_identity_verified = int(bool(request.form.get("host_identity_verified")))
        is_location_exact = int(bool(request.form.get("is_location_exact")))
        require_guest_profile_picture = int(bool(request.form.get("require_guest_profile_picture")))
        require_guest_phone_verification = int(bool(request.form.get("require_guest_phone_verification")))
        latitude = int(request.form["latitude"])
        longitude = int(request.form["longitude"])
        accommodates = int(request.form["accommodates"])
        bathrooms = int(request.form["bathrooms"])
        bedrooms = int(request.form["bedrooms"])
        beds = int(request.form["beds"])
        square_feet = int(request.form["square_feet"])
        security_deposit = int(request.form["security_deposit"])
        cleaning_fee = int(request.form["cleaning_fee"])
        guests_included = int(request.form["guests_included"])
        extra_people = int(request.form["extra_people"])
        minimum_nights = int(request.form["minimum_nights"])

        logfile = open("hata_otsenyator_logs.txt", "ab", "utf-8")
        logfile.write("<response>\n")

        predicted_price = regressor.predict_price(
                [[host_id, host_since, host_is_superhost, host_has_profile_pic,
                host_identity_verified, is_location_exact,
                require_guest_profile_picture, require_guest_phone_verification,
                latitude, longitude, accommodates, bathrooms,
                bedrooms, beds,
                square_feet, security_deposit, cleaning_fee,
                guests_included, extra_people, minimum_nights]]
        )
        predicted_price = round(predicted_price, 2)

        logfile.write(str(predicted_price))
        logfile.write("<response>\n")
        logfile.close()

    return render_template('simple_page.html', host_id = host_id,
        host_since = host_since, host_is_superhost = host_is_superhost,
        host_has_profile_pic = host_has_profile_pic,
        host_identity_verified = host_identity_verified,
        is_location_exact = is_location_exact,
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
