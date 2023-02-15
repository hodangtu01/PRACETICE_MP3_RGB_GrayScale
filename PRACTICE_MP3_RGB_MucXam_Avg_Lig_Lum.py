import cv2 # Sử dụng thư viện xử lý ảnh OpenCV
import numpy as np # Thư viện toán học liên quan đến ma trận
from PIL import Image # Sử dụng thư viện PILLOW hỗ trợ nhiều định dạng ảnh  

# Khai báo đường dẫn file ảnh
filehinh =r'bird.jpg'

# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

# Đọc ảnh màu sử dụng thư viện PIL (thay vì dùng OpenCV). Ảnh PIL dùng để thực hiện các tác vụ xử lý & tính toán 
# Dùng OpenCV để hiển thị
imgPIL = Image.open(filehinh)

# Tạo một ảnh có cùng kích thước và mode với ảnh imgPIL (sao chép tất cả kích thước ảnh trên)
# Ảnh này dùng để chứa kết quả chuyển đổi RGB sang Grayscale
#PIL. Phương thức Image.new() tạo ra một image mới với chế độ và size đã cho. 
# Kích thước được đưa ra dưới dạng bộ (chiều rộng, chiều cao), tính bằng pixel. 
# Màu sắc được đưa ra dưới dạng một giá trị duy nhất cho hình ảnh một dải 
# và bộ cho hình ảnh nhiều băng tần (với một giá trị cho mỗi dải).
average = Image.new(imgPIL.mode, imgPIL.size)
print(average)
lightness = Image.new(imgPIL.mode, imgPIL.size)
print(lightness)
luminance = Image.new(imgPIL.mode, imgPIL.size)
print(luminance)

# Lấy kích thước của ảnh từ imgPIL
# Kích thước ảnh chung cho Average, Lightness, Luminance
width = average.size[0]
print(width)
height = average.size[1]
print(height)

# Mỗi ảnh là một ma trận hai chiều nên sẽ dùng 2 vòng for
# để đọc hết các điểm ảnh(pixel) có trong ảnh 
for x in range(width):
    for y in range(height):
        # Lấy giá trị điểm ảnh tại vị trí (x, y)
        # Là 1 vector 3 giá trị R, G, B trả về từ hàm getpixel tại vị trí (x, y) của ảnh đọc bằng thư viện PILLOW 
        R, G, B = imgPIL.getpixel((x, y)) 
        MIN = min(R, G, B)
        MAX = max(R, G, B)

        # Công thức chuyển ảnh màu RGB thành điểm ảnh mức xám sử dụng phương pháp Average
        # Sử dụng thư viện numpy, ép kiểu dữ liệu về int 8 bit từ 0 đến 255
        gray1 = np.uint8((R + G + B)/3)
        gray2 = np.uint8((MAX + MIN) /2)
        gray3 = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)

        # Thực hiện giá trị gray hiển thị có bộ gtri 0 đến 255
        # Sau khi đã tính được giá trị mức xám gán vào ảnh xám
        average.putpixel((x, y), (gray1, gray1, gray1))
        lightness.putpixel((x, y), (gray2, gray2, gray2))
        luminance.putpixel((x, y), (gray3, gray3, gray3))
        #print(average)
        #print(lightness)
        #print(luminance)

# Chuyển ảnh từ PIL sang OpenCV 
# Average, Lightness, Luminance là các giá trị tính toán cần phải chuyển sang ma trận
# cv2.imshow trả về dạng ma trận
anhmucxam1 = np.array(average)
#print(anhmucxam1)
anhmucxam2 = np.array(lightness)
#print(anhmucxam2)
anhmucxam3 = np.array(luminance)
#print(anhmucxam3)

# Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh Mau RGB - HoDangTu - 20146150', img) # dạng ma trận
cv2.imshow('Anh Muc Xam Average', anhmucxam1)
cv2.imshow('Anh Muc Xam Lightness', anhmucxam2)
cv2.imshow('Anh Muc Xam Luminance', anhmucxam3)

# Bấm phím bất kỳ để đóng cửa sổ hiển thị ảnh 
cv2.waitKey(0)

# Giải phóng bộ nhớ đã cấp phát cho các cửa sổ
cv2.destroyAllWindows()

