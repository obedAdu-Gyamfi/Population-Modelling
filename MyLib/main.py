#!/usr/bin/env python3
"""
This script runs the population modeling for different regions in Ghana
"""


import numpy as np
from Packages import data as d
from Packages import cases as case


def main():
    wp, cp, gp, vp, ep, ap, bp, northp, uep, uwp = np.array(d.take_data())

    k0 = 5_000_000.0
    r_init = 0.1

    # Western Region
    d1 = case.RegionClass(wp, k0, r_init, 1, "western", "verhulst")
    v = d1.lmodel()
    d2 = case.RegionClass(wp, k0, r_init, 1, "western", "gompertz")
    g = d2.lmodel()
    d3 = case.RegionClass(wp, k0, r_init, 1, "western", "richard")
    ri = d3.lmodel()
    d.write_data(wp, v, g, ri, "Western")
    d.write_error_metrics(wp, v, "verhulst", "Western")
    d.write_error_metrics(wp, g, "gompertz", "Western")
    d.write_error_metrics(wp, ri, "richard", "Western")

    # Central Region
    a1 = case.RegionClass(cp, k0, r_init, 1, "central", "verhulst")
    v1 = a1.lmodel()
    a2 = case.RegionClass(cp, k0, r_init, 1, "central", "gompertz")
    g1 = a2.lmodel()
    a3 = case.RegionClass(cp, k0, r_init, 1, "central", "richard")
    ri1 = a3.lmodel()
    d.write_data(cp, v1, g1, ri1, "Central")
    d.write_error_metrics(cp, v1, "verhulst", "Central")
    d.write_error_metrics(cp, g1, "gompertz", "Central")
    d.write_error_metrics(cp, ri1, "richard", "Central")

    # Greater Accra Region
    b1 = case.RegionClass(
        gp,
        6_000_000.00,
        r_init,
        1,
        "greater accra",
        "verhulst"
        )
    v2 = b1.lmodel()
    b2 = case.RegionClass(
        gp,
        6_000_000.00,
        r_init,
        1,
        "greater accra",
        "gompertz"
        )
    g2 = b2.lmodel()
    b3 = case.RegionClass(
        gp,
        6_000_000.00,
        r_init,
        1,
        "greater accra",
        "richard"
        )
    ri2 = b3.lmodel()
    d.write_data(gp, v2, g2, ri2, "GreaterAccra")
    d.write_error_metrics(gp, v2, "verhulst", "GreaterAccra")
    d.write_error_metrics(gp, g2, "gompertz", "GreaterAccra")
    d.write_error_metrics(gp, ri2, "richard", "GreaterAccra")


    # Volta Region
    c1 = case.RegionClass(vp, k0, r_init, 1, "volta", "verhulst")
    v3 = c1.lmodel()
    c2 = case.RegionClass(vp, k0, r_init, 1, "volta", "gompertz")
    g3 = c2.lmodel()
    c3 = case.RegionClass(vp, k0, r_init, 1, "volta", "richard")
    ri3 = c3.lmodel()
    d.write_data(vp, v3, g3, ri3, "Volta")
    d.write_error_metrics(vp, v3, "verhulst", "Volta")
    d.write_error_metrics(vp, g3, "gompertz", "Volta")
    d.write_error_metrics(vp, ri3, "richard", "Volta")


    # Eastern Region
    e1 = case.RegionClass(ep, k0, r_init, 1, "eastern", "verhulst")
    v4 = e1.lmodel()
    e2 = case.RegionClass(ep, k0, r_init, 1, "eastern", "gompertz")
    g4 = e2.lmodel()
    e3 = case.RegionClass(ep, k0, r_init, 1, "eastern", "richard")
    ri4 = e3.lmodel()
    d.write_data(ep, v4, g4, ri4, "Eastern")
    d.write_error_metrics(ep, v4, "verhulst", "Eastern")
    d.write_error_metrics(ep, g4, "gompertz", "Eastern")
    d.write_error_metrics(ep, ri4, "richard", "Eastern")


    # Ashanti Region
    a1 = case.RegionClass(ap, 6_000_000.00, r_init, 1, "ashanti", "verhulst")
    v5 = a1.lmodel()
    a2 = case.RegionClass(ap, 6_000_000.00, r_init, 1, "ashanti", "gompertz")
    g5 = a2.lmodel()
    a3 = case.RegionClass(ap, 6_000_000.00, r_init, 1, "ashanti", "richard")
    ri5 = a3.lmodel()
    d.write_data(ap, v5, g5, ri5, "Ashanti")
    d.write_error_metrics(ap, v5, "verhulst", "Ashanti")
    d.write_error_metrics(ap, g5, "gompertz", "Ashanti")
    d.write_error_metrics(ap, ri5, "richard", "Ashanti")


    # Brong Ahafo Region
    b1 = case.RegionClass(bp, k0, r_init, 1, "brong ahafo", "verhulst")
    v6 = b1.lmodel()
    b2 = case.RegionClass(bp, k0, r_init, 1, "brong ahafo", "gompertz")
    g6 = b2.lmodel()
    b3 = case.RegionClass(bp, k0, r_init, 1, "brong ahafo", "richard")
    ri6 = b3.lmodel()
    d.write_data(bp, v6, g6, ri6, "BrongAhafo")
    d.write_error_metrics(bp, v6, "verhulst", "BrongAhafo")
    d.write_error_metrics(bp, g6, "gompertz", "BrongAhafo")
    d.write_error_metrics(bp, ri6, "richard", "BrongAhafo")


    # Northern Region
    n1 = case.RegionClass(northp, k0, r_init, 1, "northern", "verhulst")
    v7 = n1.lmodel()
    n2 = case.RegionClass(northp, k0, r_init, 1, "northern", "gompertz")
    g7 = n2.lmodel()
    n3 = case.RegionClass(northp, k0, r_init, 1, "northern", "richard")
    ri7 = n3.lmodel()
    d.write_data(northp, v7, g7, ri7, "Northern")
    d.write_error_metrics(northp, v7, "verhulst", "Northern")
    d.write_error_metrics(northp, g7, "gompertz", "Northern")
    d.write_error_metrics(northp, ri7, "richard", "Northern")


    # Upper East
    u1 = case.RegionClass(uep, k0, r_init, 1, "upper east", "verhulst")
    v8 = u1.lmodel()
    u2 = case.RegionClass(uep, k0, r_init, 1, "upper east", "gompertz")
    g8 = u2.lmodel()
    u3 = case.RegionClass(uep, k0, r_init, 1, "upper east", "richard")
    ri8 = u3.lmodel()
    d.write_data(uep, v8, g8, ri8, "UpperEast")
    d.write_error_metrics(uep, v8, "verhulst", "UpperEast")
    d.write_error_metrics(uep, g8, "gompertz", "UpperEast")
    d.write_error_metrics(uep, ri8, "richard", "UpperEast")


    # Upper West
    uw1 = case.RegionClass(uwp, k0, r_init, 1, "upper west", "verhulst")
    v9 = uw1.lmodel()
    uw2 = case.RegionClass(uwp, k0, r_init, 1, "upper west", "gompertz")
    g9 = uw2.lmodel()
    uw3 = case.RegionClass(uwp, k0, r_init, 1, "upper west", "richard")
    ri9 = uw3.lmodel()
    d.write_data(uwp, v9, g9, ri9, "UpperWest")
    d.write_error_metrics(uwp, v9, "verhulst", "UpperWest")
    d.write_error_metrics(uwp, g9, "gompertz", "UpperWest")
    print("Population modeling completed successfully.")


if __name__ == "__main__":
    main()
