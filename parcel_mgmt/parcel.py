class Parcel:
    def __init__(self, parcel_id, weight, destination):
        self.parcel_id = parcel_id
        self.weight = weight
        self.destination = destination


def normalize_destination(destination):

    if destination in ["USA", "Canada"]:
        return destination  # nothing to normalize

    if destination.lower() in [
        "usa",
        "us",
        "united states",
        "united states of america",
    ]:
        return "USA"

    if destination.lower() in ["ca", "can", "canada"]:
        return "Canada"


def ship_parcel(parcel):

    destination = normalize_destination(parcel.destination)

    if destination not in ["USA", "Canada"]:
        return "Invalid Destination"

    else:
        print("Doing the shipping ")  # do whatever you need to do
        return "Shipped"
