data = readmatrix('edpi.xlsx');
valid_data = data(~isnan(data));
minValue = 250;
maxValue = 580;
interval = 30;

edges = minValue:interval:maxValue;

[counts, ~] = histcounts(valid_data, edges);

figure;
bar(edges(1:end-1), counts);
title('The mouse sensitivity');
xlabel('Sensitivity');
ylabel('Frequency');