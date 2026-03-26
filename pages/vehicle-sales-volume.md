<div class="mb-8 flex justify-between items-start">
    <div>
        <h1 class="text-4xl font-black text-slate-800 tracking-tight mb-2">Vehicle Sales Volume</h1>
        <p class="text-slate-500 text-lg">This report provides a comprehensive overview of vehicle sales across your network. Use the filters below to refine your data by Year, Company, and Class.</p>
    </div>
    <a href="/data-storytelling" title="Back to Data Storytelling" class="group flex items-center justify-center p-3 bg-white hover:bg-gradient-to-br hover:from-blue-500 hover:to-indigo-600 text-slate-400 hover:text-white rounded-2xl shadow-sm hover:shadow-xl border border-slate-200 hover:border-transparent transition-all duration-300 transform hover:-translate-y-1 hover:rotate-3 backdrop-blur-sm z-50">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 transition-transform group-hover:-translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
    </a>
</div>

<!-- DATA SOURCES -->

```sql sales_years
SELECT DISTINCT CAST(CAST(Sales_Year AS INT) AS VARCHAR) as Sales_Year_Label, Sales_Year
FROM demo_dealer_ai.vehicle_sales
ORDER BY Sales_Year DESC
```

```sql companies
SELECT DISTINCT Company_Shortname
FROM demo_dealer_ai.vehicle_sales
WHERE Company_Shortname IS NOT NULL
ORDER BY Company_Shortname
```

```sql vehicle_classes
SELECT DISTINCT Vehicle_Class_Description
FROM demo_dealer_ai.vehicle_sales
WHERE Vehicle_Class_Description IS NOT NULL
ORDER BY Vehicle_Class_Description
```

```sql locations
SELECT DISTINCT Location_Shortname
FROM demo_dealer_ai.vehicle_sales
WHERE Location_Shortname IS NOT NULL
  AND Company_Shortname IN ${inputs.selected_company.value}
ORDER BY Location_Shortname
```

<!-- FILTERS SECTION -->
<div class="bg-slate-50 border border-slate-200 p-6 rounded-xl shadow-sm mb-10">
    <div class="flex items-center gap-2 mb-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-500" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M3 3a1 1 0 011-1h12a1 1 0 011 1v3a1 1 0 01-.293.707L12 11.414V15a1 1 0 01-.293.707l-2 2A1 1 0 018 17v-5.586L3.293 6.707A1 1 0 013 6V3z" clip-rule="evenodd" />
        </svg>
        <span class="text-sm font-bold text-slate-700 uppercase tracking-wide">Data Filters</span>
    </div>
    <div class="flex flex-col -space-y-4">
        <Dropdown data={sales_years} name="selected_year" value=Sales_Year_Label title="Sales Year" defaultValue="2025" />
        <Dropdown data={companies} name="selected_company" value=Company_Shortname title="Company" multiple=true selectAllByDefault=true />
        <Dropdown data={locations} name="selected_location" value=Location_Shortname title="Location" multiple=true selectAllByDefault=true />
        <Dropdown data={vehicle_classes} name="selected_class" value=Vehicle_Class_Description title="Vehicle Class" multiple=true selectAllByDefault=true />
    </div>
</div>

```sql filtered_sales
SELECT *
FROM demo_dealer_ai.vehicle_sales
WHERE TRUE
  -- Sales Year filter
  AND ('${inputs.selected_year.value}' = 'All' OR Sales_Year = TRY_CAST('${inputs.selected_year.value}' AS INTEGER) OR (Sales_Year IS NULL AND '${inputs.selected_year.value}' = 'null'))

  -- Company filter
  AND Company_Shortname IN ${inputs.selected_company.value}

  -- Location filter
  AND Location_Shortname IN ${inputs.selected_location.value}

  -- Vehicle Class filter
  AND Vehicle_Class_Description IN ${inputs.selected_class.value}
```

