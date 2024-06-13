
%clutter_se = getClutter_SE('frame_92.jpg')

% get Feature Congestion clutter of a test map:
[clutter_scalar_fc, clutter_map_fc] = getClutter_FC('proset.jpg');
% display the clutter map and output the scalar
%figure, imshow((clutter_map_fc-min(clutter_map_fc(:)))/(max(clutter_map_fc(:))-min(clutter_map_fc(:))));
%title('Feature Congestion clutter map');
clutter_scalar_fc