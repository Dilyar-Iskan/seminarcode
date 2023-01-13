#!/bin/bash
# Experiment on an real-life event log - RQ1, RQ2 with proposed method

# Threshold for the prediction accuracy
threshold=(1.0)

# Each file contains instnaces released in each date for resource allocation
# date_array=('2012-03-01' '2012-03-02' '2012-03-03' '2012-03-04' '2012-03-05' '2012-03-06' '2012-03-07' '2012-03-08' '2012-03-09' '2012-03-10' '2012-03-11' '2012-03-12' '2012-03-13' '2012-03-14' '2012-03-15')
date_array=('2012-03-01' '2012-03-02' '2012-03-03' '2012-03-04' '2012-03-05' '2012-03-06' '2012-03-07' '2012-03-08' '2012-03-09' '2012-03-10' '2012-03-11' '2012-03-12' '2012-03-13' '2012-03-14' )


for alpha in "${threshold[@]}"; do
	for date in "${date_array[@]}"; do
		python suggested_main.py --alpha $alpha --beta $alpha --test_path "./sample_data/real/modi_BPI_2012_$date.csv" --date $date --mode 'real' --exp_name 'exp_3_Dilyar'
	done;
done;