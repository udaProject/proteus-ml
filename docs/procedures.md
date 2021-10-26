## Explanation of growth procedure
- Import data set. Assume all data points are comprised of a common domain of vector components.
- Initialize with 2 charts (nodes) in graph data structure; they should be connected by an edge. Each chart has an associated reference vector whose components match the domain of the data points. Each chart has a list of directed edges to other charts. The edges in each chart's list contain a reference to the chart pointed to, a real-valued signal counter, and a real-valued 'utility' variable. Each chart has an accumulated error vector rooted at the head of the reference vector of the chart.
- Sample data point of data set. Compute distance of point to all existing charts in the map (graph) which is linear complexity in the number of charts, or more ideally use a similarity search structure instead which is log or polylog complexity in the number of charts.
- Select the 2 charts whose reference vectors that have the smallest distances to the sampled data point.
- Consider the closest chart the 1st BMU (the best matching unit) and the second closest the 2nd BMU.
- If there is no edge between the 1st and 2nd BMU, create one; this entails creating an entry in both charts since the edges are directed. Then set signal counter of the BMU toward the 2nd BMU to '1'; otherwise, increment signal counter of the BMU directed toward the 2nd BMU by '1'.
- Identify the topological neighbors of the 1st BMU and the 2nd BMU. Find the intersection of these two neighborhood sets. !!!Is not necessary a clique; must run routine to find subset of these vertices that define a clique!!! This defines a simplex containing the signal.
- Compute difference between the signal vector (sampled data point) and vertices of the simplex.
- The difference between the 1st BMU and the signal should be the smallest (by definition of the BMU). Use this distance to calculate the amount of "work" that would be required to move the BMU to the signal.
- For now, define 'k' as the sum of all the counters across all of the chart's edges divided by the value of the counter from the 1st BMU to 2nd BMU. That is, `edge_counter(1stBMU_to_2ndBMU) /divide /sum_over_all_edges( edge_counters )`
- The "work" (error energy) done is `k*(1/t)*(magnitude_of_difference)^2` where `t = -D*log(1-SF)`
- The idea is to treat the "work" that would have been required to move the BMU to the signal as the current error of the model (in terms of the energy that would be required to remove the error completely by moving the chart's reference vector to the signal). We want to remove some of the error by computing changes to the reference vectors of charts in the simplex containing the signal.
- Changes to reference vectors of charts in the simplex containing the signal designated 'shifts'.
- Add shifts for each chart to their respective "avg_err" props.
- Magnitude of "destroyed" avg_err (caused by simple vector addition of a shift to the avg_err vector) caused by previous step is added to chart "acc_heat"
- If `avg_err/sqrt(total_count) < \phi * sqrt(t)`, where 't' is scale parameter and `\phi = temp_exp/temp_avg and temp_exp = temp * (.7)^2` and `temp = acc_heat/(total_count-1)` and `temp_avg = sum(temp_n)/total_charts`
- Compute error energies w/ resp. to signal for all charts in simplex. Difference between shift and error energy is residual error energy.
- Residual error energy of 1st BMU (chart0) is actually a total error (since error is defined by in reference to this chart)
- (chart1 res. error energy) - (chart0 total error energy) ---> edge 1,0 utility (binding energy)
- (chart2 res. error energy) - (chart1 res. error energy) - (chart0 total error energy) ---> edge 2,0 utility (binding energy)
- Continue for all charts
- Should in general be some total error energy left (because of inverse quadratic dependence on distance and assumption about ordering (chart3 farther away than chart2 farther away than chart1 from chart0, etc...) ).
- Add final remaining residual to "acc_res" prop
- For any chart in simplex, if `mag(acc_res) + (avg_err * acc_res) >= GT` then trigger chart growth in direction of acc_res.
- Place new chart `avg( mag(edge links) )` distance in direction of acc_res?
- etc...

## Explanation of generation procedure
Under Construction!

## Explanation of classification procedure
Under Construction!

## Explanation of querying procedure
Under Construction!
