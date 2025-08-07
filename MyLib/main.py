#!/usr/bin/env python3
"""
This script runs the population modeling for different regions in Ghana
"""
import numpy as np
from Packages import data as d
from Packages import cases as case
from Packages import db as db
from Packages import models as f


def main():
    wp, cp, gp, vp, ep, ap, bp, northp, uep, uwp = np.array(d.take_data())
    year = np.array((1960, 1970, 1984, 2000, 2010))
    k0 = 6_000_000.0
    r_init = 0.1
    t_f = np.array((6,7))
    

    #-------------------Ashanti Region------------------
  
    # Model fitting And Parameter Estimates
    Ash1 = case.RegionClass(ap, 20_500_000.0, r_init, 1, "verhulst")
    Ash2 = case.RegionClass(ap, 20_500_000.0, r_init, 1, "gompertz")
    Ash3 = case.RegionClass(ap, 20_500_000.0, r_init, 1, "richard")
    vASH,vASHparams = Ash1.lmodel()
    gASH,gASHparams = Ash2.lmodel()
    rASH,rASHparams = Ash3.lmodel()
    
    #--> Forecasts <---
    Asf1 = f.forecast(ap[0],t_f,vASHparams)
    vashf = Asf1.vmodel()
    Asf2 = f.forecast(ap[0],t_f,gASHparams)
    gashf = Asf2.gmodel()
    Asf3 = f.forecast(ap[0],t_f,rASHparams)
    rashf = Asf3.rmodel()

    # --> Errors
    vError = d.write_error(ap, vASH, "verhulst")
    gError = d.write_error(ap, gASH, "gompertz")
    rError = d.write_error(ap, rASH, "richard")

    # -- Writing Errors and parameter Estimations to Database (Json file)
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
        ]
    }
    db.create_db(ashdata)
    ashforecast = {
        "region": [
            
            {
            "id": 0,
            "name": "Ashanti",
            "forecast":
                [
                    {"Verhulst": vashf},
                    {"Gompertz": gashf},
                    {"Richard": rashf}
                ]
            }
        
        ]
    }
    db.create_forecast(ashforecast)
    d.write_data(ap, vASH, gASH, rASH, filename="Ashanti_output.dat")
    

    #---------------------------Brong Ahafo Region------------------

    # Model Fitting and Parameter Estimates

    BA1 = case.RegionClass(bp, 5_500_000.0, r_init, 1, "verhulst")
    BA2 = case.RegionClass(bp, 5_500_000.0, r_init, 1, "gompertz")
    BA3 = case.RegionClass(bp, 5_500_000.0, r_init, 1, "richard")
    vBA,vBAparams = BA1.lmodel()
    gBA,gBAparams = BA2.lmodel()
    rBA,rBAparams = BA3.lmodel()

    # --> Forecasting
    BAf1 = f.forecast(bp[0],t_f,vBAparams)
    vbaf = BAf1.vmodel()
    BAf2 = f.forecast(bp[0],t_f,gBAparams)
    gbaf = BAf2.gmodel()
    BAf3 = f.forecast(bp[0],t_f,rBAparams)
    rbaf = BAf3.rmodel()


    # -----------Errors--------------
    vError = d.write_error(bp, vBA, "verhulst")
    gError = d.write_error(bp, gBA, "gompertz")
    rError = d.write_error(bp, rBA, "richard")

    # Writing Parameters and Errors to Database(JSON File)
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
        ]    
    }
    db.add_to_db(badata)
    baforecast = {
        "region": [
            
            {
            "id": 1,
            "name": "Brong Ahafo",
            "forecast":
                [
                    {"Verhulst": vbaf},
                    {"Gompertz": gbaf},
                    {"Richard": rbaf}
                ]
            }
        
        ]
    }
    db.add_forecast(baforecast)
    d.write_data(bp, vBA, gBA, rBA , filename="BrongAhafo_output.dat")


    #-----------------------Central Region---------------------

    # Model Fitting and Parameter Estimates
    CENT1 = case.RegionClass(cp, 20_500_000.0, r_init, 1, "verhulst")
    CENT2 = case.RegionClass(cp, 20_500_000.0, r_init, 1, "gompertz")
    CENT3 = case.RegionClass(cp, 20_500_000.0, r_init, 1, "richard")
    vCENT,vCENTparams = CENT1.lmodel()
    gCENT,gCENTparams = CENT2.lmodel()
    rCENT,rCENTparams = CENT3.lmodel()
    
    # --> Forecasting
    Centf1 = f.forecast(cp[0],t_f,vCENTparams)
    vcentf = Centf1.vmodel()
    Centf2 = f.forecast(cp[0],t_f,gCENTparams)
    gcentf = Centf2.gmodel()
    Centf3 = f.forecast(cp[0],t_f,rCENTparams)
    rcentf = Centf3.rmodel()    

    # ----Errors------
    vError = d.write_error(cp, vCENT, "verhulst")
    gError = d.write_error(cp, gCENT, "gompertz")
    rError = d.write_error(cp, rCENT, "richard")
    
    # Writing Parameters and Errors to Database (JSON file)
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
        ] 
    }
    db.add_to_db(cdata)
    centforecast = {
        "region": [
            
            {
            "id": 3,
            "name": "Central",
            "forecast":
                [
                    {"Verhulst": vcentf},
                    {"Gompertz": gcentf},
                    {"Richard": rcentf}
                ]
            }
        
        ]
    }
    db.add_forecast(centforecast)
    d.write_data(cp, vCENT, gCENT, rCENT, filename="Central_output.dat")


    #------------------------------Eastern Region------------------------

    # Model Fitting and Parameter Estimates

    EST1 = case.RegionClass(ep, 20_000_000.0, r_init, 1, "verhulst")
    EST2 = case.RegionClass(ep, 20_000_000.0, r_init, 1, "gompertz")
    EST3 = case.RegionClass(ep, 20_000_000.0, r_init, 1, "richard")
    vEST,vESTparams = EST1.lmodel()
    gEST,gESTparams = EST2.lmodel()
    rEST,rESTparams = EST3.lmodel()

    # --> Forecasting
    Eastf1 = f.forecast(ep[0],t_f,vESTparams)
    veastf = Eastf1.vmodel()
    Eastf2 = f.forecast(ep[0],t_f,gESTparams)
    geastf = Eastf2.gmodel()
    Eastf3 = f.forecast(ep[0],t_f,rESTparams)
    reastf = Eastf3.rmodel()    

    #--------Errors--------------

    vError = d.write_error(ep, vEST, "verhulst")
    gError = d.write_error(ep, gEST, "gompertz")
    rError = d.write_error(ep, rEST, "richard")

    # Writing Parameters and Errors to Database (JSON file)
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
        ] 
    }
    db.add_to_db(edata)
    eastforecast = {
        "region": [
            
            {
            "id": 4,
            "name": "Eastern",
            "forecast":
                [
                    {"Verhulst": veastf},
                    {"Gompertz": geastf},
                    {"Richard": reastf}
                ]
            }
        
        ]
    }
    db.add_forecast(eastforecast)
    d.write_data(ep, vEST, gEST, rEST, filename="Eastern_output.dat")

    #--------------------------Greater Accra Region-------------------------

    # Model Fitting and Parameter Estimates
    GA1 = case.RegionClass(gp, 7_000_000.0, r_init, 1, "verhulst")
    GA2 = case.RegionClass(gp, 7_000_000.0, r_init, 1, "gompertz")
    GA3 = case.RegionClass(gp, 7_000_000.0, r_init, 1, "richard")
    vGA,vGAparams = GA1.lmodel()
    gGA,gGAparams = GA2.lmodel()
    rGA,rGAparams = GA3.lmodel()

    # --> Forecasting
    GAf1 = f.forecast(gp[0],t_f,vGAparams)
    vgaf = GAf1.vmodel()
    GAf2 = f.forecast(gp[0],t_f,gGAparams)
    ggaf = GAf2.gmodel()
    GAf3 = f.forecast(gp[0],t_f,rGAparams)
    rgaf = GAf3.rmodel()   

    #------Errors-------------------
    vError = d.write_error(gp, vGA, "verhulst")
    gError = d.write_error(gp, gGA, "gompertz")
    rError = d.write_error(gp, rGA, "richard")

    # Writing Parameters and Errors to database (JSON file)
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
        ]
    }
    db.add_to_db(adata)
    gaforecast = {
        "region": [
            
            {
            "id": 5,
            "name": "Greater Accra",
            "forecast":
                [
                    {"Verhulst": vgaf},
                    {"Gompertz": ggaf},
                    {"Richard": rgaf}
                ]
            }
        
        ]
    }
    db.add_forecast(gaforecast)
    d.write_data(gp, vGA, gGA, rGA, filename="GreaterAccra_output.dat")


    #-----------------------------Northen Region-------------------------------

    # Model Fitting And Parameter Estimates

    NORTH1 = case.RegionClass(northp, k0, r_init, 1, "verhulst")
    NORTH2 = case.RegionClass(northp, k0, r_init, 1, "gompertz")
    NORTH3 = case.RegionClass(northp, k0, r_init, 1, "richard")
    vNORTH,vNORTHparams = NORTH1.lmodel()
    gNORTH,gNORTHparams = NORTH2.lmodel()
    rNORTH,rNORTHparams = NORTH3.lmodel()

    # --> Forecasting
    Nf1 = f.forecast(northp[0],t_f,vNORTHparams)
    vnf = Nf1.vmodel()
    Nf2 = f.forecast(northp[0],t_f,gNORTHparams)
    gnf = Nf2.gmodel()
    Nf3 = f.forecast(northp[0],t_f,rNORTHparams)
    rnf = Nf3.rmodel()


    #-----Errors------
    vError = d.write_error(northp, vNORTH, "verhulst")
    gError = d.write_error(northp, gNORTH, "gompertz")
    rError = d.write_error(northp, rNORTH, "richard")

    # Writing Parameters and Errors to Database (JSON file)
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
        ]
    }
    db.add_to_db(ndata)
    northforecast = {
        "region": [
            
            {
            "id": 6,
            "name": "Northern",
            "forecast":
                [
                    {"Verhulst": vnf},
                    {"Gompertz": gnf},
                    {"Richard": rnf}
                ]
            }
        
        ]
    }
    db.add_forecast(northforecast)
    d.write_data(northp, vNORTH, gNORTH, rNORTH, filename="Northern_output.dat")
    
    #---------------------------Upper East Region------------------------------
    
    # Model Fitting and Paramter Estimates
    UET1 = case.RegionClass(uep, 3_000_000.0, r_init, 1, "verhulst")
    UET2 = case.RegionClass(uep, 3_000_000.0, r_init, 1, "gompertz")
    UET3 = case.RegionClass(uep, 3_000_000.0, r_init, 1, "richard")
    vUET,vUETparams = UET1.lmodel()
    gUET,gUETparams = UET2.lmodel()
    rUET,rUETparams = UET3.lmodel()

    # --> Forecasting
    UEf1 = f.forecast(uep[0],t_f,vUETparams)
    vuef = UEf1.vmodel()
    UEf2 = f.forecast(uep[0],t_f,gUETparams)
    guef = UEf2.gmodel()
    UEf3 = f.forecast(uep[0],t_f,rUETparams)
    ruef = UEf3.rmodel()

    #-------Errors----------------
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
        ]
    }
    db.add_to_db(udata)
    ueforecast = {
        "region": [
            
            {
            "id": 7,
            "name": "Upper East",
            "forecast":
                [
                    {"Verhulst": vuef},
                    {"Gompertz": guef},
                    {"Richard": ruef}
                ]
            }
        
        ]
    }
    db.add_forecast(ueforecast)
    d.write_data(uep,  vUET, gUET, rUET, filename="UpperEast_output.dat")

    #--------------------Upper West Region-----------------------------
    UWT1 = case.RegionClass(uwp, 20_500_000.0, r_init, 1, "verhulst")
    UWT2 = case.RegionClass(uwp, 20_500_000.0, r_init, 1, "gompertz")
    UWT3 = case.RegionClass(uwp, 20_500_000.0, r_init, 1, "richard")
    vUWT,vUWTparams = UWT1.lmodel()
    gUWT,gUWTparams = UWT2.lmodel()
    rUWT,rUWTparams = UWT3.lmodel()

    # --> Forecasting
    UWf1 = f.forecast(uwp[0],t_f,vUWTparams)
    vuwf = UWf1.vmodel()
    UWf2 = f.forecast(uwp[0],t_f,gUWTparams)
    guwf = UWf2.gmodel()
    UWf3 = f.forecast(uwp[0],t_f,rUWTparams)
    ruwf = UWf3.rmodel()

    #------Errors-------
    vError = d.write_error(uwp, vUWT, "verhulst")
    gError = d.write_error(uwp, gUWT, "gompertz")
    rError = d.write_error(uwp, rUWT, "richard")

    # Writing Parameters and Errors to Database (JSON File)
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
        ]
    }
    db.add_to_db(uwdata)
    uwforecast = {
        "region": [
            
            {
            "id": 8,
            "name": "Upper West",
            "forecast":
                [
                    {"Verhulst": vuwf},
                    {"Gompertz": guwf},
                    {"Richard": ruwf}
                ]
            }
        
        ]
    }
    db.add_forecast(uwforecast)
    d.write_data(uwp, vUWT, gUWT, rUWT, filename="UpperWest_output.dat")

    #Volta Region
    VOLTA1 = case.RegionClass(vp, 20_000_000.0, r_init, 1, "verhulst")
    VOLTA2 = case.RegionClass(vp, 20_000_000.0, r_init, 1, "gompertz")
    VOLTA3 = case.RegionClass(vp, 20_000_000.0, r_init, 1, "richard")
    vVOLTA,vVOLTAparams = VOLTA1.lmodel()
    gVOLTA,gVOLTAparams = VOLTA2.lmodel()
    rVOLTA,rVOLTAparams = VOLTA3.lmodel()

    # --> Forecasting
    Vf1 = f.forecast(vp[0],t_f,vVOLTAparams)
    vvf = Vf1.vmodel()
    Vf2 = f.forecast(vp[0],t_f,gVOLTAparams)
    gvf = Vf2.gmodel()
    Vf3 = f.forecast(vp[0],t_f,rVOLTAparams)
    rvf = Vf3.rmodel()

    # -------Errors-----
    vError = d.write_error(vp, vVOLTA, "verhulst")
    gError = d.write_error(vp, gVOLTA, "gompertz")
    rError = d.write_error(vp, rVOLTA, "richard")
    
    # Writing Parameters and Errors to Database (JSON File)
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
        ] 
    }
    db.add_to_db(vdata)
    voltaforecast = {
        "region": [
            
            {
            "id": 9,
            "name": "Volta",
            "forecast":
                [
                    {"Verhulst": vvf},
                    {"Gompertz": gvf},
                    {"Richard": rvf}
                ]
            }
        
        ]
    }
    db.add_forecast(voltaforecast)
    d.write_data(vp, vVOLTA, gVOLTA, rVOLTA, filename="Volta_output.dat")

    #Western Region
    d1 = case.RegionClass(wp, 5_000_000.0, r_init, 1, "verhulst")
    d2 = case.RegionClass(wp, 5_000_000.0, r_init, 1, "gompertz")
    d3 = case.RegionClass(wp, 5_000_000.0, r_init, 1, "richard")
    v,vparams = d1.lmodel()
    g,gparams = d2.lmodel()
    ri,rparams = d3.lmodel()

    # --> Forecasting
    Wf1 = f.forecast(wp[0],t_f,vparams)
    vwf = Wf1.vmodel()
    Wf2 = f.forecast(wp[0],t_f,gparams)
    gwf = Wf2.gmodel()
    Wf3 = f.forecast(wp[0],t_f,rparams)
    rwf = Wf3.rmodel()


    #------Errors-------
    vError = d.write_error(wp, v, "verhulst")
    gError = d.write_error(wp, g, "gompertz")
    rError = d.write_error(wp, ri, "richard")

    # Writing Parameters and Errors to Database (JSON File)
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
        ]
    }
    db.add_to_db(wdata)
    westforecast = {
        "region": [
            
            {
            "id": 10,
            "name": "Western",
            "forecast":
                [
                    {"Verhulst": vwf},
                    {"Gompertz": gwf},
                    {"Richard": rwf}
                ]
            }
        
        ]
    }
    db.add_forecast(westforecast)
    d.write_data(wp, v, g, ri, filename="Western_output.dat")
    
    my_file = db.read_db()
    #l = [0,4]
    #for id in l:
    #    print(f"[{my_file["region"][id].get("name")}] \t {my_file["region"][id].get("Errors")}")

if __name__ == "__main__":
    main()
