from exercise_1 import load_my_image, apply_conv_to_image, show, print_hints
# Detects bright pixels over dark pixels. 
horizontal_line_conv = [[1, 1], 
                        [-1, -1]]
vertical_line_conv = [[1,-1],
                      [1,1]]
conv_list = [horizontal_line_conv,vertical_line_conv]

original_image = load_my_image()
print("Original image")
show(original_image)
for conv in conv_list:
    filtered_image = apply_conv_to_image(conv, original_image)
    print("Output: ")
    show(filtered_image)