```sql metrics_with_comparison
WITH base_data AS (
    SELECT Sales_Year, Vehicle_Key
    FROM demo_dealer_ai.vehicle_sales
    WHERE TRUE
      AND Company_Shortname IN ${inputs.selected_company.value}
      AND Location_Shortname IN ${inputs.selected_location.value}
      AND Vehicle_Class_Description IN ${inputs.selected_class.value}
),
agg_data AS (
    SELECT
        (SELECT COUNT(Vehicle_Key) FROM base_data WHERE '${inputs.selected_year.value}' = 'All' OR Sales_Year = TRY_CAST('${inputs.selected_year.value}' AS INTEGER)) as vehicles_sold,
        (SELECT COUNT(Vehicle_Key) FROM base_data WHERE '${inputs.selected_year.value}' != 'All' AND Sales_Year = TRY_CAST('${inputs.selected_year.value}' AS INTEGER) - 1) as previous_sold
)
SELECT
    vehicles_sold,
    previous_sold,
    (vehicles_sold - previous_sold) as difference_num,
    ((vehicles_sold - previous_sold) * 1.0 / NULLIF(previous_sold, 0)) as difference_pct
FROM agg_data
```

```sql vehicle_sales_by_class
WITH class_counts AS (
  SELECT
    Vehicle_Class_Description,
    COUNT(Vehicle_Key) as vehicles_sold
  FROM ${filtered_sales}
  WHERE Vehicle_Class_Description IS NOT NULL
  GROUP BY Vehicle_Class_Description
),
total_counts AS (
  SELECT SUM(vehicles_sold) as total_sold FROM class_counts
)
SELECT
  Vehicle_Class_Description,
  Vehicle_Class_Description || ' (' || vehicles_sold || ', ' || ROUND(vehicles_sold * 100.0 / total_sold, 1) || '%)' as Vehicle_Class_Label,
  vehicles_sold
FROM class_counts, total_counts
ORDER BY vehicles_sold DESC
```

