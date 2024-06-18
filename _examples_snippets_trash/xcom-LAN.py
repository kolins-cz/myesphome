from xcom_proto import XcomP as param
from xcom_proto import XcomC
from xcom_proto import XcomLANTCP


# OR (default ports are 4002 and 4001)
xcom = XcomLANTCP("192.168.10.23")

with XcomLANTCP(port=10000) as xcom:

    boostValue = xcom.getValue(param.SMART_BOOST_LIMIT)


    boostValue = xcom.getValue(param.SMART_BOOST_LIMIT)

    pvmode = xcom.getValue(param.PV_OPERATION_MODE)
    pvpower = xcom.getValue(param.PV_POWER) * 1000 # convert from kW to W
    sunhours = xcom.getValue(param.PV_SUN_HOURS_CURR_DAY)
    energyProd = xcom.getValue(param.PV_ENERGY_CURR_DAY)

    soc = xcom.getValue(param.BATT_SOC)
    battPhase = xcom.getValue(param.BATT_CYCLE_PHASE)
    battCurr = xcom.getValue(param.BATT_CURRENT)
    battVolt = xcom.getValue(param.BATT_VOLTAGE)

    # please look into the official Studer parameter documentation to find out
    # what type a parameter has
    pvmode_manual = xcom.getValueByID(11016, XcomC.TYPE_SHORT_ENUM)

    # using custom dstAddr (can also be used for getValueByID())
    solarPowerVS1 = xcom.getValue(param.VS_PV_POWER, dstAddr=701)
    solarPowerVS2 = xcom.getValue(param.VS_PV_POWER, dstAddr=702)

    print(boostValue, pvmode, pvpower, sunhours, energyProd, soc, battPhase, battCurr, battVolt)