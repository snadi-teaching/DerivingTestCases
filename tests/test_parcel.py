import pytest
from parcel_mgmt.parcel import Parcel, ship_parcel


@pytest.mark.parametrize(
    "test_id, parcel, expected",
    [
        (1, Parcel("P001", 5.0, "USA"), "Shipped"),
        (2, Parcel("P002", 10.0, "Canada"), "Shipped"),
        (3, Parcel("P003", 2.5, "Italy"), "Invalid Destination")
    ],
    ids=lambda x: x,
)
def test_ship_parcel(test_id, parcel, expected):
    assert ship_parcel(parcel) == expected
