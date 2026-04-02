# BRTS Data Cleaning and AI Enhancement Project

## Project Overview

This project focuses on cleaning, imputing, and enhancing a large BRTS (Bus Rapid Transit System) GPS dataset containing more than **5 million records**. The objective was to detect missing and inconsistent data, reconstruct missing values using AI-based techniques, and improve the overall data quality for further analysis.

---

## Dataset Information

Total Records: **5,128,352**

Total Columns: **17 (original)**

Data fields included:

* DepartmentName
* HistoryId
* SequenceNo
* OBUId
* InsertTime
* Longitude
* Latitude
* Speed
* Heading
* Hdop
* GPSTime
* Location (initially empty)
* UpdatedTime
* VehicleID
* VehicleNumber
* RegNo
* OperatorName

---

## Problems Identified

During the data audit phase, the following issues were found:

* Location column was 100% missing
* 16,715 missing timestamp values
* ~1.9 million speed values recorded as zero
* ~877,000 incorrect speed values detected (vehicle moving but speed = 0)
* Some unrealistic speed readings

---

## Methodology

### Step 1 – Data Loading

* Combined multiple CSV datasets using Python Pandas
* Created a structured data processing pipeline

### Step 2 – Data Audit (EDA)

* Checked missing values
* Checked zero values
* Checked duplicates
* Analyzed speed distribution
* Verified GPS coordinate ranges

### Step 3 – Data Cleaning

* Removed fully empty columns
* Converted timestamp columns to datetime format
* Removed unrealistic speed values
* Sorted data by vehicle and timestamp

### Step 4 – Timestamp Imputation

Missing InsertTime and UpdatedTime values were filled using GPSTime as a reference.

### Step 5 – AI-based Speed Correction

Incorrect speed values were detected using GPS movement logic:

If GPS coordinates changed but speed was zero → value considered incorrect.

These values were:

* Converted to missing values
* Filled using vehicle-wise interpolation
* Remaining gaps filled using vehicle averages

### Step 6 – Location Reconstruction (AI Enrichment)

Since the Location column was empty:

* GPS coordinates were rounded to reduce unique points
* Unique locations reduced from 2.8 million to 2047
* Reverse geocoding was applied
* Location names were reconstructed
* Location data merged back into main dataset

---

## AI Techniques Used

The following AI/data science techniques were applied:

* Data imputation
* Time-series interpolation
* Statistical imputation
* Geospatial enrichment
* Reverse geocoding
* Data validation rules

---

## Results

Total records processed: **5,128,352**

Improvements achieved:

* Missing timestamps fixed: **16,715**
* Incorrect speed values corrected: **~638,000**
* Missing values after processing: **0**
* Location column successfully reconstructed
* Improved dataset consistency and reliability

---

## Project Structure

Data_brts/

raw_data/

* jbm1 16-20.csv
* jbm2 16-20.csv

scripts/

* step1_load.py
* step2_audit.py
* step3_clean.py
* step4_impute_time.py
* step5_speed_analysis.py
* step6_detect_false_zero.py
* step7_impute_speed.py
* step8_report.py
* step9_unique_locations.py
* step10_reduce_locations.py
* step11_geocode_test.py
* step12_build_location_lookup.py
* step13_merge_location.py

output/

* cleaned_brts.csv
* time_fixed_brts.csv
* ai_enhanced_brts.csv
* location_lookup.csv
* final_brts_ai_dataset.csv

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn (imputation concepts)
* Geopy (reverse geocoding)

---

## Final Output

Final deliverable:

**final_brts_ai_dataset.csv**

This dataset contains cleaned, imputed, and AI-enhanced transport telemetry data ready for analysis.

---

## Conclusion

This project demonstrates how large-scale transport datasets can be cleaned and improved using Python and AI-based data preprocessing techniques. The final dataset has improved completeness, consistency, and usability for further analytics and machine learning applications.

## Dataset Note

Due to large file size (>500MB), full datasets are not included in this repository.

A small sample dataset is provided for demonstration.

Full dataset available upon request.

## Raw Data
https://drive.google.com/file/d/1GRGvfM7EDLH2Z5hnN0YW-pZnyMlk2P2o/view?usp=sharing

## Modified Data
https://drive.google.com/drive/folders/10OTFNHrshbDQFUlxecfBOZzRC_1TPzB9?usp=sharing

