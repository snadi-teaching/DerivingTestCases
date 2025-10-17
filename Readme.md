# Derviving test cases

This repo has simple code to illustrate how deriving test cases using blackbox/functional testing differs from deriving test cases using whitebox/structural testing.

# Running instructions

- create your virtual environment `python -m venv .venv`
- activate the virtual environment `source .venv/bin/activate`
- install requirements `pip install -r requirements.txt`
- run tests `pytest`

# Specification

Here is the specification we are working with.

```
The system shall ship parcels only to the USA or Canada.
```

# Deriving test cases using blackbox testing

If we use equivalence class partitioning, we come up with two classes:

- ["USA", "CANADA"] (valid to ship)
- anything not in ["USA", "CANADA"] (invalid to ship)

Now, you are actually provided with an implementation of this parcel destination checking knowledge. Don't look at the implementation yet.
We now implement the above test cases in tests/test_parcel.py .

Run the tests using `pytest`. Your tests pass. Yay!

# Deriving test cases using whitebox testing

So far we have considered only the specification/functional description to decide on what test cases to include. We did not have to look at *how* the functionality was implemented in the code. We treated the code as a black box.

Now let's start looking into the code. Let's assess our current coverage:

```
pytest --cov=parcel_mgmt --cov-branch
coverage html
```
You will see that the coverage is below 100% and if you look at the html report, you will see what's missing. 

As part of the implementation, the developer included some normalization logic in case the user enters different capitalizations. Because this is an implementation-specific detail, we never thought of it while looking only at the spec.

With whitebox testing, our goal is to make sure we exercise all parts of the code.

Accordingly, in line 10 of the test file, we can add the following test cases to the list of test cases:

``
(4, Parcel("P004", 7.0, "Usa"), "Shipped"),
(5, Parcel("P005", 3.0, "Ca"), "Shipped"),
 ```

 Now, if you run coverage again, you should get 100%.