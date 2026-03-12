# DemoDealerAI Data Dictionary

## Overview

The `DemoDealerAI` schema is designed to track vehicle inventory, movements, and sales. It follows a **Snowflake Schema** architecture consisting of Dimension (DIM) and Fact (FACT) tables.

### Architecture Highlights

- **DimDate** is a standard date dimension for time-series analysis.
- Some dimensions have hierarchies (e.g., `DimCompany` -> `DimLocation` and `DimMake` -> `DimModelType` -> `DimModel` -> `DimVehicle`).
- Other dimensions (`DimVehicleClass`, `DimVehicleType`, `DimVehicleSalesGroup`, `DimVehicleStockcardStatus`, `DimDaysInStockCategory`, `DimVehicleAcquisition`) are standalone reference tables containing primarily an ID and a Description.

---

## Dimension Tables

### DimCompany

**Purpose:** Stores company entities. This is the parent of `DimLocation`.
| Column Name | Data Type | Key | Description |
| :--- | :--- | :--- | :--- |
| `Company_Key` | INT | [PK] | Primary identifier for the company. |
| `Company_Fullname` | NVARCHAR(256) | | The full name of the company. |
| `Company_Shortname` | NVARCHAR(256) | | An abbreviated name for the company. |

### DimLocation

**Purpose:** Stores physical or logical locations belonging to a company.
| Column Name | Data Type | Key | Description |
| :--- | :--- | :--- | :--- |
| `Location_ID` | INT | [PK] | Primary identifier for the location. |
| `Location_Fullname` | NVARCHAR(256) | | The full name of the location. |
| `Location_Shortname` | NVARCHAR(256) | | An abbreviated name. |
| `Location_Fullinfo` | NVARCHAR(500) | | Extended information about the location. |
| `Is_Active` | BIT | | Indicates if the location is currently active. |
| `Company_Key` | INT | [FK] | References `DimCompany`. |

### DimMake

**Purpose:** Stores vehicle manufacturers/makes (e.g., Toyota, Ford). Parent of `DimModelType`.
| Column Name | Data Type | Key | Description |
| :--- | :--- | :--- | :--- |
| `Make_Key` | INT | [PK] | Primary identifier for the make. |
| `Make_Name` | NVARCHAR(80) | | The name of the manufacturer. |
| `Make_Description` | NVARCHAR(512) | | Detailed description of the make. |
| `Is_Active` | BIT | | Indicates if the make is currently active. |

### DimModelType

**Purpose:** Categorizes vehicle models under a specific Make. Parent of `DimModel`.
| Column Name | Data Type | Key | Description |
| :--- | :--- | :--- | :--- |
| `Model_Type_Key` | INT | [PK] | Primary identifier for the model type. |
| `Model_Type_Name` | NVARCHAR(128) | | The name of the model type. |
| `Model_Type_Description`| NVARCHAR(512)| | Detailed description of the model type. |
| `Is_Active` | BIT | | Indicates if the model type is currently active. |
| `Make_Key` | INT | [FK] | References `DimMake`. |

### DimModel

**Purpose:** Stores specific vehicle models. Parent of `DimVehicle`.
| Column Name | Data Type | Key | Description |
| :--- | :--- | :--- | :--- |
| `Model_Key` | INT | [PK] | Primary identifier for the model. |
| `Model_Name` | NVARCHAR(80) | | The name of the model. |
| `Model_Description` | NVARCHAR(1200)| | Detailed description of the model. |
| `Model_Series` | NVARCHAR(80) | | The series classification of the model. |
| `Model_Badge` | NVARCHAR(100) | | The badge/trim level of the model. |
| `Is_Active` | BIT | | Indicates if the model is active. |
| `Model_Type_Key` | INT | [FK] | References `DimModelType`. |

### DimVehicle

**Purpose:** Stores individual unique vehicles (the lowest level of the vehicle hierarchy).
| Column Name | Data Type | Key | Description |
| :--- | :--- | :--- | :--- |
| `Vehicle_Key` | INT | [PK] | Primary identifier for the assigned vehicle. |
| `VIN` | NVARCHAR(34) | | Vehicle Identification Number (partially masked for privacy). |
| `REGO_NO` | NVARCHAR(80) | | Vehicle Registration Number (partially masked). |
| `Manufacturer_ID` | NVARCHAR(80) | | Identifier from the manufacturer. |
| `Colour` | NVARCHAR(256) | | Color of the vehicle. |
| `Vehicle_Description` | NVARCHAR(2000)| | Unique description of this specific vehicle. |
| `Is_Active` | BIT | | Indicates if the vehicle record is active. |
| `Model_Key` | INT | [FK] | References `DimModel`. |

### Standalone Dimensions

These tables are lookup references containing simple ID and Description pairs.

- **`DimDate`**: Time dimension holding full dates, years, quarters, months, and fiscal periods. `Timeline_Type` flags dates as 'Past', 'Present', or 'Future'.
- **`DimVehicleClass`**: ID and Description for the class of a vehicle.
- **`DimVehicleType`**: ID and Description for the overall vehicle type.
- **`DimVehicleSalesGroup`**: Categorizes vehicles into specific sales groups.
- **`DimVehicleStockcardStatus`**: Represents the current status of a vehicle card in the inventory.
- **`DimDaysInStockCategory`**: Buckets vehicles into aging categories (e.g., '<30', '30-59', '180+').
- **`DimVehicleAcquisition`**: Defines how the vehicle was acquired by the dealership.

