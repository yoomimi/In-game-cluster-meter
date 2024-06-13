data = readmatrix('sensitivity.xlsx');
valid_data = data(~isnan(data));
minValue = 0;
maxValue = 1;
interval = 0.1;

edges = minValue:interval:maxValue;

[counts, ~] = histcounts(valid_data, edges);

figure;
bar(edges(1:end-1), counts);
title('The mouse sensitivity');
xlabel('Sensitivity');
ylabel('Frequency');