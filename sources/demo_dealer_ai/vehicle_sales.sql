SELECT 
    f.Invoice_Date,
    EXTRACT(YEAR FROM f.Invoice_Date) AS Sales_Year,
    DATE_TRUNC('month', f.Invoice_Date) AS Invoice_Month,
    c.Company_Key,
    c.Company_Shortname,
    vc.Vehicle_Class_ID,
    vc.Vehicle_Class_Description,
    m.Make_Name,
    f.Vehicle_Key,
    f.Vehicle_Gross,
    l.Location_ID,
    l.Location_Shortname
FROM FactVehicleSales f
LEFT JOIN DimLocation l ON f.Location_ID = l.Location_ID
LEFT JOIN DimCompany c ON l.Company_Key = c.Company_Key
LEFT JOIN DimVehicleClass vc ON f.Vehicle_Class_ID = vc.Vehicle_Class_ID
LEFT JOIN DimVehicle v ON f.Vehicle_Key = v.Vehicle_Key
LEFT JOIN DimModel mo ON v.Model_Key = mo.Model_Key
LEFT JOIN DimModelType mt ON mo.Model_Type_Key = mt.Model_Type_Key
LEFT JOIN DimMake m ON mt.Make_Key = m.Make_Key;
