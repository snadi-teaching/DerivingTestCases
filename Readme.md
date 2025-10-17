# Derviving test cases

This repo has simple code to illustrate how deriving test cases using blackbox/functional testing differs from deriving test cases using whitebox/structural testing.

# Specification

Here is the specification we are working with.

```
For distribution purporses, the system shall label each parcel based on its weight and destination according to the following rules:


For Local destinations:

* Parcels weighing less than or equal to 1 kg shall be categorized as "Letter (Local)".
* Parcels weighing more than 1 kg and up to 5 kg shall be categorized as "Small Parcel (Local)".
* Parcels weighing more than 5 kg and up to 20 kg shall be categorized as "Parcel (Local)".

For International destinations:
* Parcels weighing less than or equal to 0.5 kg shall be categorized as "Letter (Intl)".
* Parcels weighing more than 0.5 kg and up to 2 kg shall be categorized as "Small Parcel (Intl)".
* Parcels weighing more than 2 kg and up to 10 kg shall be categorized as "Parcel (Intl)".
```