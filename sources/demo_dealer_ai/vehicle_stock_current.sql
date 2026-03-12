SELECT 
    f.Vehicle_Key,
    f.Vehicle_ID,
    f.Stock_No,
    f.Stocked_Date,
    f.Stock_Value,
    f.Days_In_Stock,
    f.Days_In_Stock_Category_ID,
    f.Vehicle_Class_ID,
    f.Vehicle_Type_ID,
    f.Vehicle_Stockcard_Status_Code,
    c.Company_Key,
    c.Company_Shortname,
    l.Location_ID,
    l.Location_Shortname,
    vc.Vehicle_Class_Description,
    dic.Days_In_Stock_Category_Description,
    m.Make_Name
FROM FactVehicleStockCurrent f
LEFT JOIN DimLocation l ON f.Location_ID = l.Location_ID
LEFT JOIN DimCompany c ON l.Company_Key = c.Company_Key
LEFT JOIN DimVehicleClass vc ON f.Vehicle_Class_ID = vc.Vehicle_Class_ID
LEFT JOIN DimDaysInStockCategory dic ON f.Days_In_Stock_Category_ID = dic.Days_In_Stock_Category_ID
LEFT JOIN DimVehicle v ON f.Vehicle_Key = v.Vehicle_Key
LEFT JOIN DimModel mo ON v.Model_Key = mo.Model_Key
LEFT JOIN DimModelType mt ON mo.Model_Type_Key = mt.Model_Type_Key
LEFT JOIN DimMake m ON mt.Make_Key = m.Make_Key;
