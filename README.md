# Hotel Booking Cancellation Analysis: Revenue Leakage Mitigation & Interactive BI Dashboard

## 📊 1. Case Overview & Corporate Objective
A luxury hotel chain was experiencing unpredictable and severe financial losses due to high reservation cancellation rates. The objective of this project was to track the root causes of booking volatility, analyze operational seasonality, and deploy a data-driven ecosystem to protect bottom-line profit margins.

This end-to-end analytics framework processes **119,390 historical transactions** to achieve three core milestones:
1. **Isolate Primary Risk Drivers:** Quantify and analyze factors causing high-frequency reservation churn.
2. **Track Seasonal Volatility:** Identify calendar periods experiencing extreme booking risk.
3. **Deploy Enterprise Business Intelligence:** Build a dynamic dashboard to enable real-time risk assessment and decision-making for leadership teams.

---

## 🛠️ 2. Tech Stack & Engineering Lifecycle
- **Data Engineering Engine:** Python (`pandas`) for programmatic transformation and pipeline validation.
- **Business Intelligence & Reporting:** Power BI Desktop & Power BI Service Architecture.
- **Data Methodology:** Descriptive Statistics, 4Vs of Big Data Audit framework.

---

## 📁 3. Workspace Directory Layout
- `/data`: Houses the raw source transactional dataset and output processing assets.
- `/scripts`: Automated Python data pipelines handling data type casting and missing value imputations.
- `/visuals`: Complete interactive Power BI dashboard workspace files (`.pbix`) and production interface captures.

---

## 📉 4. Data Quality & Programmatic Cleaning (Veracity Layer)
To ensure 100% data reliability across downstream visual reporting layers, an automated Python ETL pipeline was built to address raw data discrepancies:
- **Casting & Normalization:** Programmatically converted raw unstructured features (`adr`, `lead_time`, `is_canceled`) into strict numeric formats.
- **Missing Value Imputation:** Captured empty rows across critical metrics (`children`, `babies`, `lead_time`) and resolved them via zero-value fallbacks.
- **Feature Engineering:** Derived strategic calculated metrics to uncover deep patterns:
  * `TotalNightsStayed` = Cumulative duration of weekend and weeknight logs.
  * `TotalGuests` = Consolidated volume of adults, children, and infants.
  * `RevenuePerBooking` = Average Daily Rate (ADR) scaled by total nights stayed.
  * `BookingStatus` = Evaluated logical flags to segment rows into `Canceled` or `Confirmed`.

---

## 💡 5. Data-Driven Commercial Insights

### Baseline Operational Metrics
- **The Churn Baseline:** **37% of all total reservations** result in cancellations, creating a severe operational and inventory constraint.
- **Lead Time Multipliers:** Cancelled stays exhibit a significantly higher average lead time of **144.85 days**, compared to the overall baseline of 104 days. Longer booking windows directly correlate with increased cancellation risk.
- **High-Value Exposure:** The average daily rate (ADR) for cancelled stays (\$104.96) sits higher than the overall average (\$101.83). The maximum single cancellation reached **\$5,400**, representing severe high-value revenue leakage.
- **Duration Constraints:** The most common length of stay for a cancelled booking is **2 nights**, revealing that short-term transient bookings represent the highest risk profile.
- **Seasonality Peaks:** Cancellations are heavily clustered around seasonal metrics, with **August (5,239)**, **July (4,742)**, and **May (4,677)** registering the absolute highest volume peaks.

---

## 🌐 6. Interactive Power BI Dashboard Capabilities
The final deliverable integrates these analytical findings into an enterprise-grade interactive workspace:
- **Core KPI Blocks:** Provides immediate, high-level metrics tracking Total Bookings (119K), Total Cancellations (44K), Corporate Cancellation Rate (37%), and **$16.73M in Lost Revenue**.
- **Cross-Filtering Slicers:** Empowers management to slice cancellation patterns dynamically by **Hotel Type** (revealing that City Hotels experience the highest volatility), **Arrival Month**, and **Customer Segment**.
- **Distribution Channel Analytics:** Exposes critical channel performance, revealing that a massive **80% of all cancellations** are driven by third-party distribution networks, while the **Online Travel Agency (TA)** segment represents the highest volume risk.

---

## 📋 7. Actionable Business Recommendations
Based on the dashboard insights, the following strategic levers are recommended to protect revenue:
1. **Targeted Pricing Rules:** Deploy discounted, strict non-refundable booking rates tailored specifically for high-risk transient customer classes.
2. **Seasonal Cancellation Policies:** Introduce stricter down-payment rules and tighter cancellation restrictions during high-velocity peak blocks (April, May, and June).
3. **Direct Booking Optimization:** Reduce reliance on high-churn third-party online travel agencies by introducing bundle incentives for direct hotel reservations.
4. **Asset Quality Audit:** Dashboard metrics show that **Room Type A** exhibits the absolute highest frequency of cancellation flags. Recommend an immediate operational inspection of room conditions, layout amenities, and feedback logs to resolve hidden experience friction.
