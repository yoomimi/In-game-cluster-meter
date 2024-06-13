image_folder = 'valmin';  % 이미지 폴더 경로
num_images = 100;
clutter_scalar_fc_sum = 0;

tic  % 시간 측정 시작

exclude_images = [81];  % 제외할 이미지 번호 목록

for i = 0:(num_images-1)
    if ismember(i, exclude_images)
        continue;  % 제외할 이미지 건너뜀
    end
    
    image_filename = fullfile(image_folder, sprintf('frame_%d.jpg', i));  % 이미지 파일 경로 생성
    [clutter_scalar_fc, ~] = getClutter_FC(image_filename);  % getClutter_FC 함수 호출
    clutter_scalar_fc_sum = clutter_scalar_fc_sum + clutter_scalar_fc;  % clutter_scalar_fc 값 누적
end

toc  % 시간 측정 종료 및 출력

clutter_scalar_fc_avg = clutter_scalar_fc_sum / (num_images - numel(exclude_images))  % clutter_scalar_fc 값의 평균 계산