<div class="flex justify-center w-full mt-8 mb-16">
    <div class="bg-white rounded-2xl shadow-[0_8px_30px_rgb(0,0,0,0.12)] border border-slate-200 px-10 py-8 flex flex-col items-center min-w-[350px] transform hover:scale-105 transition-all duration-300">
        <h3 class="text-slate-500 font-bold text-sm tracking-widest uppercase mb-3">Total Vehicles Sold</h3>
        <div class="text-6xl font-black text-slate-800 mb-4 tracking-tight drop-shadow-sm">
            <Value data={metrics_with_comparison} column=vehicles_sold fmt="num0" />
        </div>
        {#if metrics_with_comparison.length > 0 && metrics_with_comparison[0].previous_sold !== null}
            <div class="flex items-center space-x-3 text-sm font-semibold {metrics_with_comparison[0].difference_num >= 0 ? 'text-emerald-700 bg-emerald-50 border-emerald-200' : 'text-rose-700 bg-rose-50 border-rose-200'} px-4 py-1.5 rounded-full border shadow-sm">
                <span>Prev: <Value data={metrics_with_comparison} column=previous_sold fmt="num0" /></span>
                <span class="opacity-40">|</span>
                <span class="flex items-center">
                    {#if metrics_with_comparison[0].difference_num >= 0}
                        ▲ +<Value data={metrics_with_comparison} column=difference_num fmt="num0" /> (+<Value data={metrics_with_comparison} column=difference_pct fmt="pct1" />)
                    {:else}
                        ▼ <Value data={metrics_with_comparison} column=difference_num fmt="num0" /> (<Value data={metrics_with_comparison} column=difference_pct fmt="pct1" />)
                    {/if}
                </span>
            </div>
        {/if}
    </div>
</div>

    <ECharts config={{
    title: {
        text: 'Sales by Vehicle Class',
        left: 'center'
    },
    tooltip: {
        trigger: 'item',
        formatter: '{b}: {c} ({d}%)'
    },
    legend: {
        show: false
    },
    series: [
        {
            name: 'Vehicle Class',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: true,
            itemStyle: {
                borderRadius: 5,
                borderColor: '#fff',
                borderWidth: 2
            },
            label: {
                show: true,
                formatter: '{b}'
            },
            data: vehicle_sales_by_class.map(d => ({ value: d.vehicles_sold, name: d.Vehicle_Class_Description }))
        }
    ]
}} />

---

<div class="bg-white border border-slate-200 p-6 rounded-xl shadow-sm mb-10 transform hover:-translate-y-1 transition-transform duration-300">
    <div class="flex items-center gap-3 mb-6 border-b border-slate-100 pb-4">
        <div class="p-2 bg-blue-50 text-blue-600 rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" />
            </svg>
        </div>
        <h2 class="text-2xl font-bold text-slate-800 tracking-tight">Monthly Sales Trend</h2>
    </div>

```sql monthly_sales
SELECT
  Invoice_Month,
  COUNT(Vehicle_Key) as vehicles_sold
FROM ${filtered_sales}
GROUP BY Invoice_Month
ORDER BY Invoice_Month
```

    <LineChart
        data={monthly_sales}
        x=Invoice_Month
        y=vehicles_sold
        title="Vehicles Sold per Month"
        labels=true
        yScale=true
        colorPalette={['#3b82f6', '#8b5cf6', '#ec4899']}
        lineType="curveCardinal"
        renderer="canvas"
    />

</div>

<div class="bg-white border border-slate-200 p-6 rounded-xl shadow-sm mb-10 transform hover:-translate-y-1 transition-transform duration-300">
    <div class="flex items-center gap-3 mb-6 border-b border-slate-100 pb-4">
        <div class="p-2 bg-indigo-50 text-indigo-600 rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2z" />
            </svg>
        </div>
        <h2 class="text-2xl font-bold text-slate-800 tracking-tight">Sales by Make</h2>
    </div>

```sql make_sales
SELECT
  Make_Name,
  CAST(Sales_Year AS VARCHAR) as Sales_Year_String,
  COUNT(Vehicle_Key) as vehicles_sold
FROM ${filtered_sales}
WHERE Make_Name IS NOT NULL
GROUP BY Make_Name, Sales_Year
ORDER BY Make_Name, Sales_Year
```

    <BarChart
        data={make_sales}
        x=Make_Name
        y=vehicles_sold
        series=Sales_Year_String
        title="Vehicle Sales by Make and Year"
        type=grouped
        labels=true
        swapXY=true
    />

</div>

<div class="bg-white border border-slate-200 p-6 rounded-xl shadow-sm mb-10">
    <div class="flex items-center gap-3 mb-6 border-b border-slate-100 pb-4">
        <div class="p-2 bg-emerald-50 text-emerald-600 rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3 10h18M3 14h18m-9-4v8m-7 0h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
            </svg>
        </div>
        <h2 class="text-2xl font-bold text-slate-800 tracking-tight">Monthly Sales by Company & Location</h2>
    </div>

```sql heatmap_data
WITH monthly_data AS (
  SELECT
    Company_Shortname as Company,
    Location_Shortname as Location,
    DATE_TRUNC('month', Invoice_Month) as Month_Date,
    strftime(Invoice_Month, '%b') as Month,
    COUNT(Vehicle_Key) as Sales
  FROM ${filtered_sales}
  WHERE Company_Shortname IS NOT NULL AND Location_Shortname IS NOT NULL
  GROUP BY Company_Shortname, Location_Shortname, Month_Date, Month
),
totals AS (
  SELECT
    Company,
    Location,
    SUM(Sales) as Total_Sales
  FROM monthly_data
  GROUP BY Company, Location
)
SELECT
  m.Company || ' - ' || m.Location as Entity,
  m.Month_Date,
  m.Month,
  m.Sales
FROM monthly_data m
JOIN totals t ON m.Company = t.Company AND m.Location = t.Location
ORDER BY t.Total_Sales DESC, Entity, m.Month_Date
```

    <Heatmap
        data={heatmap_data}
        x=Month
        y=Entity
        value=Sales
        valueLabels=true
        colorPalette={['#f8fafc', '#60a5fa', '#1e3a8a']}
        borders=true
        cellHeight=30
    />

</div>
