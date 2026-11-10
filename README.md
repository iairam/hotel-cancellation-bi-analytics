# Hotel Booking Cancellations: Analyzing Revenue Losses & Building a Power BI Dashboard

## 📊 Quick Summary
A luxury hotel chain was losing significant revenue ($16.73M) due to unpredicted booking cancellations. I built an analytics workflow using Python to clean 119,390 transaction records and designed an interactive Power BI dashboard to help management identify cancellation patterns, track seasonal drops, and adjust booking rules.

---

## 🛠️ The Tech Stack
- **Data Prep:** Python (Pandas)
- **Visuals & Dashboard:** Power BI Desktop & Service
- **Core Approach:** Descriptive Statistics & 4Vs of Big Data Audit

---

## 📁 Repository Structure
- `/scripts/hotel_analysis.py` -> The Python data preparation script
- `/visuals/assignment 1.pbix` -> The actual interactive Power BI dashboard file
- `/visuals/dashboard_screenshot.png` -> Preview image of the finished dashboard layout

---

## 🧼 How the Data Was Prepared (Python Pipeline)
Before building the dashboard, I used Python to fix data quality issues in the raw dataset:
- **Type Conversion:** Converted stays, guests, and pricing rows into strict numeric formats.
- **Handling Missing Values:** Filled null values in the `children`, `babies`, and `lead_time` columns with 0.
- **Engineered Metrics:** Created four new calculated columns to drive the analysis:
  * `TotalNightsStayed` (Weekend nights + Week nights)
  * `TotalGuests` (Adults + Children + Babies)
  * `RevenuePerBooking` (ADR * Total Nights Stayed)
  * `BookingStatus` (Flags rows as "Canceled" or "Confirmed")

---

## 💡 Key Business Insights Found
- **The Churn Baseline:** 37% of all hotel reservations get canceled, heavily draining operational revenue.
- **Longer Planning = Higher Churn:** Canceled bookings have a much longer average lead time (144.85 days) compared to confirmed bookings (104 days).
- **High-Value Exposure:** The average daily rate (ADR) for canceled bookings is higher ($104.96) than the overall average ($101.83). The largest single canceled booking hit $5,400.
- **Short Stays Churn Fastest:** The most common length of stay for a canceled booking is just 2 nights.
- **Seasonality Peaks:** Cancellations peak heavily during the end of spring and summer, led by August (5,239), July (4,742), and May (4,677).

---

## 🌐 The Power BI Dashboard Capabilities
The interactive dashboard provides the management team with a clean visual toolkit:
- **Main KPI Counters:** Tracks Total Bookings (119K), Cancellations (44K), Corporate Cancellation Rate (37%), and $16.73M in Lost Revenue at a single glance.
- **Dynamic Filters:** Allows users to slice data instantly by Hotel Type, Arrival Month, and Customer Type (revealing that City Hotels face the highest volatility).
- **Channel Issues:** Exposes the fact that 80% of all cancellations are driven by third-party distribution networks, with the Online Travel Agency (TA) segment acting as the highest risk zone.

---

## 📋 Actionable Next Steps for Management
1. **Change Pricing Rules:** Offer discounted, strict non-refundable booking rates for transient customers to reduce baseline cancellations.
2. **Stricter Peak Rules:** Introduce stricter cancellation deadlines and down-payments during high-churn months (April, May, and June).
3. **Optimize Direct Bookings:** Create special bundle deals for direct website reservations to lower our dependence on high-churn third-party online platforms.
4. **Inspect Room Type A:** This specific room configuration shows the absolute highest frequency of cancellation flags. The team needs to review its room conditions, features, and feedback logs to see what is causing the friction.