---

## Fact Tables

### FactVehicleStockCurrent

**Purpose:** Tracks a snapshot of the **current** vehicle inventory stock.
| Column Name | Data Type | Key | Description |
| :--- | :--- | :--- | :--- |
| `Days_In_Stock_Category_ID` | INT | [FK] | Links to `DimDaysInStockCategory`. |
| `Location_ID` | INT | [FK] | Links to `DimLocation`. |
| `Vehicle_Key` | INT | [FK] | Links to `DimVehicle`. |
| `Vehicle_Class_ID` | INT | [FK] | Links to `DimVehicleClass`. |
| `Vehicle_Type_ID` | INT | [FK] | Links to `DimVehicleType`. |
| `Vehicle_Stockcard_Status_Code`| INT| [FK] | Links to `DimVehicleStockcardStatus`. |
| `Vehicle_ID` | NVARCHAR(80)| | Secondary vehicle identifier. |
| `Stock_No` | INT | | Unique stock number assigned by the dealer. |
| `Stocked_Date` | DATE | | Original date the vehicle entered stock. |
| `Vehicle_Stockcard_Key`| INT | | Unique key identifying the stock card. |
| `Stock_Value` | DECIMAL(19,4)| **Measure** | The value of the vehicle currently in stock. |
| `Days_In_Stock` | INT | **Measure** | Calculated number of days the vehicle has been in stock (Current Date - Stocked Date). |

### FactVehicleStockMovement

**Purpose:** Tracks historical **movements** and changes in stock over time.
| Column Name | Data Type | Key | Description |
| :--- | :--- | :--- | :--- |
| `Date_In_Stock` | DATE | [FK] | The date of the stock movement. Links to `DimDate`. |
| `Days_In_Stock_Category_ID` | INT | [FK] | Links to `DimDaysInStockCategory`. Calculated as of `Date_In_Stock`. |
| `Location_ID` | INT | [FK] | Links to `DimLocation`. |
| `Vehicle_Key` | INT | [FK] | Links to `DimVehicle`. |
| `Vehicle_Class_ID` | INT | [FK] | Links to `DimVehicleClass`. |
| `Vehicle_Type_ID` | INT | [FK] | Links to `DimVehicleType`. |
| `Vehicle_Stockcard_Status_Code`| INT| [FK] | Links to `DimVehicleStockcardStatus`. |
| `Vehicle_ID` | NVARCHAR(80)| | Secondary vehicle identifier. |
| `Stock_No` | INT | | Unique stock number assigned by the dealer. |
| `Stocked_Date` | DATE | | Original date the vehicle entered stock. |
| `Vehicle_Stockcard_Key`| INT | | Unique key identifying the stock card. |
| `Stock_Value` | DECIMAL(19,4)| **Measure** | The value of the vehicle at the time of the movement. |
| `Days_In_Stock` | INT | **Measure** | Number of days in stock calculated as of the `Date_In_Stock`. |

### FactVehicleSales

**Purpose:** Tracks individual sales transactions, financials, and profits.
| Column Name | Data Type | Key | Description |
| :--- | :--- | :--- | :--- |
| `Invoice_Date` | DATE | [FK] | The date the sale was invovoiced. Links to `DimDate`. |
| `Location_ID` | INT | [FK] | Links to `DimLocation`. |
| `Vehicle_Key` | INT | [FK] | Links to `DimVehicle`. |
| `Vehicle_Class_ID` | INT | [FK] | Links to `DimVehicleClass`. |
| `Vehicle_Type_ID` | INT | [FK] | Links to `DimVehicleType`. |
| `Vehicle_Sales_Group_ID` | INT | [FK] | Links to `DimVehicleSalesGroup`. |
| `Vehicle_Acquisition_Type`| INT | [FK] | Links to `DimVehicleAcquisition`. |
| `Vehicle_ID` | NVARCHAR(80)| | Secondary vehicle identifier. |
| `Stock_No` | INT | | Unique stock number assigned by the dealer. |
| `Deal_No` | INT | | Identifier for the sales deal. |
| `Invoice_No` | INT | | Identifier for the final invoice. |
| `Vehicle_Deal_Key`| INT | | Primary key for the deal record. |
| `Vehicle_Stockcard_Key`| INT | | Identifying key for the vehicle's stock card. |
| `Purchased_From_Name`| NVARCHAR(256)| | Name of the entity the vehicle was purchased from (if applicable). |
| `Deal_Profit` | DECIMAL(19,4)| **Measure** | Raw profit from the sale of the vehicle (Selling Price - Cost Price). |
| `Holdback_Amount` | DECIMAL(19,4)| **Measure** | Manufacturer incentives/holdbacks received per vehicle. |
| `Trade_In_Income` | DECIMAL(19,4)| **Measure** | Profit generated from accompanying trade-ins. |
| `Aftermarket_Profit` | DECIMAL(19,4)| **Measure** | Profit from aftermarket add-ons (warranties, accessories, etc.). |
| `Vehicle_Gross` | DECIMAL(19,4)| **Measure** | Subtotal: `Deal_Profit` + `Holdback_Amount` + `Trade_In_Income`. |
| `Total_Gross` | DECIMAL(19,4)| **Measure** | Total Profit: `Vehicle_Gross` + `Aftermarket_Profit`. |
