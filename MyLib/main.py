#!/usr/bin/env python3
"""
This script runs the population modeling for different regions in Ghana
"""
import numpy as np
from Packages import data as d
from Packages import cases as case
from Packages import db as db


def main():
    wp, cp, gp, vp, ep, ap, bp, northp, uep, uwp = np.array(d.take_data())
    year = np.array((1960, 1970, 1984, 2000, 2010))
    k0 = 5_000_000.0
    r_init = 0.1

    #Ashanti Region
    Ash1 = case.RegionClass(ap, k0, r_init, 1, "verhulst")
    vASH,vASHparams = Ash1.lmodel()
    Ash2 = case.RegionClass(ap, k0, r_init, 1, "gompertz")
    gASH,gASHparams = Ash2.lmodel()
    Ash3 = case.RegionClass(ap, k0, r_init, 1, "richard")
    rASH,rASHparams = Ash3.lmodel()
    vError = d.write_error(ap, vASH, "verhulst")
    gError = d.write_error(ap, gASH, "gompertz")
    rError = d.write_error(ap, rASH, "richard")
    ashdata = {
        "region": [
            {
                "id": 1,
                "name": "Ashanti",
                "model": [
                    {"Verhulst": vASH},
                    {"Gompertz": gASH},
                    {"Richard": rASH}
                    ],
                "Parameters": [
                    {"verhulst": vASHparams},
                    {"gompertz": gASHparams},
                    {"richard": rASHparams}
                    ],
                "Errors": [
                    {"verhulst": vError},
                    {"gompertz": gError},
                    {"richard": rError}
                    ]
            }
        ],
        "orgData":
            {
            "year": year.tolist(),
            "population": ap.tolist()
            }    
    }
    db.create_db(ashdata)
    d.write_data(ap, vASH, gASH, rASH, "Ashanti")

    #Brong Ahafo Region
    BA1 = case.RegionClass(bp, k0, r_init, 1, "verhulst")
    vBA,vBAparams = BA1.lmodel()
    BA2 = case.RegionClass(bp, k0, r_init, 1, "gompertz")
    gBA,gBAparams = BA2.lmodel()
    BA3 = case.RegionClass(ap, k0, r_init, 1, "richard")
    rBA,rBAparams = BA3.lmodel()
    vError = d.write_error(bp, vBA, "verhulst")
    gError = d.write_error(bp, gBA, "gompertz")
    rError = d.write_error(bp, rBA, "richard")
    badata = {
        "region": [
            {
                "id": 2,
                "name": "Brong Ahafo",
                "model": [
                    {"Verhulst": vBA},
                    {"Gompertz": gBA},
                    {"Richard": rBA}
                    ],
                "Parameters": [
                    {"verhulst": vBAparams},
                    {"gompertz": gBAparams},
                    {"richard": rBAparams}
                    ],
                "Errors": [
                    {"verhulst": vError},
                    {"gompertz": gError},
                    {"richard": rError}
                    ]
            }
        ],
        "orgData":
            {
            "year": year.tolist(),
            "population": bp.tolist()
            }    
    }
    db.add_to_db(badata)
    d.write_data(bp, vBA, gBA, rBA , "Brong Ahafo")

    #Central Region
    CENT1 = case.RegionClass(cp, k0, r_init, 1, "verhulst")
    vCENT,vCENTparams = CENT1.lmodel()
    CENT2 = case.RegionClass(cp, k0, r_init, 1, "gompertz")
    gCENT,gCENTparams = CENT2.lmodel()
    CENT3 = case.RegionClass(cp, k0, r_init, 1, "richard")
    rCENT,rCENTparams = CENT3.lmodel()
    vError = d.write_error(cp, vCENT, "verhulst")
    gError = d.write_error(cp, gCENT, "gompertz")
    rError = d.write_error(cp, rCENT, "richard")
    cdata = {
        "region": [
            {
                "id": 3,
                "name": "Central",
                "model": [
                    {"Verhulst": vCENT},
                    {"Gompertz": gCENT},
                    {"Richard": rCENT}
                    ],
                "Parameters": [
                    {"verhulst": vCENTparams},
                    {"gompertz": gCENTparams},
                    {"richard": rCENTparams}
                    ],
                "Errors": [
                    {"verhulst": vError},
                    {"gompertz": gError},
                    {"richard": rError}
                    ]
            }
        ],
        "orgData":
            {
            "year": year.tolist(),
            "population": cp.tolist()
            }    
    }
    db.add_to_db(cdata)
    d.write_data(cp, vCENT, gCENT, rCENT, "Central")

    #Eastern Region
    EST1 = case.RegionClass(ep, k0, r_init, 1, "verhulst")
    vEST,vESTparams = EST1.lmodel()
    EST2 = case.RegionClass(ep, k0, r_init, 1, "gompertz")
    gEST,gESTparams = EST2.lmodel()
    EST3 = case.RegionClass(ep, k0, r_init, 1, "richard")
    rEST,rESTparams = EST3.lmodel()
    vError = d.write_error(ep, vEST, "verhulst")
    gError = d.write_error(ep, gEST, "gompertz")
    rError = d.write_error(ep, rEST, "richard")
    edata = {
        "region": [
            {
                "id": 4,
                "name": "Eastern",
                "model": [
                    {"Verhulst": vEST},
                    {"Gompertz": gEST},
                    {"Richard": rEST}
                    ],
                "Parameters": [
                    {"verhulst": vESTparams},
                    {"gompertz": gESTparams},
                    {"richard": rESTparams}
                    ],
                "Errors": [
                    {"verhulst": vError},
                    {"gompertz": gError},
                    {"richard": rError}
                    ]
            }
        ],
        "orgData":
            {
            "year": year.tolist(),
            "population": ep.tolist()
            }    
    }
    db.add_to_db(edata)
    d.write_data(ep, vEST, gEST, rEST, "Eastern")

    #Greater Accra Region
    GA1 = case.RegionClass(gp, k0, r_init, 1, "verhulst")
    vGA,vGAparams = GA1.lmodel()
    GA2 = case.RegionClass(gp, k0, r_init, 1, "gompertz")
    gGA,gGAparams = GA2.lmodel()
    GA3 = case.RegionClass(gp, k0, r_init, 1, "richard")
    rGA,rGAparams = GA3.lmodel()
    vError = d.write_error(gp, vGA, "verhulst")
    gError = d.write_error(gp, gGA, "gompertz")
    rError = d.write_error(gp, rGA, "richard")
    adata = {
        "region": [
            {
                "id": 5,
                "name": "Greater Accra",
                "model": [
                    {"Verhulst": vGA},
                    {"Gompertz": gGA},
                    {"Richard": rGA}
                    ],
                "Parameters": [
                    {"verhulst": vGAparams},
                    {"gompertz": gGAparams},
                    {"richard": rGAparams}
                    ],
                "Errors": [
                    {"verhulst": vError},
                    {"gompertz": gError},
                    {"richard": rError}
                    ]
            }
        ],
        "orgData":
            {
            "year": year.tolist(),
            "population": gp.tolist()
            }    
    }
    db.add_to_db(adata)
    d.write_data(gp, vGA, gGA, rGA, "Greater Accra")

    #Northen Region
    NORTH1 = case.RegionClass(northp, k0, r_init, 1, "verhulst")
    vNORTH,vNORTHparams = NORTH1.lmodel()
    NORTH2 = case.RegionClass(northp, k0, r_init, 1, "gompertz")
    gNORTH,gNORTHparams = NORTH2.lmodel()
    NORTH3 = case.RegionClass(northp, k0, r_init, 1, "richard")
    rNORTH,rNORTHparams = NORTH3.lmodel()
    vError = d.write_error(northp, vNORTH, "verhulst")
    gError = d.write_error(northp, gNORTH, "gompertz")
    rError = d.write_error(northp, rNORTH, "richard")
    ndata = {
        "region": [
            {
                "id": 6,
                "name": "Northern",
                "model": [
                    {"Verhulst": vNORTH},
                    {"Gompertz": gNORTH},
                    {"Richard": rNORTH}
                    ],
                "Parameters": [
                    {"verhulst": vNORTHparams},
                    {"gompertz": gNORTHparams},
                    {"richard": rNORTHparams}
                    ],
                "Errors": [
                    {"verhulst": vError},
                    {"gompertz": gError},
                    {"richard": rError}
                    ]
            }
        ],
        "orgData":
            {
            "year": year.tolist(),
            "population": northp.tolist()
            }    
    }
    db.add_to_db(ndata)
    d.write_data(northp, vNORTH, gNORTH, rNORTH, "Northern")
    
    #Upper East Region
    UET1 = case.RegionClass(uep, k0, r_init, 1, "verhulst")
    vUET,vUETparams = UET1.lmodel()
    UET2 = case.RegionClass(uep, k0, r_init, 1, "gompertz")
    gUET,gUETparams = UET2.lmodel()
    UET3 = case.RegionClass(uep, k0, r_init, 1, "richard")
    rUET,rUETparams = UET3.lmodel()
    vError = d.write_error(uep, vUET, "verhulst")
    gError = d.write_error(uep, gUET, "gompertz")
    rError = d.write_error(uep, rUET, "richard")
    udata = {
        "region": [
            {
                "id": 7,
                "name": "Upper East",
                "model": [
                    {"Verhulst": vUET},
                    {"Gompertz": gUET},
                    {"Richard": rUET}
                    ],
                "Parameters": [
                    {"verhulst": vUETparams},
                    {"gompertz": gUETparams},
                    {"richard": rUETparams}
                    ],
                "Errors": [
                    {"verhulst": vError},
                    {"gompertz": gError},
                    {"richard": rError}
                    ]
            }
        ],
        "orgData":
            {
            "year": year.tolist(),
            "population": uep.tolist()
            }    
    }
    db.add_to_db(udata)
    d.write_data(uep,  vUET, gUET, rUET, "Upper East")

    #Upper West Region
    UWT1 = case.RegionClass(uwp, k0, r_init, 1, "verhulst")
    vUWT,vUWTparams = UWT1.lmodel()
    UWT2 = case.RegionClass(uwp, k0, r_init, 1, "gompertz")
    gUWT,gUWTparams = UWT2.lmodel()
    UWT3 = case.RegionClass(uwp, k0, r_init, 1, "richard")
    rUWT,rUWTparams = UWT3.lmodel()
    vError = d.write_error(uwp, vUWT, "verhulst")
    gError = d.write_error(uwp, gUWT, "gompertz")
    rError = d.write_error(uwp, rUWT, "richard")
    uwdata = {
        "region": [
            {
                "id": 8,
                "name": "Upper West",
                "model": [
                    {"Verhulst": vUWT},
                    {"Gompertz": gUWT},
                    {"Richard": rUWT}
                    ],
                "Parameters": [
                    {"verhulst": vUWTparams},
                    {"gompertz": gUWTparams},
                    {"richard": rUWTparams}
                    ],
                "Errors": [
                    {"verhulst": vError},
                    {"gompertz": gError},
                    {"richard": rError}
                    ]
            }
        ],
        "orgData":
            {
            "year": year.tolist(),
            "population": uwp.tolist()
            }    
    }
    db.add_to_db(uwdata)
    d.write_data(uwp, vUWT, gUWT, rUWT, "Upper West")

    #Volta Region
    VOLTA1 = case.RegionClass(vp, k0, r_init, 1, "verhulst")
    vVOLTA,vVOLTAparams = VOLTA1.lmodel()
    VOLTA2 = case.RegionClass(vp, k0, r_init, 1, "gompertz")
    gVOLTA,gVOLTAparams = VOLTA2.lmodel()
    VOLTA3 = case.RegionClass(vp, k0, r_init, 1, "richard")
    rVOLTA,rVOLTAparams = VOLTA3.lmodel()
    vError = d.write_error(vp, vVOLTA, "verhulst")
    gError = d.write_error(vp, gVOLTA, "gompertz")
    rError = d.write_error(vp, rVOLTA, "richard")
    vdata = {
        "region": [
            {
                "id": 9,
                "name": "Volta",
                "model": [
                    {"Verhulst": vVOLTA},
                    {"Gompertz": gVOLTA},
                    {"Richard": rVOLTA}
                    ],
                "Parameters": [
                    {"verhulst": vVOLTAparams},
                    {"gompertz": gVOLTAparams},
                    {"richard": rVOLTAparams}
                    ],
                "Errors": [
                    {"verhulst": vError},
                    {"gompertz": gError},
                    {"richard": rError}
                    ]
            }
        ],
        "orgData":
            {
            "year": year.tolist(),
            "population": vp.tolist()
            }    
    }
    db.add_to_db(vdata)
    d.write_data(vp, vVOLTA, gVOLTA, rVOLTA, "Volta")

    #Western Region
    d1 = case.RegionClass(wp, k0, r_init, 1, "verhulst")
    v,vparams = d1.lmodel()
    d2 = case.RegionClass(wp, k0, r_init, 1, "gompertz")
    g,gparams = d2.lmodel()
    d3 = case.RegionClass(wp, k0, r_init, 1, "richard")
    ri,rparams = d3.lmodel()
    vError = d.write_error(wp, v, "verhulst")
    gError = d.write_error(wp, g, "gompertz")
    rError = d.write_error(wp, ri, "richard")
    wdata = {
        "region": [
            {
                "id": 10,
                "name": "western",
                "model": [
                    {"Verhulst": v},
                    {"Gompertz": g},
                    {"Richard": ri}
                    ],
                "Parameters": [
                    {"verhulst": vparams},
                    {"gompertz": gparams},
                    {"richard": rparams}
                    ],
                "Errors": [
                    {"verhulst": vError},
                    {"gompertz": gError},
                    {"richard": rError}
                    ]
            }
        ],
        "orgData":
            {
            "year": year.tolist(),
            "population": wp.tolist()
            }    
    }
    db.add_to_db(wdata)
    d.write_data(wp, v, g, ri, "Western")
    
    my_file = db.read_db()
    print(type(my_file))

    for i in range(10):
        print(f"[{my_file["region"][i].get("name")}] \t {my_file["region"][i].get("Errors")}")

if __name__ == "__main__":
    main()
