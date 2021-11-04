from flask import Flask,render_template,request,redirect,session,url_for,flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from ch_login import is_user_login,is_admin_login
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key='mysecretkey'
db = SQLAlchemy(app)

# 定义一个用户及密码的数据库
class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(16))
#定义房源信息存储数据库
class HouseInfo(db.Model):
    __tablename__ = "houseinfo"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country = db.Column(db.String(10))
    communityName= db.Column(db.String(10))
    houseInfo= db.Column(db.String(50))
    price= db.Column(db.Float(10))
    name= db.Column(db.String(10))
    telenumber= db.Column(db.String(11))
    useraccount=db.Column(db.String(11))  #房源的拥有者用户名

    def to_dict(self):
        data = {
            'id':self.id,
            'country':self.country,
            'communityName':self.communityName,
            'houseInfo':self.houseInfo,
            'price':self.price,
            'name':self.name,
            'telenumber':self.telenumber,
            'useraccount':self.useraccount
        }
        return data
#定义各地区房源数量数据库
class HouseCount(db.Model):
    __tablename__ = "housecount"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country = db.Column(db.String(10))
    countryhousecount = db.Column(db.String(11))

"""用户注册方法"""
@app.route('/sign-up',methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template('sign-up.html')
    else:
        username = request.form.get('nick')
        pwd = request.form.get('pwd')
        pwd2 = request.form.get('pwd2')

        if not all([username,pwd,pwd2]):
            flash("信息输入不完整！")

        elif(pwd!=pwd2):
            flash('两次输入密码不一致！')
        else:
            new_user=Users(username=username,password=pwd,id=None)
            db.session.add(new_user)
            try:
                db.session.commit()
                flash('注册成功！')
            except:
                flash("用户名重复！注册失败！")
        return render_template('sign-up.html')

#定义主url跳转登录页面
@app.route('/')
def after_login():
    return redirect('/login')

#定义登录页面方法
@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template('login.html')
    else:
        user=request.form.get('username')
        pwd=request.form.get('pwd')
        if not all([user, pwd]):
            flash('信息输入不完整！')
        user=Users.query.filter(Users.username==user,Users.password==pwd).first()
        if user:
            session['user']=user.username
            if user.username=="admin":
                return redirect('/admin_index')
            else:
                return redirect('/user_index')
        else:
            flash("密码错误！")
        return render_template('login.html',error='用户名或者密码错误')


#定义登出方法
@app.route("/log_out",methods=["GET","POST"])
def logout():
    session.clear()
    return redirect('/login')

#管理员才可以访问
@app.route('/admin_index')
@is_admin_login
def index():
    return render_template('admin_index.html')

#任意用户均可访问
@app.route('/user_index',methods=["GET","POST"])
@is_user_login
def user_index():
    if request.method == "POST":
        user = session.get('user')
        country=request.form.get("country")
        communityName=request.form.get("communityName")
        houseInfo=request.form.get("houseInfo")
        price=request.form.get("price")
        name=request.form.get("name")
        telenumber=request.form.get("telenumber")
        if not all([country,communityName,houseInfo,price,name,telenumber]):
            flash("信息输入不完整！")
            return render_template('user_index.html')
        else:
            new_house=HouseInfo(
                        country=country,
                        communityName=communityName,
                        houseInfo=houseInfo,
                        price=price,
                        name=name,
                        telenumber=telenumber,
                        useraccount=user,
                        id=None
                    )
            db.session.add(new_house)
            db.session.commit()
            flash('发布成功！')
            return jsonify({'msg': "yes"})
    else:
        return render_template('user_index.html')


@app.route("/viewhouseinfo")
@is_user_login
def viewhouseinfo():
    return render_template('viewhouseinfo.html')

#查询当前登录用户的房源信息
@app.route('/houseinfoquery', methods=["GET"])
def houseinfoquery():
    houselist = []
    user = session.get('user')
    newHouse = HouseInfo.query.filter(HouseInfo.useraccount==user)
    for h in newHouse:
        houselist.append(h.to_dict())
    return jsonify({'houselist': houselist})

#修改用户房源信息
@app.route('/changehouseinfo/<changeid>',methods=["GET","POST"])
@is_user_login
def changehouseinfo(changeid):
    if request.method == "POST":
        id=changeid
        country = request.form.get("country")
        communityName = request.form.get("communityName")
        houseInfo = request.form.get("houseInfo")
        price = request.form.get("price")
        name = request.form.get("name")
        telenumber = request.form.get("telenumber")
        if not all([country, communityName, houseInfo, price, name, telenumber]):
            flash("信息输入不完整！")
            info = HouseInfo.query.filter(HouseInfo.id == changeid).first()
            dic = {}
            dic['country'] = info.country
            dic['communityName'] = info.communityName
            dic['houseInfo'] = info.houseInfo
            dic['price'] = info.price
            dic['name'] = info.name
            dic['telenumber'] = info.telenumber
            dic['id'] = changeid
            return render_template('changehouseinfo.html', dic=dic)
        else:
            newdic={"country":country, "communityName": communityName, "houseInfo":houseInfo,"price":price,"name":name,"telenumber":telenumber}
            HouseInfo.query.filter_by(id=id).update(newdic)
            db.session.commit()
            flash('修改成功！')
            return jsonify({'status': "yes"})
    else:
        # print(changeid)
        info=HouseInfo.query.filter(HouseInfo.id==changeid).first()
        dic={}
        dic['country']=info.country
        dic['communityName']=info.communityName
        dic['houseInfo']=info.houseInfo
        dic['price']=info.price
        dic['name']=info.name
        dic['telenumber']=info.telenumber
        dic['id']=changeid
        return render_template('changehouseinfo.html',dic=dic)

#删除房源信息
@app.route('/deletehouseinfo/<deleteid>',methods=["GET"])
@is_user_login
def deletehouseinfo(deleteid):
    houseID = deleteid
    info = HouseInfo.query.filter(HouseInfo.id == houseID).first()
    db.session.delete(info)
    db.session.commit()
    return redirect('/viewhouseinfo')

#关键字查询房源信息
@app.route('/quert_by_key_words',methods=["GET"])
@is_user_login
def query_by_keywords():
    return render_template('search.html')

#查询数据库各地区房源数量
@app.route('/get_housecount',methods=['GET', 'POST'])
def get_housecount():
    CountryHouses=HouseCount.query.all()
    outcome = {}
    for CH in CountryHouses:
        outcome[CH.country] = CH.countryhousecount
    return outcome
if __name__ == '__main__':
    app.run()
