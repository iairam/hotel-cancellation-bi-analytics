# =========================================================================
# PROJECT: HOTEL BOOKING CANCELLATION ANALYSIS & REVENUE OPTIMIZATION
# =========================================================================

# -------------------------------------------------------------------------
# 1. LOAD THE DATASET
# -------------------------------------------------------------------------
import pandas as pd 

file_path = "table_HOTEL_BOOKING_DEMAND_DATASET.csv"  
df = pd.read_csv(file_path) 
 
# -------------------------------------------------------------------------
# 2. CONVERT COLUMNS TO NUMERIC DATA TYPES
# -------------------------------------------------------------------------
numeric_columns = [ 
    "stays_in_weekend_nights", "stays_in_week_nights", "adults", 
    "children", "babies", "adr", "is_canceled", "lead_time"  
] 
 
for col in numeric_columns: 
    df[col] = pd.to_numeric(df[col], errors="coerce")  # Convert and set errors to NaN 
 
# -------------------------------------------------------------------------
# 3. FILL MISSING DATA VALUES (NaN TO 0)
# -------------------------------------------------------------------------
df[["children", "babies", "lead_time"]] = df[["children", "babies", "lead_time"]].fillna(0) 
 
# -------------------------------------------------------------------------
# 4. CREATE NEW CALCULATED COLUMNS (FEATURE ENGINEERING)
# -------------------------------------------------------------------------
df["TotalNightsStayed"] = df["stays_in_weekend_nights"] + df["stays_in_week_nights"] 
df["TotalGuests"] = df["adults"] + df["children"] + df["babies"] 
df["RevenuePerBooking"] = df["adr"] * df["TotalNightsStayed"] 
df["BookingStatus"] = df["is_canceled"].apply(lambda x: "Canceled" if x == 1 else "Confirmed") 
 
# Display the first few rows with new calculated columns 
print("\nNew Calculated Columns:\n", df[["TotalNightsStayed", "TotalGuests", "RevenuePerBooking", "BookingStatus"]].head()) 
 
# Select relevant columns for cancellation analysis 
cancellation_columns = ["lead_time", "adr", "TotalNightsStayed", "is_canceled"] 
 
# Check if all columns exist in the dataset 
existing_columns = [col for col in cancellation_columns if col in df.columns]

# -------------------------------------------------------------------------
# 5. GENERATE DESCRIPTIVE STATISTICS
# -------------------------------------------------------------------------
if existing_columns: 
    # Compute descriptive statistics for selected columns 
    cancellation_stats = df[existing_columns].describe() 
 
    # Filter dataset for canceled bookings 
    canceled_df = df[df["is_canceled"] == 1] 
 
    # Compute descriptive statistics for canceled bookings 
    canceled_stats = canceled_df[existing_columns].describe() 
 
    # Display results 
    print("\nOverall Descriptive Statistics:\n", cancellation_stats) 
    print("\nDescriptive Statistics for Canceled Bookings:\n", canceled_stats) 
 
    # Additional Insights: 
    # - Most common length of stay 
    most_common_stay = df["TotalNightsStayed"].mode()[0] 
    print(f"\nMost Common Length of Stay: {most_common_stay} nights.") 
 
    # - Peak cancellation period (most frequent months for cancellations) 
    df["arrival_date_month"] = df["arrival_date_month"].astype(str) 
    peak_cancellation_months = canceled_df["arrival_date_month"].value_counts().head(3) 
    print("\nPeak Cancellation Period (Top 3 Months):\n", peak_cancellation_months) 
 
    # - Maximum ADR for canceled bookings (high-value bookings canceled) 
    max_adr_canceled = canceled_df["adr"].max() 
    print(f"\nMaximum ADR for Canceled Bookings: ${max_adr_canceled}") 
 
else: 
    print("\nNo valid columns found for descriptive statistics.") 
 
# -------------------------------------------------------------------------
# 6. EXPORT CLEAN CLEANED FILE FOR POWER BI
# -------------------------------------------------------------------------
df.to_csv("Modified_Hotel_Booking.csv", index=False) 
print("\nModified dataset saved as 'Modified_Hotel_Booking.csv'")
