image_folder = ['pro_split_cap'];  % 이미지 폴더 경로
num_images = 450;
clutter_scalar_fc_array = zeros(1, num_images); % 배열 preallocation

tic  % 시간 측정 시작

for i = 1:num_images
    
    image_filename = fullfile(image_folder, sprintf('frame_%d.jpg', i));  % 이미지 파일 경로 생성
    [clutter_scalar_fc, ~] = getClutter_FC(image_filename);  % getClutter_FC 함수 호출
    
    clutter_scalar_fc_array(i) = clutter_scalar_fc;  % clutter_scalar_fc 값을 배열에 저장
end

toc  % 시간 측정 종료 및 출력

clutter_scalar_fc_avg = mean(clutter_scalar_fc_array); % clutter_scalar_fc 값의 평균 계산

% clutter_scalar_fc_array의 그래프 그리기
figure;
plot(clutter_scalar_fc_array, 'b');
xlabel('Image Index');
ylabel('Clutter Scalar FC');
title('Clutter Scalar FC for Each Image');