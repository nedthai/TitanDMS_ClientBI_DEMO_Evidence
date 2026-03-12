<div class="min-h-[80vh] flex flex-col items-center justify-center p-6 bg-gradient-to-br from-slate-50 to-slate-100 font-sans">
    <!-- Header Section -->
    <div class="w-full max-w-5xl mx-auto flex flex-col items-center text-center space-y-6 mb-16">
        <div class="w-36 h-36 bg-white rounded-3xl p-5 shadow-[0_8px_30px_rgb(0,0,0,0.08)] mb-6 flex items-center justify-center border border-slate-100 transform hover:scale-105 transition-all duration-300">
            <img src="/logo.png" alt="Dealer Comprehensive Invision Logo" class="w-full h-full object-contain" />
        </div>
        <div>
            <h1 class="text-5xl md:text-6xl font-black text-slate-800 tracking-tight mb-4 drop-shadow-sm">
                DEALER COMPREHENSIVE <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600">INVISION</span>
            </h1>
            <p class="text-xl text-slate-500 max-w-2xl mx-auto leading-relaxed">
                Welcome to your command center. Access real-time insights into your vehicle stock and sales network performance.
            </p>
        </div>
    </div>

    <!-- Navigation Cards -->
    <div class="w-full max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">

        <!-- Aged Stock Card -->
        <a href="/vehicle-aged-stock" class="group block bg-white rounded-3xl p-8 shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-slate-100 hover:shadow-[0_8px_30px_rgb(0,0,0,0.12)] hover:border-blue-200 transition-all duration-300 transform hover:-translate-y-1 relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-blue-50 rounded-bl-full -mr-8 -mt-8 transition-transform group-hover:scale-110"></div>
            <div class="relative z-10">
                <div class="w-14 h-14 bg-blue-100 rounded-2xl flex items-center justify-center mb-6 text-blue-600 group-hover:scale-110 group-hover:rotate-3 transition-transform duration-300 shadow-inner">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                    </svg>
                </div>
                <h2 class="text-2xl font-bold text-slate-800 tracking-tight mb-3 group-hover:text-blue-600 transition-colors">Vehicle Aged Stock</h2>
                <p class="text-slate-500 leading-relaxed">
                    View a snapshot of your current vehicle stock. Drill down by Company, Location, and Vehicle Class to optimize inventory.
                </p>
            </div>
            <div class="relative z-10 mt-6 flex items-center text-blue-600 font-semibold group-hover:translate-x-2 transition-transform duration-300">
                <span>View Dashboard</span>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
            </div>
        </a>

        <!-- Sales Volume Card -->
        <a href="/vehicle-sales-volume" class="group block bg-white rounded-3xl p-8 shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-slate-100 hover:shadow-[0_8px_30px_rgb(0,0,0,0.12)] hover:border-indigo-200 transition-all duration-300 transform hover:-translate-y-1 relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-indigo-50 rounded-bl-full -mr-8 -mt-8 transition-transform group-hover:scale-110"></div>
            <div class="relative z-10">
                <div class="w-14 h-14 bg-indigo-100 rounded-2xl flex items-center justify-center mb-6 text-indigo-600 group-hover:scale-110 group-hover:-rotate-3 transition-transform duration-300 shadow-inner">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                    </svg>
                </div>
                <h2 class="text-2xl font-bold text-slate-800 tracking-tight mb-3 group-hover:text-indigo-600 transition-colors">Vehicle Sales Volume</h2>
                <p class="text-slate-500 leading-relaxed">
                    Access a comprehensive overview of your sales network. Analyze historical performance and monthly sales trends.
                </p>
            </div>
             <div class="relative z-10 mt-6 flex items-center text-indigo-600 font-semibold group-hover:translate-x-2 transition-transform duration-300">
                <span>View Dashboard</span>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
            </div>
        </a>

        <!-- Predictive Forecast Card -->
        <a href="/predictive-sales-forecast" class="group block bg-white rounded-3xl p-8 shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-slate-100 hover:shadow-[0_8px_30px_rgb(0,0,0,0.12)] hover:border-emerald-200 transition-all duration-300 transform hover:-translate-y-1 relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-emerald-50 rounded-bl-full -mr-8 -mt-8 transition-transform group-hover:scale-110"></div>
            <div class="relative z-10">
                <div class="w-14 h-14 bg-emerald-100 rounded-2xl flex items-center justify-center mb-6 text-emerald-600 group-hover:scale-110 group-hover:-rotate-3 transition-transform duration-300 shadow-inner">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                    </svg>
                </div>
                <h2 class="text-2xl font-bold text-slate-800 tracking-tight mb-3 group-hover:text-emerald-600 transition-colors">Predictive Forecast</h2>
                <p class="text-slate-500 leading-relaxed">
                    Harness advanced Simple Linear Regression to accurately predict your sales volume over the next 6 months.
                </p>
            </div>
             <div class="relative z-10 mt-6 flex items-center text-emerald-600 font-semibold group-hover:translate-x-2 transition-transform duration-300">
                <span>View Dashboard</span>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
            </div>
        </a>

    </div>

</div>
