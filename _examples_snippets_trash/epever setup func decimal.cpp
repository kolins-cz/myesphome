std::vector<uint16_t> battery_settings1 = {
    0,     // 9000 Battery Type 0 = User
    200,   // 9001 Battery Cap 115AH
    0,   // 9002 Temp compensation -3V /°C/2V
    6500,  // 9003 Over Voltage Disconnect Voltage 15.0
    6230,  // 9004 Charging Limit Voltage 14.8
    6220,  // 9005 Over Voltage Reconnect Voltage 14.8
    6210,  // 9006 Equalize Charging Voltage 14.6
    6032,  // 9007 Boost Charging Voltage 14.7
    6030,  // 9008 Float Charging Voltage 13.6
    5900,  // 9009 Boost Reconnect Charging Voltage 13.2
    5800,  // 900A Low Voltage Reconnect Voltage 12.2
    5400,  // 900B Under Voltage Warning Reconnect Voltage 12.0
    5300,  // 900c Under Volt. Warning Volt 12.1
    5200,  // 900d Low Volt. Disconnect Volt. 11.8
    5200   // 900E Discharging Limit Voltage 11.8
};