#!/bin/bash
# Experiment on an real-life event log - RQ1, RQ2 with baseline approach

# Each file contains instnaces released in each date for resource allocation
date_array=('2016-07-04' '2016-10-31' '2016-06-06' '2016-06-22' '2016-09-13' '2016-08-29' '2016-10-25' )


for date in "${date_array[@]}"; do
	python baseline_main.py --test_path "./sample_data/real_Dilyar/tests/modi_assignment_filtered_test_$date.csv" --date $date --mode 'real' --exp_name 'exp_4-baseline_Dilyar_test'
done;