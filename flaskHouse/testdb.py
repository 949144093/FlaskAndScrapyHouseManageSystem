from app import db,Users,HouseInfo,HouseCount

# # 会删除所有继承
db.drop_all()
db.create_all()

b1 =Users(username="admin",password="666",id=None)
b2 =Users(username="user",password="666",id=None)
b3 =Users(username="user2",password="666",id=None)

a1=HouseInfo(
    country="武汉",
    communityName="天成美雅",
    houseInfo="天成美雅-2室2厅-87.59平米",
    price="218.5",
    name="李先生",
    telenumber="13555555555",
    useraccount="user",
    id=None
)

a2=HouseInfo(
    country="武汉",
    communityName="旭辉御府",
    houseInfo="旭辉御府/2室1厅/77.19平米",
    price="147",
    name="李先生",
    telenumber="13999999999",
    useraccount="user",
    id=None
)



a3=HouseInfo(
    country="武汉",
    communityName="天祥尚府",
    houseInfo="天祥尚府-2室1厅-89.95平米",
    price="175",
    name="王先生",
    telenumber="13899999999",
    useraccount="user",
    id=None
)

a4=HouseInfo(
    country="武汉",
    communityName="宜家龙臣",
    houseInfo="宜家龙臣-2室1厅-91.94平米",
    price="98.5",
    name="王先生",
    telenumber="138988899",
    useraccount="user2",
    id=None
)


a8=HouseCount(country="武汉",countryhousecount="12")
a9=HouseCount(country="北京",countryhousecount="19")
a5=HouseCount(country="天津",countryhousecount="3")
a6=HouseCount(country="上海",countryhousecount="17")
a7=HouseCount(country="重庆",countryhousecount="28")

db.session.add(b1)
db.session.add(b2)
db.session.add(b3)
db.session.add(a1)
db.session.add(a2)
db.session.add(a3)
db.session.add(a4)
db.session.add(a5)
db.session.add(a6)
db.session.add(a7)
db.session.add(a8)
db.session.add(a9)

db.session.commit()