# data-analytics-internship
# 🚀 60 Days Data Analytics Internship

## 📌 Task 1 - Data Immersion & Wrangling

---

### 📦 Dataset 1 - Superstore Sales

| Detail | Info |
|---|---|
| Rows | 9,800 |
| Columns | 18 → 21 (after cleaning) |
| Source | Kaggle Superstore Dataset |

#### Issues Found & Fixed
| Issue | Fix |
|---|---|
| Order Date & Ship Date were strings | Converted to datetime |
| Postal Code was float with 11 nulls | Converted to string, nulls → "Unknown" |
| No new time features | Added Order Year, Order Month, Shipping Days |

#### Key Stats
- Only Postal Code had 11 missing values
- 1,145 Sales outliers detected (kept — likely bulk orders)
- 0 duplicate rows

---
