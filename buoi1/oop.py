# class
class Xe:
    def __init__(self, price):
        self.price = price


# sub class
class XeHoi(Xe):
    def __init__(self, price, brandName):
        super().__init__(price)
        self.brandName = brandName


xeHoiA = XeHoi(price=123456789, brandName="Toyota")
# print(xeHoiA.price)


# ------------------------------
class HinhChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def chuVi(self):
        return (self.dai + self.rong) * 2
    
    def dienTich(self):
        return self.dai * self.rong

obj_hcn = HinhChuNhat(dai=3, rong=1)
print('Chu vi hinh chu nhat la',obj_hcn.chuVi())