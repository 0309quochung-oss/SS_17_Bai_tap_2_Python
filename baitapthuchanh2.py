
import functools

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]


def hien_thi_tem_nhan():
    print("\n--- DANH SÁCH TEM NHÃN ---")

    for product in product_list:
        try:
            data = product.split("-")

            ma = data[0]
            ten = data[1]
            gia = int(data[2])
            rating = data[3]

            info = {
                "ma": f"{ma:<10}",
                "ten": ten,
                "gia": f"{gia:,}",
                "rating": rating
            }

            template = "Mã: {ma} | Tên: {ten:<20} | Giá: {gia} VND | Rating: {rating}*"

            print(template.format_map(info))

        except IndexError:
            print(f"Bỏ qua sản phẩm {data[0]} do sai cấu trúc dữ liệu")

        except ValueError:
            print(f"Bỏ qua sản phẩm {data[0]} do dữ liệu không hợp lệ")


def sap_xep():
    def key_sort(product):
        data = product.split("-")

        try:
            gia = int(data[2])
            rating = float(data[3])

            return (-rating, gia)

        except:
            return (9999, 999999999)

    product_list.sort(key=key_sort)

    print("\n--- SẮP XẾP SẢN PHẨM ---")

    for index, product in enumerate(product_list, start=1):
        print(f"{index}. {product}")


def tinh_tong():
    gia_list = []

    for product in product_list:

        try:
            data = product.split("-")

            if data[2].isdigit():
                gia_list.append(int(data[2]))

            else:
                print(f"Bỏ qua sản phẩm {data[0]} do giá không hợp lệ")

        except IndexError:
            print(f"Bỏ qua sản phẩm {data[0]} do sai cấu trúc dữ liệu")

    if len(gia_list) == 0:
        tong = 0
    else:
        tong = functools.reduce(lambda x, y: x + y, gia_list)

    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    print(f"Tổng giá trị các mặt hàng hiện tại là: {tong:,} VND.")


while True:

    menu = " E-COMMERCE ANALYTICS ".center(50, "=")

    choice = input(f"""
{menu}
1. Hiển thị tem nhãn sản phẩm
2. Sắp xếp sản phẩm thông minh
3. Tính tổng giá trị kho hàng
4. Đóng hệ thống
{"=" * 50}
Chọn chức năng (1-4):
""")

    match choice:

        case "1":
            hien_thi_tem_nhan()

        case "2":
            sap_xep()

        case "3":
            tinh_tong()

        case "4":
            print("Đóng hệ thống thành công.")
            break

        case _:
            print("Lựa chọn không hợp lệ.")

