1. Cach xay dung folder code ------------------------------------------------------
- app: 
    + main.py => chay file chinh de tao app
    + DAO.py => ket noi voi data
    + controllers: viet functions tuong tac voi data
    + views: viet class tuong tac voi giao dien (login, home)
    + ui: chua file thiet o phan mem Qt designer
    + models: viet class (quy dinh thuoc tinh cua object)
    + assets: chua hinh anh, video, ... (nguyen lieu cho phan mem)
- data
    + data.json => chua du lieu cua app
    + data_example.json => du lieu goc (du lieu test)
- readme.txt

2. Quy dinh ve class (class diagram + data diagram) --------------------------------
- user: {
    username: khong cach khong dau,
    password: > 6 chu so,
    email: khong duoc trung, 
    avatar: link file hinh,
    rated_list: danh sach id cac film da danh gia, 
}
- film: {
    film_id: so thu tu film trong danh sach,
    name: ten film, 
    published_year: nam cong chieu film (so nguyen),
    rating: 1 => 5 (so nguyen),
    img: link file hinh,
    desc: mo ta chi tiet film,
    types: danh sach the loai + tag,
    actors: danh sach ten dien vien,
}

3. Rang buoc -------------------------------------
- User: 
    + khong duoc trung username
    + khong duoc trung email
    + id auto