<div class="mb-8 flex justify-between items-start">
    <div>
        <h1 class="text-4xl font-black text-slate-800 tracking-tight mb-2">Vehicle Aged Stock</h1>
        <p class="text-slate-500 text-lg">This report provides a snapshot of your current vehicle stock. Use the filters below to drill down by Company, Location, and Vehicle Class.</p>
    </div>
    <a href="/" title="Back to Homepage" class="group flex items-center justify-center p-3 bg-white hover:bg-gradient-to-br hover:from-blue-500 hover:to-indigo-600 text-slate-400 hover:text-white rounded-2xl shadow-sm hover:shadow-xl border border-slate-200 hover:border-transparent transition-all duration-300 transform hover:-translate-y-1 hover:rotate-3 backdrop-blur-sm z-50">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 transition-transform group-hover:-translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
    </a>
</div>

<!-- DATA SOURCES FOR FILTERS -->

```sql companies
SELECT DISTINCT Company_Shortname
FROM demo_dealer_ai.vehicle_stock_current
WHERE Company_Shortname IS NOT NULL
ORDER BY Company_Shortname
```

```sql locations
SELECT DISTINCT Location_Shortname
FROM demo_dealer_ai.vehicle_stock_current
WHERE Location_Shortname IS NOT NULL
  AND Company_Shortname IN ${inputs.selected_company.value}
ORDER BY Location_Shortname
```

```sql vehicle_classes
SELECT DISTINCT Vehicle_Class_Description
FROM demo_dealer_ai.vehicle_stock_current
WHERE Vehicle_Class_Description IS NOT NULL
ORDER BY Vehicle_Class_Description
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
        <Dropdown data={companies} name="selected_company" value=Company_Shortname title="Company" multiple=true selectAllByDefault=true />
        <Dropdown data={locations} name="selected_location" value=Location_Shortname title="Location" multiple=true selectAllByDefault=true />
        <Dropdown data={vehicle_classes} name="selected_class" value=Vehicle_Class_Description title="Vehicle Class" multiple=true selectAllByDefault=true />
    </div>
</div>

<!-- FILTERED DATA -->

```sql filtered_stock
SELECT *
FROM demo_dealer_ai.vehicle_stock_current
WHERE Company_Shortname IN ${inputs.selected_company.value}
  AND Location_Shortname IN ${inputs.selected_location.value}
  AND Vehicle_Class_Description IN ${inputs.selected_class.value}
```

<!-- TOTAL VEHICLES CARD -->

```sql total_vehicles
SELECT COUNT(Vehicle_Key) as total_count
FROM ${filtered_stock}
```

<div class="flex justify-center w-full mt-8 mb-16">
    <div class="bg-white rounded-2xl shadow-[0_8px_30px_rgb(0,0,0,0.12)] border border-slate-200 px-10 py-8 flex flex-col items-center min-w-[350px] transform hover:scale-105 transition-all duration-300">
        <h3 class="text-slate-500 font-bold text-sm tracking-widest uppercase mb-3">Total Vehicles in Stock</h3>
        <div class="text-6xl font-black text-slate-800 mb-1 tracking-tight drop-shadow-sm">
            <Value data={total_vehicles} column=total_count fmt="num0" />
        </div>
    </div>
</div>

<!-- DONUT CHART: Vehicles by Class -->

```sql stock_by_class
SELECT
  Vehicle_Class_Description,
  COUNT(Vehicle_Key) as vehicle_count
FROM ${filtered_stock}
WHERE Vehicle_Class_Description IS NOT NULL
GROUP BY Vehicle_Class_Description
ORDER BY vehicle_count DESC
```

<div class="bg-white border border-slate-200 p-6 rounded-xl shadow-sm mb-10 transform hover:-translate-y-1 transition-transform duration-300">
    <div class="flex items-center gap-3 mb-6 border-b border-slate-100 pb-4">
        <div class="p-2 bg-violet-50 text-violet-600 rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z" />
                <path stroke-linecap="round" stroke-linejoin="round" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z" />
            </svg>
        </div>
        <h2 class="text-2xl font-bold text-slate-800 tracking-tight">Vehicles in Stock by Class</h2>
    </div>

    <ECharts config={{
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
            data: stock_by_class.map(d => ({ value: d.vehicle_count, name: d.Vehicle_Class_Description }))
        }
    ]
    }} />

</div>

<!-- BAR CHART: Vehicles by Days In Stock Category -->

```sql stock_by_days_category
SELECT
  Days_In_Stock_Category_Description,
  Days_In_Stock_Category_ID,
  COUNT(Vehicle_Key) as vehicle_count
