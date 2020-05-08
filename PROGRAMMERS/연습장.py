# for j = 1: 2
#     folder = ['V' num2str(j) '\*.jpg' ];
#     V_image = dir(folder);
#     for i = 1:10
#         name = V_image(i).name;
#         folder = V_image(i).folder;
#         path = [folder '\' name];
#         image = imread(path);
#     end   
# end

folder = []
for j in range(1, 3):
    folder += ['V' + str(j) + '.jpg']
print(folder)