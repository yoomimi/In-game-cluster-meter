
% 제외할 인덱스
indices_to_exclude = [35, 276];

% 35번과 276번을 제외한 새로운 배열 생성
new_array = clutter_scalar_fc_array;
new_array(indices_to_exclude) = [];

figure;
plot(new_array, 'b');
xlabel('Image Index');
ylabel('Clutter Scalar FC');
title('Clutter Scalar FC for Each Image');