FROM ${filtered_stock}
WHERE Days_In_Stock_Category_Description IS NOT NULL
GROUP BY Days_In_Stock_Category_Description, Days_In_Stock_Category_ID
ORDER BY Days_In_Stock_Category_ID
```

```sql total_for_pct
SELECT COUNT(Vehicle_Key) as total
FROM ${filtered_stock}
```

<div class="bg-white border border-slate-200 p-6 rounded-xl shadow-sm mb-10 transform hover:-translate-y-1 transition-transform duration-300">
    <div class="flex items-center gap-3 mb-6 border-b border-slate-100 pb-4">
        <div class="p-2 bg-amber-50 text-amber-600 rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" />
            </svg>
        </div>
        <h2 class="text-2xl font-bold text-slate-800 tracking-tight">Vehicles in Stock by Days in Stock</h2>
    </div>

    <ECharts config={{
    tooltip: {
        trigger: 'axis',
        axisPointer: { type: 'shadow' }
    },
    xAxis: {
        type: 'category',
        data: stock_by_days_category.map(d => d.Days_In_Stock_Category_Description),
        axisLabel: { fontSize: 12 }
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        type: 'bar',
        data: stock_by_days_category.map(d => d.vehicle_count),
        itemStyle: {
            color: '#236aa4',
            borderRadius: [4, 4, 0, 0]
        },
        label: {
            show: true,
            position: 'top',
            formatter: (params) => {
                const total = total_for_pct[0].total;
                const pct = (params.value / total * 100).toFixed(1);
                return params.value.toLocaleString() + ' (' + pct + '%)';
            },
            fontSize: 11
        }
    }]
    }}/>

</div>

<!-- HORIZONTAL BAR CHART: Vehicles by Make -->

```sql stock_by_make
SELECT
  Make_Name,
  COUNT(Vehicle_Key) as vehicle_count
FROM ${filtered_stock}
WHERE Make_Name IS NOT NULL
GROUP BY Make_Name
ORDER BY vehicle_count DESC
```

<div class="bg-white border border-slate-200 p-6 rounded-xl shadow-sm mb-10 transform hover:-translate-y-1 transition-transform duration-300">
    <div class="flex items-center gap-3 mb-6 border-b border-slate-100 pb-4">
        <div class="p-2 bg-indigo-50 text-indigo-600 rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2z" />
            </svg>
        </div>
        <h2 class="text-2xl font-bold text-slate-800 tracking-tight">Vehicles in Stock by Make</h2>
    </div>

    <BarChart
        data={stock_by_make}
        x="Make_Name"
        y="vehicle_count"
        swapXY=true
        labels=true
    />

</div>

<div class="bg-white border border-slate-200 p-6 rounded-xl shadow-sm mb-10">
    <div class="flex items-center gap-3 mb-6 border-b border-slate-100 pb-4">
        <div class="p-2 bg-emerald-50 text-emerald-600 rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3 10h18M3 14h18m-9-4v8m-7 0h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
            </svg>
        </div>
        <h2 class="text-2xl font-bold text-slate-800 tracking-tight">Aged Stock by Company & Location</h2>
    </div>

```sql heatmap_data
WITH category_data AS (
  SELECT
    Company_Shortname as Company,
    Location_Shortname as Location,
    Days_In_Stock_Category_Description as Category,
    Days_In_Stock_Category_ID as Category_ID,
    COUNT(Vehicle_Key) as Stock_Count
  FROM ${filtered_stock}
  WHERE Company_Shortname IS NOT NULL
    AND Location_Shortname IS NOT NULL
    AND Days_In_Stock_Category_Description IS NOT NULL
  GROUP BY Company_Shortname, Location_Shortname, Days_In_Stock_Category_Description, Days_In_Stock_Category_ID
),
totals AS (
  SELECT
    Company,
    Location,
    SUM(Stock_Count) as Total_Stock
  FROM category_data
  GROUP BY Company, Location
)
SELECT
  c.Company || ' - ' || c.Location as Entity,
  c.Category,
  c.Category_ID,
  c.Stock_Count
FROM category_data c
JOIN totals t ON c.Company = t.Company AND c.Location = t.Location
ORDER BY t.Total_Stock DESC, Entity, c.Category_ID
```

    <Heatmap
        data={heatmap_data}
        x=Category
        y=Entity
        value=Stock_Count
        valueLabels=true
        colorPalette={['#f8fafc', '#ec4899', '#9f1239']}
        borders=true
        cellHeight=30
    />

</div>
