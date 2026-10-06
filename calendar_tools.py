"""Reconciling price series that cover different sets of dates.

Exchanges run different holiday calendars and vendors drop days, so two price
series rarely cover exactly the same dates. Pairing them by position silently
misaligns everything after the first gap. These functions compare date coverage
explicitly and report what is usable.
""" 

def sym_diff(a, b):
    """Returns the dates present in exactly on of the sets.

    Built from difference and union only, as a check on the built in.
    """
    return (a - b) | (b - a)

def common_calendar(*dates_sets): 
    """Returns the dates of present in every set"""
    if not dates_sets: 
        return set()
    common = dates_sets[0]
    for s in dates_sets[1:]:
        common = common & s 
    return common 

def coverage_report(required, series_by_name):
    """Compare required dates to what each series actually has.

    required: set of dates the model needs.
    series_by_name: dict of {name: set_of_dates}

    Returns (usable, missing_by_name).
    """
    all_sets = list(series_by_name.values())
    usable = required & common_calendar(*all_sets)

    missing = {}
    for name, dates in series_by_name.items():
        missing[name] = required - dates
    return usable, missing
    


if __name__ == "__main__":

    A = {"2026-05-04", "2026-05-05", "2026-05-06"}
    B = {"2026-05-05", "2026-05-06", "2026-05-07"}    

    brent_days = {"2026-05-01", "2026-05-05", "2026-05-06", "2026-05-07", "2026-05-08"}
    rbob_days  = {"2026-05-01", "2026-05-04", "2026-05-05", "2026-05-07", "2026-05-08"}

    required = {"2026-05-01", "2026-05-04", "2026-05-05",
                "2026-05-06", "2026-05-07", "2026-05-08"}
    series = {"brent": brent_days, "rbob": rbob_days}


    
    print(A | B)
    print(A & B)
    print(A - B)
    print(B - A)
    print(A ^ B)
    print("2026-05-05" in B)
    print(set() <= A)
    
    assert sym_diff(A, B) == A.symmetric_difference(B)
    assert sym_diff(A, B) == A^B
    assert sym_diff({"x"}, {"y"}) == {"x", "y"}

    print(sorted(common_calendar(brent_days, rbob_days)))
    print(sorted(sym_diff(brent_days, rbob_days)))

    usable, missing = coverage_report (required, series)
    print(sorted(usable))
    for name, dates in missing.items():
        if dates:
            print(f"{name} missing {sorted(dates)}")
