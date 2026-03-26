<!-- HEADER -->
<div class="mb-8 flex justify-between items-start">
    <div>
        <h1 class="text-4xl font-black text-slate-800 tracking-tight mb-2">Data Storytelling</h1>
        <p class="text-slate-500 text-lg max-w-2xl">
            The art of transforming raw data into intuitive visual narratives and interactive dashboards that drive meaningful business decisions.
        </p>
    </div>
    <a href="/" title="Back to Homepage" class="group flex items-center justify-center p-3 bg-white hover:bg-gradient-to-br hover:from-blue-500 hover:to-indigo-600 text-slate-400 hover:text-white rounded-2xl shadow-sm hover:shadow-xl border border-slate-200 hover:border-transparent transition-all duration-300 transform hover:-translate-y-1 hover:rotate-3 backdrop-blur-sm z-50">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 transition-transform group-hover:-translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
    </a>
</div>

<!-- INTRO BANNER -->
<div class="bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-100 rounded-2xl p-6 mb-10 flex gap-5 items-start shadow-sm">
    <div class="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center text-blue-600 flex-shrink-0 mt-0.5 shadow-inner">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
    </div>
    <div>
        <h2 class="font-bold text-slate-700 mb-1">What is Data Storytelling?</h2>
        <p class="text-slate-500 text-sm leading-relaxed">
            Data Storytelling standardizes KPIs across the organization, delivering instant and actionable insights. It helps users spot trends, identify anomalies at a glance, and make faster, evidence-based decisions — bridging the gap between raw numbers and clear business narratives.
        </p>
    </div>
</div>

<!-- DASHBOARD CARDS -->
<div class="mb-6">
    <p class="text-xs font-bold text-slate-400 uppercase tracking-[0.2em]">Available Dashboards</p>
    <div class="h-px bg-gradient-to-r from-slate-200 to-transparent mt-2 mb-8"></div>
</div>

<div class="w-full grid grid-cols-1 md:grid-cols-2 gap-8">

    <!-- Vehicle Aged Stock Card -->
    <a href="/vehicle-aged-stock" class="group block bg-white rounded-3xl p-8 shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-slate-100 hover:shadow-[0_8px_30px_rgb(0,0,0,0.12)] hover:border-blue-200 transition-all duration-300 transform hover:-translate-y-1 relative overflow-hidden">
        <div class="absolute top-0 right-0 w-32 h-32 bg-blue-50 rounded-bl-full -mr-8 -mt-8 transition-transform group-hover:scale-110"></div>
        <div class="relative z-10">
            <div class="w-14 h-14 bg-blue-100 rounded-2xl flex items-center justify-center mb-6 text-blue-600 group-hover:scale-110 group-hover:rotate-3 transition-transform duration-300 shadow-inner">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                </svg>
            </div>
            <h2 class="text-2xl font-bold text-slate-800 tracking-tight mb-3 group-hover:text-blue-600 transition-colors">Vehicle Aged Stock</h2>
            <p class="text-slate-500 leading-relaxed text-sm">
                A real-time snapshot of current vehicle inventory. Drill down by Company, Location, and Vehicle Class to identify aging stock and optimize turnover.
            </p>
        </div>
        <div class="relative z-10 mt-6 flex items-center text-blue-600 font-semibold group-hover:translate-x-2 transition-transform duration-300">
            <span>View Dashboard</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
        </div>
    </a>

    <!-- Vehicle Sales Volume Card -->
    <a href="/vehicle-sales-volume" class="group block bg-white rounded-3xl p-8 shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-slate-100 hover:shadow-[0_8px_30px_rgb(0,0,0,0.12)] hover:border-indigo-200 transition-all duration-300 transform hover:-translate-y-1 relative overflow-hidden">
        <div class="absolute top-0 right-0 w-32 h-32 bg-indigo-50 rounded-bl-full -mr-8 -mt-8 transition-transform group-hover:scale-110"></div>
        <div class="relative z-10">
            <div class="w-14 h-14 bg-indigo-100 rounded-2xl flex items-center justify-center mb-6 text-indigo-600 group-hover:scale-110 group-hover:-rotate-3 transition-transform duration-300 shadow-inner">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                </svg>
            </div>
            <h2 class="text-2xl font-bold text-slate-800 tracking-tight mb-3 group-hover:text-indigo-600 transition-colors">Vehicle Sales Volume</h2>
            <p class="text-slate-500 leading-relaxed text-sm">
                A comprehensive overview of sales performance across the network. Analyze historical data, monthly trends, and year-over-year comparisons by company and location.
            </p>
        </div>
        <div class="relative z-10 mt-6 flex items-center text-indigo-600 font-semibold group-hover:translate-x-2 transition-transform duration-300">
            <span>View Dashboard</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
        </div>
    </a>

</div>
