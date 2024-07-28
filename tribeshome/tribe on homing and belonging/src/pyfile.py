import os
import pymysql
from flask import *
from werkzeug.utils import secure_filename

con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='tribe')
cmd=con.cursor()

pyfile=Flask(__name__)
pyfile.secret_key='abc'
path="static//upload"

@pyfile.route('/')
def home():
     return render_template('login.html')

@pyfile.route('/login',methods=['get','post'])
def login():
    USERNAME=request.form["textfield"]
    PASSWORD=request.form["textfield2"]
    cmd.execute("select * from tb_login_master where username='"+USERNAME+"' and password='"+PASSWORD+"'")
    s=cmd.fetchone()
    if s is None:

        return '''<script>alert("inavalid username or password");window.location='/'</script>'''

    elif s[3]=='admin':
        session['lid'] = s[0]
        return '''<script>alert("login successfully");window.location='/adminhome'</script>'''

    elif s[3]=='councillor':
        session['cid'] = s[0]
        return '''<script>alert("login successfully");window.location='/councilhome'</script>'''

    elif s[3]=='coordinator':
        session['crid'] = s[0]
        return '''<script>alert("login successfully");window.location='/coordhome'</script>'''

    # elif s[3]=='expertise':
    #     session['eid'] = s[0]
    #     return '''<script>alert("login successfully");window.location='/exphome'</script>'''

    elif s[3]=='shop':
        session['sid'] = s[0]
        return '''<script>alert("login successfully");window.location='/shophome'</script>'''

    # elif s[3]=='volunteer':
    #     session['vid'] = s[0]
    #     return '''<script>alert("login successfully");window.location='/volunteerhome'</script>'''
    elif s[3]=='district':
        session['districtid']=s[0]
        return '''<script>alert("login successfully");window.location='/district_home'</script>'''

    else:

        return '''<script>alert("Invalid Username or Password");window.location='/'</script>'''



@pyfile.route('/adminhome',methods=['get','post'])
def adminhome():
    return render_template('admin_temp2.html')

@pyfile.route('/coucilreg',methods=['get','post'])
def coucilreg():
    return render_template('addcouncil.html')

@pyfile.route('/creg',methods=['get','post'])
def creg():
    Firstname=request.form["textfield"]
    Lastname=request.form["textfield2"]
    DateOfBirth=request.form["textfield3"]
    Gender=request.form["radiobutton"]
    Place=request.form["textfield5"]
    PostOffice=request.form["textfield11"]
    Pin=request.form["textfield4"]
    PhoneNumber=request.form["textfield6"]
    Email=request.form["textfield7"]
    Qualifications=request.form.getlist('checkbox')
    Username=request.form["textfield9"]
    Password=request.form["textfield10"]
    cmd.execute("insert into tb_login_master values(null,'"+Username+"','"+Password+"','councillor')")
    lid=con.insert_id()
    cmd.execute("insert into tb_registration values(null,'"+str(lid)+"','"+Firstname+"','"+Lastname+"','"+DateOfBirth+"','"+Gender+"','"+Place+"','"+PostOffice+"','"+Pin+"','"+PhoneNumber+"','"+Email+"','"+str(','.join(Qualifications))+"','councillor','"+str(session['districtid'])+"')")
    con.commit()
    return '''<script>alert("successfully inserted");window.location="/viewcouncillor"</script>'''


@pyfile.route('/viewcouncillor',methods=['get','post'])
def viewcouncillor():
    cmd.execute("select * from tb_registration where type='councillor' and officer_id='"+str(session["districtid"])+"'")
    s = cmd.fetchall()
    return render_template('viewcouncil.html',val=s)

@pyfile.route('/editcouncillor',methods=['get','post'])
def editcouncillor():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_registration where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("editcouncil.html",val=s)

@pyfile.route('/updatecouncil',methods=['get','post'])
def updatecouncil():
    id=session['id']
    Firstname = request.form["textfield"]
    Lastname = request.form["textfield2"]
    DateOfBirth = request.form["textfield3"]
    Gender = request.form["radiobutton"]
    Place = request.form["textfield5"]
    PostOffice = request.form["textfield11"]
    Pin = request.form["textfield4"]
    PhoneNumber = request.form["textfield6"]
    Email = request.form["textfield7"]
    Qualifications = request.form.getlist('checkbox')
    cmd.execute("update tb_registration set fname='" + Firstname + "',lname='" + Lastname + "',dob='" + DateOfBirth + "',gender='" + Gender + "',place='" + Place + "',post='" + PostOffice + "',pin='" + Pin + "',contactno='" + PhoneNumber + "',email='" + Email + "',qualification='" + str(','.join(Qualifications)) + "',type='councillor' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("update successfully");window.location="/viewcouncillor"</script>'''

@pyfile.route('/delecouncillor',methods=['get','post'])
def delecouncillor():
    id=request.args.get('id')
    cmd.execute("delete from tb_registration where id='"+id+"'")
    con.commit()
    return viewcouncillor()
###################################################################################################################
@pyfile.route('/district_home')
def district_home():
    return render_template("district_home.html")

@pyfile.route('/District_off_reg',methods=['get','post'])
def District_off_reg():
    return render_template('add_district_officer.html')

@pyfile.route('/District_off_reg_post',methods=['get','post'])
def District_off_reg_post():
    Firstname=request.form["textfield"]
    Lastname=request.form["textfield2"]
    DateOfBirth=request.form["textfield3"]
    Gender=request.form["radiobutton"]
    Place=request.form["textfield5"]
    PostOffice=request.form["textfield11"]
    Pin=request.form["textfield4"]
    PhoneNumber=request.form["textfield6"]
    Email=request.form["textfield7"]
    Qualifications=request.form.getlist('checkbox')
    Username=request.form["textfield9"]
    Password=request.form["textfield10"]
    cmd.execute("insert into tb_login_master values(null,'"+Username+"','"+Password+"','district')")
    lid=con.insert_id()
    cmd.execute("insert into tb_registration values(null,'"+str(lid)+"','"+Firstname+"','"+Lastname+"','"+DateOfBirth+"','"+Gender+"','"+Place+"','"+PostOffice+"','"+Pin+"','"+PhoneNumber+"','"+Email+"','"+str(','.join(Qualifications))+"','district','0')")
    con.commit()
    return '''<script>alert("successfully inserted");window.location="/adminhome"</script>'''


@pyfile.route('/viewdistrict_officer',methods=['get','post'])
def viewdistrict_officer():
    cmd.execute("select * from tb_registration where type='district'")
    s = cmd.fetchall()
    return render_template('View_district_officer.html',val=s)

@pyfile.route('/editdistrict',methods=['get','post'])
def editdistrict():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_registration where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("edit_district_officer.html",val=s)

@pyfile.route('/update_district',methods=['get','post'])
def update_district():
    id=session['id']
    Firstname = request.form["textfield"]
    Lastname = request.form["textfield2"]
    DateOfBirth = request.form["textfield3"]
    Gender = request.form["radiobutton"]
    Place = request.form["textfield5"]
    PostOffice = request.form["textfield11"]
    Pin = request.form["textfield4"]
    PhoneNumber = request.form["textfield6"]
    Email = request.form["textfield7"]
    Qualifications = request.form.getlist('checkbox')
    qry="update tb_registration set fname='" + Firstname + "',lname='" + Lastname + "',dob='" + DateOfBirth + "',gender='" + Gender + "',place='" + Place + "',post='" + PostOffice + "',pin='" + Pin + "',contactno='" + PhoneNumber + "',email='" + Email + "',qualification='" + str(','.join(Qualifications)) + "' where id='"+str(id)+"'"
    print(qry)
    cmd.execute(qry)
    con.commit()
    return '''<script>alert("update successfully");window.location="/adminhome"</script>'''

@pyfile.route('/dele_district',methods=['get','post'])
def dele_district():
    id=request.args.get('id')
    cmd.execute("delete from tb_registration where id='"+id+"'")
    con.commit()
    return render_template("View_district_officer.html")

@pyfile.route('/district_view_packages',methods=['get'])
def district_view_packages():
    cmd.execute("select * from tb_package")
    s = cmd.fetchall()
    return render_template('district_view_packages.html',val=s)


@pyfile.route('/district_officer_view_report',methods=['get','post'])
def district_officer_view_report():
    cmd.execute("select lid,fname,lname from tb_registration where officer_id='"+str(session['districtid'])+"' and type='councillor'")
    s2 = cmd.fetchall()

    # cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_registration`.`type` ,`tb_report`.* FROM `tb_registration`INNER JOIN `tb_report` ON `tb_registration`.`lid`=`tb_report`.`lid` and `tb_registration`.`type`='coordinator' ")
    # s=cmd.fetchall()
    return render_template('district_view_report.html',val2=s2)


@pyfile.route('/district_officer_view_report_post', methods=['get', 'post'])
def district_officer_view_report_post():
    cmd.execute("select lid,fname,lname from tb_registration where officer_id='" + str(session['districtid']) + "' and type='councillor'")
    s2 = cmd.fetchall()

    councilorid=request.form["se"]
    print("cccc",councilorid)

    cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_registration`.`type` ,`tb_report`.* FROM `tb_registration`INNER JOIN `tb_report` ON `tb_registration`.`lid`=`tb_report`.`lid` where `tb_report`.`lid`='"+councilorid+"' ")
    s=cmd.fetchall()
    return render_template('district_view_report.html', val=s, val2=s2)
###################################################################################################################

@pyfile.route('/addnotification',methods=['get','post'])
def addnotification():
    notification=request.form['textfield']
    cmd.execute("insert into tb_notification values(null,curdate(),'"+notification+"')")
    con.commit()
    return '''<script>alert(" add notification successfully");window.location="/adminhome"</script>'''

@pyfile.route('/addnotification2',methods=['get','post'])
def addnotification2():
    return render_template('addnoti.html')

@pyfile.route('/viewnotiadmin',methods=['get','post'])
def viewnotiadmin():
    cmd.execute("select * from tb_notification")
    s = cmd.fetchall()
    return render_template('viewnotiadmin.html',val=s)

@pyfile.route('/editnoti',methods=['get','post'])
def editnoti():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_notification where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("editnotification.html",val=s)

@pyfile.route('/updatenotification',methods=['get','post'])
def updatenotification():
    id=session['id']
    notification=request.form['textfield']
    cmd.execute("update tb_notification set date=curdate(),notification='"+notification+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("update notification successfully");window.location="/adminhome"</script>'''

@pyfile.route('/delenoti',methods=['get','post'])
def delenoti():
    id=request.args.get('id')
    cmd.execute("delete from tb_notification where id='"+id+"'")
    con.commit()
    return render_template("viewnotiadmin.html")

@pyfile.route('/addpackage',methods=['get','post'])
def addpackage():
    return render_template('addpackage.html')

@pyfile.route('/addpackage2',methods=['get','post'])
def addpackage2():
    packagename=request.form['textfield']
    description=request.form['textarea']
    cmd.execute("insert into tb_package values(null,'"+packagename+"','"+description+"')")
    con.commit()
    return '''<script>alert("package added successfully");window.location='/adminhome'</script>'''

@pyfile.route('/viewpackadmin',methods=['get','post'])
def viewpackadmin():
    cmd.execute("select * from tb_package")
    s = cmd.fetchall()
    return render_template('viewpackadmin.html',val=s)

@pyfile.route('/editpackage',methods=['get','post'])
def editpackage():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_package where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("editpackage.html",val=s)

@pyfile.route('/updatepackage',methods=['get','post'])
def updatepackage():
    id=session['id']
    packagename=request.form['textfield']
    description=request.form['textarea']
    cmd.execute("update tb_package set package_name='"+packagename+"',description='"+description+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("package update successfully");window.location='/adminhome'</script>'''

@pyfile.route('/delepackage',methods=['get','post'])
def delepackage():
    id=request.args.get('id')
    cmd.execute("delete from tb_package where id='"+id+"'")
    con.commit()
    return viewpackadmin()

@pyfile.route('/adddonationdt',methods=['get','post'])
def adddonationdt():
    return render_template('donationdthome.html')

@pyfile.route('/addclothdt',methods=['get','post'])
def addclothdt():
    return render_template('cloth.html')

@pyfile.route('/addclothdt2',methods=['get','post'])
def addclothdt2():
    gender=request.form["radiobutton"]
    age=request.form["textfield"]
    clothtype=request.form["textfield3"]
    Count=request.form["textfield2"]
    DonorName=request.form["textfield4"]
    PhoneNumber=request.form["textfield5"]
    Email=request.form["textfield6"]
    cmd.execute("insert into tb_cloth values(null,'"+gender+"','"+age+"','"+clothtype+"','"+Count+"','"+DonorName+"','"+PhoneNumber+"','"+Email+"')")
    con.commit()
    return '''<script>alert("add cloth details successfully");window.location="/adminhome"</script>'''

@pyfile.route('/addeducationdt',methods=['get','post'])
def addeducationdt():
    return render_template('education.html')

@pyfile.route('/addeducationdt2',methods=['get','post'])
def addeducationdt2():
    MaterialName=request.form["textfield"]
    Count=request.form["textfield2"]
    DonorName=request.form["textfield3"]
    PhoneNumber=request.form["textfield4"]
    Email=request.form["textfield5"]
    cmd.execute("insert into tb_education values(null,'"+MaterialName+"','"+Count+"','"+DonorName+"','"+PhoneNumber+"','"+Email+"')")
    con.commit()
    return '''<script>alert("add education material details successfully");window.location="/adminhome"</script>'''

@pyfile.route('/addfooddt',methods=['get','post'])
def addfooddt():
    return render_template('food.html')

@pyfile.route('/addfooddt2',methods=['get','post'])
def addfooddt2():
    ItemName=request.form["textfield"]
    Quantity=request.form["textfield2"]
    DonorName=request.form["textfield3"]
    PhoneNumber=request.form["textfield4"]
    Email=request.form["textfield5"]
    cmd.execute("insert into tb_food values(null,'"+ItemName+"','"+Quantity+"','"+DonorName+"','"+PhoneNumber+"','"+Email+"')")
    con.commit()
    return '''<script>alert("add food details successfully");window.location="/adminhome"</script>'''

@pyfile.route('/addmedicinedt',methods=['get','post'])
def addmedicinedt():
    return render_template('medicine.html')

@pyfile.route('/addmedicinedt2',methods=['get','post'])
def addmedicinedt2():
    Type=request.form["select"]
    MedicineName=request.form["textfield"]
    Dosage=request.form["textfield2"]
    Quantity=request.form["textfield3"]
    ExpiryDate =request.form["textfield4"]
    DonorName = request.form["textfield5"]
    PhoneNumber = request.form["textfield6"]
    Email = request.form["textfield7"]
    cmd.execute("insert into tb_medicine values(null,'"+Type+"','"+MedicineName+"','"+Dosage+"','"+Quantity+"','"+ExpiryDate +"','"+DonorName+"','"+PhoneNumber+"','"+Email+"')")
    con.commit()
    return '''<script>alert("add medicine details successfully");window.location="/adminhome"</script>'''

@pyfile.route('/editdonationdt',methods=['get','post'])
def editdonationdt():
    return render_template('editdonationdthome.html')

@pyfile.route('/viewclothdt',methods=['get','post'])
def viewclothdt():
    cmd.execute("select * from tb_cloth")
    s = cmd.fetchall()
    return render_template('viewcloth.html',val=s)

@pyfile.route('/editclothdt',methods=['get','post'])
def editclothdt():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_cloth where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("updatecloth.html",val=s)

@pyfile.route('/updateclothdt2',methods=['get','post'])
def updateclothdt2():
    id=session['id']
    gender=request.form["radiobutton"]
    age=request.form["textfield"]
    clothtype=request.form["textfield3"]
    Count=request.form["textfield2"]
    DonorName=request.form["textfield4"]
    PhoneNumber=request.form["textfield5"]
    Email=request.form["textfield6"]
    cmd.execute("update tb_cloth set gender='"+gender+"',age='"+age+"',cloth_type='"+clothtype+"',count='"+Count+"',donor_name='"+DonorName+"',phoneno='"+PhoneNumber+"',email='"+Email+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("update cloth details successfully");window.location="/adminhome"</script>'''

@pyfile.route('/delecloth',methods=['get','post'])
def delecloth():
    id=request.args.get('id')
    cmd.execute("delete from tb_cloth where id='"+id+"'")
    con.commit()
    return render_template("viewcloth.html")

@pyfile.route('/vieweducationdt',methods=['get','post'])
def vieweducationdt():
    cmd.execute("select * from tb_education")
    s = cmd.fetchall()
    return render_template('vieweducation.html',val=s)

@pyfile.route('/editeducation',methods=['get','post'])
def editeducation():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_education where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("updateeducation.html",val=s)

@pyfile.route('/updateeducationdt',methods=['get','post'])
def updateeducationdt():
    id=session['id']
    MaterialName=request.form["textfield"]
    Count=request.form["textfield2"]
    DonorName=request.form["textfield3"]
    PhoneNumber=request.form["textfield4"]
    Email=request.form["textfield5"]
    cmd.execute("update tb_education set material_name='"+MaterialName+"',count='"+Count+"',donor_name='"+DonorName+"',phoneno='"+PhoneNumber+"',email='"+Email+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("update education material details successfully");window.location="/adminhome"</script>'''

@pyfile.route('/deleeducation',methods=['get','post'])
def deleeducation():
    id=request.args.get('id')
    cmd.execute("delete from tb_education where id='"+id+"'")
    con.commit()
    return render_template("vieweducation.html")

@pyfile.route('/viewfooddt',methods=['get','post'])
def viewfooddtt():
    cmd.execute("select * from tb_food")
    s = cmd.fetchall()
    return render_template('viewfood.html',val=s)

@pyfile.route('/editfood',methods=['get','post'])
def editfood():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_food where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("updatefood.html",val=s)

@pyfile.route('/updatefooddt',methods=['get','post'])
def updatefooddt():
    id=session['id']
    ItemName=request.form["textfield"]
    Quantity=request.form["textfield2"]
    DonorName=request.form["textfield3"]
    PhoneNumber=request.form["textfield4"]
    Email=request.form["textfield5"]
    cmd.execute("update tb_food set item_name='"+ItemName+"',quantity='"+Quantity+"',donor_name='"+DonorName+"',phoneno='"+PhoneNumber+"',email='"+Email+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("update food details successfully");window.location="/adminhome"</script>'''

@pyfile.route('/delefood',methods=['get','post'])
def delefood():
    id=request.args.get('id')
    cmd.execute("delete from tb_food where id='"+id+"'")
    con.commit()
    return render_template("viewfood.html")

@pyfile.route('/viewmedicinedt',methods=['get','post'])
def viewmedicinedt():
    cmd.execute("select * from tb_medicine")
    s = cmd.fetchall()
    return render_template('viewmedicine.html',val=s)

@pyfile.route('/editmedicine',methods=['get','post'])
def editmedicine():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_medicine where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("updatemedicine.html",val=s)

@pyfile.route('/updatemedicine',methods=['get','post'])
def updatemedicine():
    id=session['id']
    Type=request.form["select"]
    MedicineName=request.form["textfield"]
    Dosage=request.form["textfield2"]
    Quantity=request.form["textfield3"]
    ExpiryDate =request.form["textfield4"]
    DonorName = request.form["textfield5"]
    PhoneNumber = request.form["textfield6"]
    Email = request.form["textfield7"]
    cmd.execute("update tb_medicine set type='"+Type+"',medicine_name='"+MedicineName+"',dosage='"+Dosage+"',quantity='"+Quantity+"',expiry_date='"+ExpiryDate +"',donor_name='"+DonorName+"',phoneno='"+PhoneNumber+"',email='"+Email+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("update medicine details successfully");window.location="/adminhome"</script>'''

@pyfile.route('/delemedicine',methods=['get','post'])
def delemedicine():
    id=request.args.get('id')
    cmd.execute("delete from tb_medicine where id='"+id+"'")
    con.commit()
    return render_template("viewmedicine.html")


@pyfile.route('/adddonationreport',methods=['get','post'])
def adddonationreport():
    return render_template('updonationreport.html')

@pyfile.route('/adddonationreport2',methods=['get','post'])
def adddonationreport2():
    type=request.form["select"]
    tribearea=request.form["textfield"]
    description=request.form["textarea"]
    report=request.files["file"]
    img=secure_filename(report.filename)
    report.save(os.path.join(path,img))
    cmd.execute("insert into tb_updonation values(null,'"+type+"','"+tribearea+"',curdate(),'"+description+"','"+img+"')")
    con.commit()
    return '''<script>alert('add report successfully');window.location="/adminhome"</script>'''

@pyfile.route('/viewdonationreport',methods=['get','post'])
def viewdonationreport():
    cmd.execute("select * from tb_updonation")
    s = cmd.fetchall()
    return render_template('viewdonationreport.html',val=s)

@pyfile.route('/editdonationreport',methods=['get','post'])
def editdonationreport():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_updonation where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("updatedonationreport.html",val=s)

@pyfile.route('/updatedonationreport',methods=['get','post'])
def updatedonationreport():
    id=session['id']
    type=request.form["select"]
    tribearea=request.form["textfield"]
    description=request.form["textarea"]
    cmd.execute("update tb_updonation set type='"+type+"',tribe_area='"+tribearea+"',date=curdate(),description='"+description+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update report successfully');window.location="/adminhome"</script>'''

@pyfile.route('/changereport',methods=['get','post'])
def changereport():
    return render_template("changereport.html")

@pyfile.route('/updtreport',methods=['get','post'])
def updtreport():
    rprt=request.files['file']
    img = secure_filename(rprt.filename)
    rprt.save(os.path.join(path, img))
    cmd.execute("update tb_updonation set report='"+img+"' where id='"+str(session['id'])+"'")
    con.commit()
    return '''<script>alert('update report successfully');window.location="/viewdonationreport"</script>'''

@pyfile.route('/deledonationreport',methods=['get','post'])
def deledonationreport():
    id=request.args.get('id')
    cmd.execute("delete from tb_updonation where id='"+id+"'")
    con.commit()
    return render_template("viewdonationreport.html")


@pyfile.route('/viewreport',methods=['get','post'])
def viewreport():
    cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_registration`.`type` ,`tb_report`.* FROM `tb_registration`INNER JOIN `tb_report` ON `tb_registration`.`lid`=`tb_report`.`lid` and `tb_registration`.`type`='councillor' ")
    s=cmd.fetchall()
    return render_template('viewreportadmin.html',val=s)

@pyfile.route('/viewcomplaints',methods=['get','post'])
def viewcomplaints():
    cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_registration`.`type`,`tb_complaint`.* FROM `tb_registration` INNER JOIN `tb_complaint` ON `tb_complaint`.`lid`=`tb_registration`.`lid` and `tb_registration`.`type`='councillor'")
    s=cmd.fetchall()
    return render_template('mngecomplaint.html',val=s)

@pyfile.route('/reply',methods=['get','post'])
def reply():
    id = request.args.get('id')
    session['id'] = id
    return render_template("reply.html")

@pyfile.route('/sendreply',methods=['get','post'])
def sendreply():
    id=session['id']
    reply=request.form["textarea"]
    cmd.execute("update tb_complaint set reply='"+reply+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('send reply successfully');window.location="/adminhome"</script>'''

@pyfile.route('/viewchangepass',methods=['get','post'])
def viewchangepass():
      return render_template('change password.html')

@pyfile.route('/changepass',methods=['get','post'])
def changepass():
    currentpass=request.form["textfield"]
    newpass=request.form["textfield2"]
    confirmpass=request.form["textfield3"]
    cmd.execute("select * from tb_login_master where password='"+currentpass+"' and lid='"+str(session['lid'])+"'")
    s=cmd.fetchone()
    if s is not None:
        if newpass==confirmpass:
            cmd.execute("update tb_login_master set password='"+newpass+"' where lid='"+str(session['lid'])+"'")
            con.commit()
            return '''<script>alert('update successfully');window.location="/adminhome"</script>'''
        else:
            return '''<script>alert('invalid');window.location="/adminhome"</script>'''

    else:
        return '''<script>alert('password mismatch');window.location="/adminhome"</script>'''


@pyfile.route('/councilhome',methods=['get','post'])
def councilhome():
    return render_template('counciltemp2.html')

@pyfile.route('/managecoord',methods=['get','post'])
def managecoord():
    cmd.execute("select * from tb_registration where type='coordinator' and officer_id='"+str(session['cid'])+"'")
    s = cmd.fetchall()
    return render_template('viewcoordinator.html',val=s)

@pyfile.route('/addcord',methods=['get','post'])
def addcord():
      return render_template('addcoordinator.html')

@pyfile.route('/cordreg',methods=['get','post'])
def cordreg():
    Firstname=request.form["textfield"]
    Lastname=request.form["textfield2"]
    DateOfBirth=request.form["textfield3"]
    Gender=request.form["radiobutton"]
    Place=request.form["textfield5"]
    PostOffice=request.form["textfield11"]
    Pin=request.form["textfield4"]
    PhoneNumber=request.form["textfield6"]
    Email=request.form["textfield7"]
    Qualifications=request.form.getlist('checkbox')
    Username=request.form["textfield9"]
    Password=request.form["textfield10"]
    cmd.execute("insert into tb_login_master values(null,'"+Username+"','"+Password+"','coordinator')")
    lid=con.insert_id()
    cmd.execute("insert into tb_registration values(null,'"+str(lid)+"','"+Firstname+"','"+Lastname+"','"+DateOfBirth+"','"+Gender+"','"+Place+"','"+PostOffice+"','"+Pin+"','"+PhoneNumber+"','"+Email+"','"+str(','.join(Qualifications))+"','coordinator','"+str(session['cid'])+"')")
    con.commit()
    return '''<script>alert("successfully inserted");window.location="/councilhome"</script>'''

@pyfile.route('/editcoord',methods=['get','post'])
def editcoord():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_registration where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("editcord.html",val=s)

@pyfile.route('/updatecord',methods=['get','post'])
def updatecord():
    id=session['id']
    Firstname = request.form["textfield"]
    Lastname = request.form["textfield2"]
    DateOfBirth = request.form["textfield3"]
    Gender = request.form["radiobutton"]
    Place = request.form["textfield5"]
    PostOffice = request.form["textfield11"]
    Pin = request.form["textfield4"]
    PhoneNumber = request.form["textfield6"]
    Email = request.form["textfield7"]
    Qualifications = request.form.getlist('checkbox')
    cmd.execute("update tb_registration set fname='" + Firstname + "',lname='" + Lastname + "',dob='" + DateOfBirth + "',gender='" + Gender + "',place='" + Place + "',post='" + PostOffice + "',pin='" + Pin + "',contactno='" + PhoneNumber + "',email='" + Email + "',qualification='" + str(','.join(Qualifications)) + "',type='coordinator' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("update successfully");window.location="/councilhome"</script>'''

@pyfile.route('/delecord',methods=['get','post'])
def delecord():
    id=request.args.get('id')
    cmd.execute("delete from tb_registration where id='"+id+"'")
    con.commit()
    return render_template("viewcoordinator.html")

@pyfile.route('/addreportcoun1',methods=['get','post'])
def addreportcoun1():
    return render_template("addreportcouncil.html")

@pyfile.route('/addreportcoun2',methods=['get','post'])
def addreportcoun2():
    id=session['cid']
    tribearea=request.form["textfield"]
    title=request.form["textfield3"]
    report=request.files["file"]
    img=secure_filename(report.filename)
    report.save(os.path.join(path,img))
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='tribe')
    cmd = con.cursor()
    cmd.execute("insert into tb_report values(null,'"+str(id)+"',curdate(),'"+tribearea+"','"+title+"','"+img+"')")
    con.commit()
    return '''<script>alert('add report successfully');window.location="/councilhome"</script>'''

@pyfile.route('/viewreportcoun',methods=['get','post'])
def viewreportcoun():
    id=session['cid']
    print("select * from tb_report where lid='"+str(id)+"'")
    cmd.execute("select * from tb_report where lid='"+str(id)+"'")
    s = cmd.fetchall()
    return render_template('viewreportcouncil.html',val=s)

@pyfile.route('/editreportcoun',methods=['get','post'])
def editreportcoun():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_report where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("editreportcouncil.html",val=s)

@pyfile.route('/updatereportcoun',methods=['get','post'])
def updatereportcoun():
    id=session['id']
    tribearea=request.form["textfield"]
    title=request.form["textfield3"]
    cmd.execute("update tb_report set date=curdate(),tribe_area='"+tribearea+"',title='"+title+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update report successfully');window.location="/councilhome"</script>'''

@pyfile.route('/changereportcounc',methods=['get','post'])
def changereportcounc():
 return render_template("changereportcounc.html")

@pyfile.route('/upreportcoun',methods=['get','post'])
def upreportcoun():
    rprt=request.files['file']
    img = secure_filename(rprt.filename)
    rprt.save(os.path.join(path, img))
    cmd.execute("update tb_report set report='"+img+"' where id='"+str(session['id'])+"'")
    con.commit()
    return '''<script>alert('update report successfully');window.location="/viewreportcoun"</script>'''

@pyfile.route('/delereportcounc',methods=['get','post'])
def delereportcounc():
    id=request.args.get('id')
    cmd.execute("delete from tb_report where id='"+id+"'")
    con.commit()
    return viewreportcoun()

@pyfile.route('/addcompcounc',methods=['get','post'])
def addcompcounc():
    return render_template("addcomplaintcouncil.html")

@pyfile.route('/addcompcounc2',methods=['get','post'])
def addcompcounc2():
    id = session['cid']
    complaint=request.form["textfield"]
    cmd.execute("insert into tb_complaint values(null,'"+str(id)+"',curdate(),'"+complaint+"','pending')")
    con.commit()
    return '''<script>alert('add complaint successfully');window.location="/councilhome"</script>'''

@pyfile.route('/viewcomplaintcoun',methods=['get','post'])
def viewcomplaintcoun():
    id=session['cid']
    cmd.execute("select * from tb_complaint where lid='"+str(id)+"'")
    s = cmd.fetchall()
    return render_template('viewcomplaintcoun.html',val=s)

@pyfile.route('/editcomplaintcoun',methods=['get','post'])
def editcomplaintcoun():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_complaint where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("upcomplaintcouncil.html",val=s)

@pyfile.route('/updatecompcounc',methods=['get','post'])
def updatecompcounc():
    id = session['id']
    complaint=request.form["textfield"]
    cmd.execute("update tb_complaint set date=curdate(),complaint='"+complaint+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update complaint successfully');window.location="/councilhome"</script>'''

@pyfile.route('/delecompcounc',methods=['get','post'])
def delecompcounc():
    id=request.args.get('id')
    cmd.execute("delete from tb_complaint where id='"+id+"'")
    con.commit()
    return render_template("viewcomplaintcoun.html")

@pyfile.route('/viewservicereq',methods=['get','post'])
def viewservicereq():
    cmd.execute("select * from tb_servicereq where service='pending'")
    s = cmd.fetchall()
    return render_template('viewservicereq.html',val=s)

@pyfile.route('/allotservice',methods=['get','post'])
def allotservice():
    id=request.args.get('id')
    session['rid']=id
    return render_template('addservicescouncil.html')

@pyfile.route('/serviceupload',methods=['get','post'])
def serviceupload():
    id=session['rid']
    services = request.files['file']
    img = secure_filename(services.filename)
    services.save(os.path.join(path, img))
    cmd.execute("update tb_servicereq set service='" + img + "' where rid='" + str(id) + "'")
    con.commit()
    return '''<script>alert('add services successfully');window.location="/viewservicereq"</script>'''

@pyfile.route('/viewallotser',methods=['get','post'])
def viewallotser():
    cmd.execute("select * from tb_servicereq where service!='pending'")
    s = cmd.fetchall()
    return render_template('viewallotsercoun.html',val=s)

@pyfile.route('/editallotser',methods=['get','post'])
def editallotser():
    id=request.args.get('id')
    session['rid']=id
    print(id)
    cmd.execute("select service from tb_servicereq where rid='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("updateservicescouncil.html",val=s)

@pyfile.route('/updateallotser',methods=['get','post'])
def updateallotser():
    id = session['rid']
    services = request.files['file']
    img = secure_filename(services.filename)
    services.save(os.path.join(path, img))
    cmd.execute("update tb_servicereq set service='" + img + "' where rid='" + str(id) + "'")
    con.commit()
    return '''<script>alert('add services successfully');window.location="/viewallotser"</script>'''

@pyfile.route('/viewprofilecounc',methods=['get','post'])
def viewprofilecounc():
    id=session['cid']
    print(id)
    cmd.execute("select * from tb_registration where lid='" + str(id) + "'")
    s = cmd.fetchone()
    return render_template("viewprofilecouncil.html", val=s)

@pyfile.route('/viewreportcouncilor',methods=['get','post'])
def viewreportcouncilor():
    cmd.execute("select lid,fname,lname from tb_registration where officer_id='"+str(session['cid'])+"' and type='coordinator'")
    s2 = cmd.fetchall()
    print(s2,"===========================")
    # cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_registration`.`type` ,`tb_report`.* FROM `tb_registration`INNER JOIN `tb_report` ON `tb_registration`.`lid`=`tb_report`.`lid` and `tb_registration`.`type`='coordinator' ")
    # s=cmd.fetchall()
    return render_template('viewreport2councillor.html',val2=s2)
@pyfile.route('/viewreportcouncilor_post',methods=['get','post'])
def viewreportcouncilor_post():
    cordinatorid=request.form["se"]
    print("CCCCCCCCC",cordinatorid)
    cmd.execute("select lid,fname,lname from tb_registration where officer_id='" + str(session['cid']) + "' and type='coordinator'")
    s2 = cmd.fetchall()
    print(s2,"=======================")
    cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_registration`.`type` ,`tb_report`.* FROM `tb_registration`INNER JOIN `tb_report` ON `tb_registration`.`lid`=`tb_report`.`lid` where `tb_registration`.`type`='coordinator' and `tb_report`.`lid`='"+cordinatorid+"' ")
    s=cmd.fetchall()
    return render_template('viewreport2councillor.html',val2=s2,val=s)

@pyfile.route('/viewnoticoun',methods=['get','post'])
def viewnoticoun():
    cmd.execute("select * from tb_notification")
    s = cmd.fetchall()
    return render_template('viewnoticouncil.html',val=s)

@pyfile.route('/viewcomplaintcoun2',methods=['get','post'])
def viewcomplaintcoun2():
    cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_registration`.`type`,`tb_complaint`.* FROM `tb_registration` INNER JOIN `tb_complaint` ON `tb_complaint`.`lid`=`tb_registration`.`lid` and `tb_registration`.`type`='coordinator'")
    s=cmd.fetchall()
    return render_template('mngecomplaintcoun.html',val=s)

@pyfile.route('/usercomplaints',methods=['get','post'])
def usercomplaints():
    cmd.execute("SELECT `tb_publicreg`.`fname`,`lname`,`tb_complaint`.* FROM `tb_publicreg` INNER JOIN `tb_complaint` ON `tb_complaint`.`lid`=`tb_publicreg`.`id`")
    s=cmd.fetchall()
    return render_template('usercomplaints.html',val=s)



@pyfile.route('/replyuser',methods=['get','post'])
def replyuser():
    id = request.args.get('id')
    session['id'] = id
    return render_template("replyuser.html")

@pyfile.route('/replycoun',methods=['get','post'])
def replycoun():
    id = request.args.get('id')
    session['id'] = id
    return render_template("replycoun.html")

@pyfile.route('/sendreplycoun',methods=['get','post'])
def sendreplycoun():
    id=session['id']
    reply=request.form["textarea"]
    cmd.execute("update tb_complaint set reply='"+reply+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('send reply successfully');window.location="/councilhome"</script>'''

@pyfile.route('/viewpackcoun',methods=['get','post'])
def viewpackcoun():
    cmd.execute("select * from tb_package")
    s = cmd.fetchall()
    return render_template('viewpackagecoun.html',val=s)

@pyfile.route('/viewtribe',methods=['get','post'])
def viewtribe():
    cmd.execute("select * from tb_tribeinfo")
    s = cmd.fetchall()
    return render_template('viewtribe.html',val=s)

@pyfile.route('/viewfamilydt',methods=['get','post'])
def viewfamilydt():
    id = request.args.get('id')
    session['id'] = id
    cmd.execute("select * from tb_familydt where tid='"+str(id)+"'")
    s = cmd.fetchall()
    return render_template('familymembers.html',val=s)

@pyfile.route('/viewchangepasscoun',methods=['get','post'])
def viewchangepasscoun():
      return render_template('changepswdcoun.html')

@pyfile.route('/changepasscoun',methods=['get','post'])
def changepasscoun():
    currentpass=request.form["textfield"]
    newpass=request.form["textfield2"]
    confirmpass=request.form["textfield3"]
    cmd.execute("select * from tb_login_master where password='"+currentpass+"' and lid='"+str(session['cid'])+"'")
    s=cmd.fetchone()
    if s is not None:
        if newpass==confirmpass:
            cmd.execute("update tb_login_master set password='"+newpass+"' where lid='"+str(session['cid'])+"'")
            con.commit()
            return '''<script>alert('update successfully');window.location="/councilhome"</script>'''
        else:
            return '''<script>alert('invalid');window.location="/councilhome"</script>'''

    else:
        return '''<script>alert('password mismatch');window.location="/councilhome"</script>'''

@pyfile.route('/coordhome',methods=['get','post'])
def coordhome():
    return render_template('cordtemp2.html')

@pyfile.route('/managexpert',methods=['get','post'])
def managexpert():
    cmd.execute("select * from tb_registration where type='expertise'")
    s = cmd.fetchall()
    return render_template('viewexpert.html',val=s)

@pyfile.route('/addexpert',methods=['get','post'])
def addexpert():
      return render_template('addexpert.html')

@pyfile.route('/expertreg',methods=['get','post'])
def expertreg():
    Firstname=request.form["textfield"]
    Lastname=request.form["textfield2"]
    DateOfBirth=request.form["textfield3"]
    Gender=request.form["radiobutton"]
    Place=request.form["textfield5"]
    PostOffice=request.form["textfield11"]
    Pin=request.form["textfield4"]
    PhoneNumber=request.form["textfield6"]
    Email=request.form["textfield7"]
    Qualifications=request.form.getlist('checkbox')
    Username=request.form["textfield9"]
    Password=request.form["textfield10"]
    cmd.execute("insert into tb_login_master values(null,'"+Username+"','"+Password+"','expertise')")
    lid=con.insert_id()
    cmd.execute("insert into tb_registration values(null,'"+str(lid)+"','"+Firstname+"','"+Lastname+"','"+DateOfBirth+"','"+Gender+"','"+Place+"','"+PostOffice+"','"+Pin+"','"+PhoneNumber+"','"+Email+"','"+str(','.join(Qualifications))+"','expertise')")
    con.commit()
    return '''<script>alert("successfully inserted");window.location="/coordhome"</script>'''

@pyfile.route('/editexpert',methods=['get','post'])
def editexpert():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_registration where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("updateexpert.html",val=s)

@pyfile.route('/updateexpert',methods=['get','post'])
def updateexpert():
    id=session['id']
    Firstname = request.form["textfield"]
    Lastname = request.form["textfield2"]
    DateOfBirth = request.form["textfield3"]
    Gender = request.form["radiobutton"]
    Place = request.form["textfield5"]
    PostOffice = request.form["textfield11"]
    Pin = request.form["textfield4"]
    PhoneNumber = request.form["textfield6"]
    Email = request.form["textfield7"]
    Qualifications = request.form.getlist('checkbox')
    cmd.execute("update tb_registration set fname='" + Firstname + "',lname='" + Lastname + "',dob='" + DateOfBirth + "',gender='" + Gender + "',place='" + Place + "',post='" + PostOffice + "',pin='" + Pin + "',contactno='" + PhoneNumber + "',email='" + Email + "',qualification='" + str(','.join(Qualifications)) + "',type='expertise' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("update successfully");window.location="/coordhome"</script>'''

@pyfile.route('/deleexpert',methods=['get','post'])
def deleexpert():
    id=request.args.get('id')
    cmd.execute("delete from tb_registration where id='"+id+"'")
    con.commit()
    return render_template("viewexpert.html")

@pyfile.route('/addreportcord',methods=['get','post'])
def addreportcord():
    return render_template("addreportcord.html")

@pyfile.route('/addreportcord2',methods=['get','post'])
def addreportcord2():
    id=session['crid']
    tribearea=request.form["textfield"]
    title=request.form["textfield3"]
    report=request.files["file"]
    img=secure_filename(report.filename)
    report.save(os.path.join(path,img))
    cmd.execute("insert into tb_report values(null,'"+str(id)+"',curdate(),'"+tribearea+"','"+title+"','"+img+"')")
    con.commit()
    return '''<script>alert('add report successfully');window.location="/coordhome"</script>'''

@pyfile.route('/viewreportcoord',methods=['get','post'])
def viewreportcoord():
    id=session['crid']
    cmd.execute("select * from tb_report where lid='"+str(id)+"'")
    s = cmd.fetchall()
    return render_template('viewreportcord.html',val=s)

@pyfile.route('/editreportcord',methods=['get','post'])
def editreportcord():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_report where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("editreportcord.html",val=s)

@pyfile.route('/updatereportcord',methods=['get','post'])
def updatereportcord():
    id=session['id']
    tribearea=request.form["textfield"]
    title=request.form["textfield3"]
    cmd.execute("update tb_report set date=curdate(),tribe_area='"+tribearea+"',title='"+title+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update report successfully');window.location="/coordhome"</script>'''

@pyfile.route('/changereportcord',methods=['get','post'])
def changereportcord():
 return render_template("changereportcord.html")

@pyfile.route('/upreportcord',methods=['get','post'])
def upreportcord():
    rprt=request.files['file']
    img = secure_filename(rprt.filename)
    rprt.save(os.path.join(path, img))
    cmd.execute("update tb_report set report='"+img+"' where id='"+str(session['id'])+"'")
    con.commit()
    return '''<script>alert('update report successfully');window.location="/viewreportcoord"</script>'''

@pyfile.route('/delereportcord',methods=['get','post'])
def delereportcord():
    id=request.args.get('id')
    cmd.execute("delete from tb_report where id='"+id+"'")
    con.commit()
    return render_template("viewreportcord.html")

@pyfile.route('/addservicereq',methods=['get','post'])
def addservicereq():
    return render_template("addservicereqcord.html")

@pyfile.route('/addservicereq2',methods=['get','post'])
def addservicereq2():
    id=session['crid']
    tribearea=request.form["textfield"]
    title = request.form["textfield2"]
    req=request.files["file"]
    img=secure_filename(req.filename)
    req.save(os.path.join(path,img))
    cmd.execute("insert into tb_servicereq values(null,'"+str(id)+"',curdate(),'"+tribearea+"','"+title+"','"+img+"','pending')")
    con.commit()
    return '''<script>alert('add request successfully');window.location="/coordhome"</script>'''

@pyfile.route('/viewsercoord',methods=['get','post'])
def viewsercoord():
    cmd.execute("select * from tb_servicereq where  lid='"+str(session['crid'])+"'")
    s = cmd.fetchall()
    return render_template('viewservicecord.html',val=s)

@pyfile.route('/editsercord',methods=['get','post'])
def editsercord():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_servicereq where rid='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("editsercord.html",val=s)

@pyfile.route('/updatesercord',methods=['get','post'])
def updatesercord():
    id=session['id']
    tribearea=request.form["textfield"]
    title=request.form["textfield3"]
    cmd.execute("update tb_servicereq  set date=curdate(),tribearea='"+tribearea+"',title='"+title+"' where rid='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update request successfully');window.location="/coordhome"</script>'''

@pyfile.route('/changereqcord',methods=['get','post'])
def changereqcord():
 return render_template("changereqcord.html")

@pyfile.route('/upreqcord',methods=['get','post'])
def upreqcord():
    req=request.files['file']
    img = secure_filename(req.filename)
    req.save(os.path.join(path, img))
    cmd.execute("update tb_servicereq  set request='"+img+"' where rid='"+str(session['id'])+"'")
    con.commit()
    return '''<script>alert('update request successfully');window.location="/viewsercoord"</script>'''

@pyfile.route('/delereqcord',methods=['get','post'])
def delereqcord():
    id=request.args.get('id')
    cmd.execute("delete from tb_servicereq where rid='"+id+"'")
    con.commit()
    return render_template("'viewservicecord.html")

@pyfile.route('/addcompcord',methods=['get','post'])
def addcompcord():
    return render_template("addcomplaintcord.html")

@pyfile.route('/addcompcord2',methods=['get','post'])
def addcompcord2():
    id = session['crid']
    complaint=request.form["textfield"]
    cmd.execute("insert into tb_complaint values(null,'"+str(id)+"',curdate(),'"+complaint+"','pending')")
    con.commit()
    return '''<script>alert('add complaint successfully');window.location="/coordhome"</script>'''

@pyfile.route('/viewcomplaintcord',methods=['get','post'])
def viewcomplaintcord():
    id=session['crid']
    cmd.execute("select * from tb_complaint where lid='"+str(id)+"'and reply!='pending'")
    s = cmd.fetchall()
    return render_template('viewcomplaintcord.html',val=s)

@pyfile.route('/viewcomplaintdis',methods=['get','post'])
def viewcomplaintdis():
    id=session['districtid']
    print(id)
    cmd.execute("select * from tb_complaint where lid='"+str(id)+"'and reply!='pending'")
    s = cmd.fetchall()
    return render_template('viewcomplaintdist.html',val=s)
# @pyfile.route('/notif',methods=['get','post'])
# def notif():
#     return render_template('sndnotif.html')
# @pyfile.route('/sndnotif',methods=['get','post'])
# def sndnotif():
#     id=session['districtid']
#     print(id)
#     notif=request.form['file']
#     fn=secure_filename(notif.filename)
#     notif.save(os.path.join(path,fn))
#     cmd.execute("insert into tb_notifications values(null,'"+str(id)+"','"+fn+"',curdate())")
#     con.commit()
#     return '''<script>alert('send successfully');window.location="/"</script>'''
@pyfile.route('/editcomplaintcord',methods=['get','post'])
def editcomplaintcord():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_complaint where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("upcomplaintcord.html",val=s)

@pyfile.route('/updatecompcord',methods=['get','post'])
def updatecompcord():
    id = session['id']
    complaint=request.form["textfield"]
    cmd.execute("update tb_complaint set date=curdate(),complaint='"+complaint+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update complaint successfully');window.location="/coordhome"</script>'''

@pyfile.route('/delecompcord',methods=['get','post'])
def delecompcord():
    id=request.args.get('id')
    cmd.execute("delete from tb_complaint where id='"+id+"'")
    con.commit()
    return render_template("viewcomplaintcord.html")

@pyfile.route('/addprgmcord',methods=['get','post'])
def addprgmcord():
    return render_template("addprgmcord.html")

@pyfile.route('/addprgmcord2',methods=['get','post'])
def addprgmcord2():
    id=session['crid']
    prgmnm=request.form["textfield"]
    details=request.form["textfield2"]
    photo=request.files["file"]
    img=secure_filename(photo.filename)
    photo.save(os.path.join(path,img))
    cmd.execute("insert into tb_event values(null,'"+str(id)+"',curdate(),'"+prgmnm+"','"+details+"','"+img+"')")
    con.commit()
    return '''<script>alert('add events successfully');window.location="/coordhome"</script>'''

@pyfile.route('/vieweventcoord',methods=['get','post'])
def vieweventcoord():
    cmd.execute("select * from tb_event")
    s = cmd.fetchall()
    return render_template('vieweventcord.html',val=s)

@pyfile.route('/deleteeventcord',methods=['get','post'])
def deleteeventcord():
    id=request.args.get('id')
    cmd.execute("delete from tb_event where id='"+id+"'")
    con.commit()
    return render_template("coordinatorhome.html")

@pyfile.route('/addtribecord',methods=['get','post'])
def addtribecord():
    return render_template("addtribecord.html")

@pyfile.route('/addtribecord2',methods=['get','post'])
def addtribecord2():
    id = session['crid']
    TribeArea=request.form["textfield"]
    Name=request.form["textfield2"]
    Age=request.form["textfield3"]
    Gender=request.form["radiobutton"]
    Position=request.form["textfield4"]
    cmd.execute("insert into tb_tribeinfo values(null,'"+str(id)+"','"+TribeArea+"','"+Name+"','"+Age+"','"+Gender+"','"+Position+"')")
    tid=con.insert_id()
    session['tid']=tid
    con.commit()
    return redirect("next")

@pyfile.route('/addfamilycord2',methods=['get','post'])
def addfamilycord2():
    btn=request.form['Submit']
    if btn=='ADD':
        id=session['tid']
        MemberName=request.form["textfield"]
        Gender = request.form["radiobutton"]
        Age=request.form["textfield2"]
        Relation = request.form["textfield3"]
        Position=request.form["textfield4"]
        cmd.execute("insert into tb_familydt values(null,'"+str(id)+"','"+MemberName+"','"+Gender+"','"+Age+"','"+Relation+"','"+Position+"')")
        con.commit()
        return '''<script>alert('add family details');window.location="/next"</script>'''
    else:
        return '''<script>alert('add family details');window.location="/finish"</script>'''

@pyfile.route('/next')
def next():
    return render_template('addfamilycord.html')

@pyfile.route('/finish')
def finish():
    return render_template('coordinatorhome.html')

@pyfile.route('/viewtrbeinfocord',methods=['get','post'])
def viewtrbeinfocord():
    cmd.execute("select * from tb_tribeinfo")
    s=cmd.fetchall()
    return render_template("viewtribeinfocord.html",val=s)

@pyfile.route('/edittribecord',methods=['get','post'])
def edittribecord():
    id=request.args.get('id')
    session['tid']=id
    print(id)
    cmd.execute("select * from tb_tribeinfo where tid='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("updatetribecord.html",val=s)

@pyfile.route('/updatetribecord',methods=['get','post'])
def updatetribecord():
    id = session['tid']
    TribeArea=request.form["textfield"]
    Name=request.form["textfield2"]
    Age=request.form["textfield3"]
    Gender=request.form["radiobutton"]
    Position=request.form["textfield4"]
    cmd.execute("update tb_tribeinfo set tribe_area='"+TribeArea+"',name='"+Name+"',age='"+Age+"',gender='"+Gender+"',position='"+Position+"' where tid='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update tribeinfo successfully');window.location="/viewfamilydetails"</script>'''

@pyfile.route('/viewfamilydetails',methods=['get','post'])
def viewfamilydetails():
    id=session['tid']
    cmd.execute("select * from tb_familydt where tid='"+str(id)+"'")
    s = cmd.fetchall()
    return render_template("viewfamilydetails.html",val=s)

@pyfile.route('/editfamilydt',methods=['get','post'])
def editfamilydt():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_familydt where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("updatefamilydt.html",val=s)


@pyfile.route('/updatefamilydt',methods=['get','post'])
def updatefamilydt():
    id = session['id']
    MemberName = request.form["textfield"]
    Gender = request.form["radiobutton"]
    Age = request.form["textfield2"]
    Relation = request.form["textfield3"]
    Position = request.form["textfield4"]
    cmd.execute("update tb_familydt set member_name='" + MemberName + "',gender='" + Gender + "',age='" + Age + "',relation_with_head='" + Relation + "',position='" + Position + "' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update member details');window.location="/viewfamilydetails"</script>'''

@pyfile.route('/deletribeinfo',methods=['get','post'])
def deletribeinfo():
    id=request.args.get('id')
    cmd.execute("delete from tb_tribeinfo where tid='"+id+"'")
    cmd.execute("delete from tb_familydt where tid='" + id + "'")
    con.commit()
    return render_template("coordinatorhome.html")

@pyfile.route('/addworkcord',methods=['get','post'])
def addworkcord():
    cmd.execute("select * from tb_registration where type='volunteer'")
    s = cmd.fetchall()
    return render_template('addworkcord.html', val=s)


@pyfile.route('/addworkcord2',methods=['get','post'])
def addworkcord2():
    crid=session['crid']
    Volunteer=request.form["select"]
    TribeArea=request.form["textfield"]
    WorkDetails=request.form["textarea"]
    cmd.execute("insert into tb_work values(null,'"+Volunteer+"','"+str(crid)+"',curdate(),'"+TribeArea+"','"+WorkDetails+"')")
    con.commit()
    return '''<script>alert('add work successfully');window.location="/addworkcord"</script>'''

@pyfile.route('/viewworkcord',methods=['get','post'])
def viewworkcord():
    cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_work`.* FROM `tb_registration`INNER JOIN `tb_work` ON `tb_registration`.`lid`=`tb_work`.`vid`")
    s = cmd.fetchall()
    return render_template('viewworkcord.html',val=s)

@pyfile.route('/editworkcord',methods=['get','post'])
def editworkcord():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_work`.* FROM `tb_registration`INNER JOIN `tb_work` ON `tb_registration`.`lid`=`tb_work`.`vid`")
    s=cmd.fetchone()
    return render_template("updateworkcord.html",val=s)

@pyfile.route('/updateworkcord',methods=['get','post'])
def updateworkcord():
    id = session['id']
    TribeArea=request.form["textfield"]
    WorkDetails=request.form["textarea"]
    cmd.execute("update tb_work set date=curdate(),tribearea='"+TribeArea+"',work_details='"+WorkDetails+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update work successfully');window.location="/viewworkcord"</script>'''
@pyfile.route('/packstat',methods=['get','post'])
def packstat():
    id = session['vid']
    pid=request.args.get('id')
    cmd.execute("insert into packagestatus values(null,'"+str(pid)+"','"+str(id)+"','pending')")
    con.commit()
    return '''<script>alert('forwarded');window.location="/viewpackvol"</script>'''
@pyfile.route('/statcord',methods=['get','post'])
def statcord():
    pid=request.args.get('id')
    cmd.execute("update packagestatus set status='received' where pkgid='"+str(pid)+"' ")
    con.commit()
    return '''<script>alert('forwarded');window.location="/viewpackcord"</script>'''
@pyfile.route('/stat',methods=['get','post'])
def stat():
    cmd.execute("SELECT `tb_package`.* FROM `tb_package` JOIN `packagestatus` ON `packagestatus`.`pkgid`=`tb_package`.`id` WHERE `packagestatus`.status!='pending'")
    s = cmd.fetchall()
    return render_template('viewpackadm.html',val=s)
@pyfile.route('/statdist',methods=['get','post'])
def statdist():
    pid=request.args.get('id')
    cmd.execute("update packagestatus set status='forwarded' where pkgid='"+str(pid)+"' ")
    con.commit()
    return '''<script>alert('forwarded');window.location="/viewpackdis"</script>'''
@pyfile.route('/deleworkcord',methods=['get','post'])
def deleworkcord():
    id=request.args.get('id')
    cmd.execute("delete from tb_work where id='"+id+"'")
    con.commit()
    return render_template("coordinatorhome.html")

@pyfile.route('/viewprofilecord',methods=['get','post'])
def viewprofilecord():
    id=session['crid']
    print(id)
    cmd.execute("select * from tb_registration where lid='" + str(id) + "'")
    s = cmd.fetchone()
    return render_template("viewprofilecord.html", val=s)

@pyfile.route('/viewtribedtcord',methods=['get','post'])
def viewtribedtcord():
    id=session['crid']
    cmd.execute("select * from tb_tribeinfo where crid='"+str(id)+"'")
    s = cmd.fetchall()
    return render_template("viewtribecord.html", val=s)

@pyfile.route('/viewfamilydtcord',methods=['get','post'])
def viewfamilydtcord():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_familydt where tid='"+str(id)+"'")
    s=cmd.fetchall()
    return render_template("viewfamilydtcord.html",val=s)

@pyfile.route('/viewpackcord',methods=['get','post'])
def viewpackcord():
    cmd.execute("SELECT `tb_package`.* FROM `tb_package` JOIN `packagestatus` ON `packagestatus`.`pkgid`=`tb_package`.`id` WHERE `packagestatus`.status='pending'")
    s = cmd.fetchall()
    return render_template('viewpackagecord.html',val=s)


@pyfile.route('/viewpackdis',methods=['get','post'])
def viewpackdis():
    id=session['districtid']
    cmd.execute("SELECT `tb_package`.* FROM `tb_package` JOIN `tb_packagealllot` ON `tb_package`.id=`tb_packagealllot`.pid WHERE `tb_packagealllot`.disid='"+str(id)+"'")
    s = cmd.fetchall()
    return render_template('viewpackagedist.html',val=s)

@pyfile.route('/viewpackvol',methods=['get','post'])
def viewpackvol():
    cmd.execute("SELECT * FROM tb_package WHERE  id NOT IN (SELECT  pkgid FROM `packagestatus`) ")
    s = cmd.fetchall()
    return render_template('viewpackagevol.html',val=s)

@pyfile.route('/viewreportcordinator',methods=['get','post'])
def viewreportcordinator():
    cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_registration`.`type` ,`tb_report`.* FROM `tb_registration`INNER JOIN `tb_report` ON `tb_registration`.`lid`=`tb_report`.`lid` and `tb_registration`.`type`='volunteer' and `tb_registration`.`officer_id`='"+str(session['crid'])+"'")
    s = cmd.fetchall()
    return render_template('viewreport2cord.html', val=s)

# @pyfile.route('/viewreportcordi2',methods=['get','post'])
# def viewreportcordi2():
#     type = request.form['select']
#     cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_registration`.`type` ,`tb_report`.* FROM `tb_registration`INNER JOIN `tb_report` ON `tb_registration`.`lid`=`tb_report`.`lid` and `tb_registration`.`type`='volunteer' and `tb_registration`.`officer_id='"++"'`")
#     s = cmd.fetchall()
#     return render_template('viewreport2cord.html', val=s)

@pyfile.route('/viewcompcordinator',methods=['get','post'])
def viewcompcordinator():
    cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_registration`.`type`,`tb_complaint`.* FROM `tb_registration` INNER JOIN `tb_complaint` ON `tb_complaint`.`lid`=`tb_registration`.`lid` and `tb_registration`.`type`='volunteer' and `tb_registration`.`officer_id`='"+str(session['crid'])+"' ")
    s = cmd.fetchall()
    return render_template('mngecomplaintcord.html', val=s)

# @pyfile.route('/viewcomplaintcord2',methods=['get','post'])
# def viewcomplaintcord2():
#     type = request.form['select']
#     cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_registration`.`type`,`tb_complaint`.* FROM `tb_registration` INNER JOIN `tb_complaint` ON `tb_complaint`.`lid`=`tb_registration`.`lid` and `tb_registration`.`type`='"+str(type)+"'")
#     s=cmd.fetchall()
#     return render_template('mngecomplaintcord.html',val=s)

@pyfile.route('/replycord',methods=['get','post'])
def replycord():
    id = request.args.get('id')
    session['id'] = id
    return render_template("replycord.html")





@pyfile.route('/sendreplycord',methods=['get','post'])
def sendreplycord():
    id=session['id']
    reply=request.form["textarea"]
    cmd.execute("update tb_complaint set reply='"+reply+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('send reply successfully');window.location="/coordhome"</script>'''

@pyfile.route('/sendreplyuser',methods=['get','post'])
def sendreplyuser():
    id=session['id']
    reply=request.form["textarea"]
    cmd.execute("update tb_complaint set reply='"+reply+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('send reply successfully');window.location="/adminhome"</script>'''

@pyfile.route('/viewnoticord',methods=['get','post'])
def viewnoticord():
    cmd.execute("select * from tb_notification")
    s = cmd.fetchall()
    return render_template('viewnoticord.html',val=s)

@pyfile.route('/viewallotsercord',methods=['get','post'])
def viewallotsercord():
    cmd.execute("select * from tb_servicereq")
    s = cmd.fetchall()
    return render_template('viewallotsercord.html',val=s)

@pyfile.route('/approvevolunteer',methods=['get','post'])
def approvevolunteer():
    cmd.execute("SELECT `tb_registration`.* FROM `tb_registration` INNER JOIN `tb_login_master` ON `tb_login_master`.`lid`=`tb_registration`.`lid` AND `tb_login_master`.`type`='pending' and tb_registration.type='volunteer'")
    s = cmd.fetchall()
    return render_template('viewregvolun.html',val=s)

@pyfile.route('/acceptvolun',methods=['get','post'])
def acceptvolun():
    id =request.args.get('id')
    print(id)
    cmd.execute("update tb_login_master set type='volunteer'  where lid='" + str(id) + "'")
    con.commit()

    cmd.execute("update tb_registration set officer_id='"+ str(session['crid'])+"'  where lid='" + str(id) + "'")
    con.commit()
    return '''<script>alert('accept volunteer');window.location="/approvevolunteer"</script>'''

@pyfile.route('/rejectvolun',methods=['get','post'])
def rejectvolun():
    id =request.args.get('id')
    print(id)
    cmd.execute("delete from tb_login_master where lid='" + str(id) + "'")
    cmd.execute("delete from tb_registration where lid='" + str(id) + "'")
    con.commit()
    return '''<script>alert('deleted successfully');window.location="/approvevolunteer"</script>'''


@pyfile.route('/viewchangepasscord',methods=['get','post'])
def viewchangepasscord():
      return render_template('changepswdcord.html')

@pyfile.route('/changepasscord',methods=['get','post'])
def changepasscord():
    currentpass=request.form["textfield"]
    newpass=request.form["textfield2"]
    confirmpass=request.form["textfield3"]
    cmd.execute("select * from tb_login_master where password='"+currentpass+"' and lid='"+str(session['crid'])+"'")
    s=cmd.fetchone()
    if s is not None:
        if newpass==confirmpass:
            cmd.execute("update tb_login_master set password='"+newpass+"' where lid='"+str(session['crid'])+"'")
            con.commit()
            return '''<script>alert('update successfully');window.location="/coordhome"</script>'''
        else:
            return '''<script>alert('invalid');window.location="/coordhome"</script>'''

    else:
        return '''<script>alert('password mismatch');window.location="/coordhome"</script>'''

@pyfile.route('/exphome',methods=['get','post'])
def exphome():
    return render_template("expertise_temp.html")
    # return render_template('exphome.html')


@pyfile.route('/addprgmexp',methods=['get','post'])
def addprgmexp():
    return render_template("addawareexp.html")

@pyfile.route('/addprgmexp2',methods=['get','post'])
def addprgmexp2():
    prgmnm=request.form["textfield"]
    details=request.form["textfield2"]
    photo=request.files["file"]
    img=secure_filename(photo.filename)
    photo.save(os.path.join(path,img))
    cmd.execute("insert into tb_awareness values(null,curdate(),'"+prgmnm+"','"+details+"','"+img+"')")
    con.commit()
    return '''<script>alert('add programs successfully');window.location="/addprgmexp"</script>'''

@pyfile.route('/viewprgmexp',methods=['get','post'])
def viewprgmexp():


    cmd.execute("select * from tb_awareness")
    s = cmd.fetchall()
    return render_template('viewawareexp.html',val=s)


@pyfile.route('/viewaware',methods=['get','post'])
def viewaware():
    cmd.execute("select * from tb_awareness")
    s = cmd.fetchall()
    return render_template('viewaware.html',val=s)

@pyfile.route('/deleteprgmexp',methods=['get','post'])
def deleteprgmexp():
    id=request.args.get('id')
    cmd.execute("delete from tb_awareness where id='"+id+"'")
    con.commit()
    return viewprgmexp()

@pyfile.route('/addreportexp',methods=['get','post'])
def addreportexp():
    return render_template("addreportexp.html")

@pyfile.route('/addreportexp2',methods=['get','post'])
def addreportexp2():
    id=session['eid']
    tribearea=request.form["textfield"]
    title=request.form["textfield3"]
    report=request.files["file"]
    img=secure_filename(report.filename)
    report.save(os.path.join(path,img))
    cmd.execute("insert into tb_report values(null,'"+str(id)+"',curdate(),'"+tribearea+"','"+title+"','"+img+"')")
    con.commit()
    return '''<script>alert('add report successfully');window.location="/exphome"</script>'''

@pyfile.route('/viewreportexp',methods=['get','post'])
def viewreportexp():
    id=session['eid']
    cmd.execute("select * from tb_report where lid='"+str(id)+"'")
    s = cmd.fetchall()
    return render_template('viewreportexp.html',val=s)

@pyfile.route('/editreportexp',methods=['get','post'])
def editreportexp():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_report where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("editreportexp.html",val=s)

@pyfile.route('/updatereportexp',methods=['get','post'])
def updatereportexp():
    id=session['id']
    tribearea=request.form["textfield"]
    title=request.form["textfield3"]
    cmd.execute("update tb_report set date=curdate(),tribe_area='"+tribearea+"',title='"+title+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update report successfully');window.location="/viewreportexp"</script>'''

@pyfile.route('/changereportexp',methods=['get','post'])
def changereportexp():
 return render_template("changereportexp.html")

@pyfile.route('/upreportexp',methods=['get','post'])
def upreportexp():
    rprt=request.files['file']
    img = secure_filename(rprt.filename)
    rprt.save(os.path.join(path, img))
    cmd.execute("update tb_report set report='"+img+"' where id='"+str(session['id'])+"'")
    con.commit()
    return '''<script>alert('update report successfully');window.location="/viewreportexp"</script>'''

@pyfile.route('/delereportexp',methods=['get','post'])
def delereportexp():
    id=request.args.get('id')
    cmd.execute("delete from tb_report where id='"+id+"'")
    con.commit()
    return render_template("exphome.html")

@pyfile.route('/addcompexp',methods=['get','post'])
def addcompexp():
    return render_template("addcomplaintexp.html")

@pyfile.route('/addcompexp2',methods=['get','post'])
def addcompexp2():
    id = session['eid']
    complaint=request.form["textfield"]
    cmd.execute("insert into tb_complaint values(null,'"+str(id)+"',curdate(),'"+complaint+"','pending')")
    con.commit()
    return '''<script>alert('add complaint successfully');window.location="/exphome"</script>'''

@pyfile.route('/viewcomplaintexp',methods=['get','post'])
def viewcomplaintexp():
    id=session['eid']
    cmd.execute("select * from tb_complaint where lid='"+str(id)+"' and reply='pending'")
    s = cmd.fetchall()
    return render_template('viewcomplaintexp.html',val=s)

@pyfile.route('/editcomplaintexp',methods=['get','post'])
def editcomplaintexp():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_complaint where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("upcomplaintexp.html",val=s)

@pyfile.route('/updatecompexp',methods=['get','post'])
def updatecompexp():
    id = session['id']
    complaint=request.form["textfield"]
    cmd.execute("update tb_complaint set date=curdate(),complaint='"+complaint+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update complaint successfully');window.location="/viewcomplaintexp"</script>'''

@pyfile.route('/delecompexp',methods=['get','post'])
def delecompexp():
    id=request.args.get('id')
    cmd.execute("delete from tb_complaint where id='"+id+"'")
    con.commit()
    return render_template("exphome.html")

@pyfile.route('/viewprofileexp',methods=['get','post'])
def viewprofileexp():
    id=session['eid']
    print(id)
    cmd.execute("select * from tb_registration where lid='" + str(id) + "'")
    s = cmd.fetchone()
    return render_template("viewprofileexp.html", val=s)

@pyfile.route('/viewproblem',methods=['get','post'])
def viewproblem():
    cmd.execute("select * from tb_tribeproblem")
    s = cmd.fetchall()
    return render_template('viewprblmexp.html',val=s)

@pyfile.route('/viewnotiexp',methods=['get','post'])
def viewnotiexp():
    cmd.execute("select * from tb_notification")
    s = cmd.fetchall()
    return render_template('viewnotiexp.html',val=s)

@pyfile.route('/viewchangepassexp',methods=['get','post'])
def viewchangepassexp():
      return render_template('changepswdexp.html')

@pyfile.route('/changepassexp',methods=['get','post'])
def changepassexp():
    currentpass=request.form["textfield"]
    newpass=request.form["textfield2"]
    confirmpass=request.form["textfield3"]
    cmd.execute("select * from tb_login_master where password='"+currentpass+"' and lid='"+str(session['eid'])+"'")
    s=cmd.fetchone()
    if s is not None:
        if newpass==confirmpass:
            cmd.execute("update tb_login_master set password='"+newpass+"' where lid='"+str(session['eid'])+"'")
            con.commit()
            return '''<script>alert('update successfully');window.location="/exphome"</script>'''
        else:
            return '''<script>alert('invalid');window.location="/exphome"</script>'''

    else:
        return '''<script>alert('password mismatch');window.location="/exphome"</script>'''


@pyfile.route('/shophome',methods=['get','post'])
def shophome():
    return render_template('shophome.html')

@pyfile.route('/addproduct',methods=['get','post'])
def addproduct():
    return render_template('addproduct.html')

@pyfile.route('/addproduct2',methods=['get','post'])
def addproduct2():
    id = session['sid']
    ProductName=request.form['textfield']
    Description=request.form['textarea']
    Quantity=request.form['textfield2']
    Price=request.form['textfield3']
    photo = request.files["file"]
    img = secure_filename(photo.filename)
    photo.save(os.path.join(path, img))
    cmd.execute("insert into tb_product values(null,'"+str(id)+"','"+ProductName+"','"+Description+"','"+Quantity+"','"+Price+"','"+img+"')")
    con.commit()
    return '''<script>alert(" add product successfully");window.location="/shophome"</script>'''

@pyfile.route('/viewproduct',methods=['get','post'])
def viewproduct():
    cmd.execute("select * from tb_product")
    s = cmd.fetchall()
    return render_template('viewproduct.html',val=s)

@pyfile.route('/editproduct',methods=['get','post'])
def editproduct():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_product where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("updateproduct.html",val=s)

@pyfile.route('/updateproduct',methods=['get','post'])
def updateproduct():
    id = session['id']
    ProductName=request.form['textfield']
    Description=request.form['textarea']
    Quantity=request.form['textfield2']
    Price=request.form['textfield3']
    cmd.execute("update tb_product set poduct_name='"+ProductName+"',description='"+Description+"',quantity='"+Quantity+"',price='"+Price+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert(" update product successfully");window.location="/viewproduct"</script>'''

@pyfile.route('/deleproduct',methods=['get','post'])
def deleproduct():
    id=request.args.get('id')
    cmd.execute("delete from tb_product where id='"+id+"'")
    con.commit()
    return redirect("viewproduct")

@pyfile.route('/viewstock',methods=['get','post'])
def viewstock():
    id=session['sid']
    cmd.execute("select * from tb_product where sid='"+str(id)+"'")
    s=cmd.fetchall()
    print(id)
    return render_template('stockupdation.html',val=s)

@pyfile.route('/stockup',methods=['get','post'])
def stockup():
    pid=request.form['pid']
    cmd.execute("SELECT `quantity` FROM `tb_product` WHERE `id`='"+str(pid)+"'")
    # print("select quantity from tb_product where sid='"+str(session['sid'])+"'")
    s=cmd.fetchone()
    print(s)

    resp = make_response(jsonify(str(s[0])))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@pyfile.route('/updatestock',methods=['get','post'])
def updatestock():
    stock=request.form['textfield']
    cmd.execute("update tb_product set quantity=quantity+"+stock+" where sid='"+str(session['sid'])+"'")
    con.commit()
    return '''<script>alert(" update stock successfully");window.location="/shophome"</script>'''

@pyfile.route('/viewpurchasepdt',methods=['get','post'])
def viewpurchasepdt():
    cmd.execute("select * from tb_bill")
    s = cmd.fetchall()
    return render_template('viewpurchasepdt.html',val=s)

@pyfile.route('/acceptpdt',methods=['get','post'])
def acceptpdt():
    id =request.args.get('id')
    print(id)
    cmd.execute("update tb_bill set type='payed' where bid='" + str(id) + "'")
    con.commit()
    return '''<script>alert('accept product');window.location="/approve"</script>'''

@pyfile.route('/rejectpdt',methods=['get','post'])
def rejectpdt():
    id =request.args.get('id')
    print(id)
    cmd.execute("delete from tb_bill where bid='" + str(id) + "'")
    cmd.execute("delete from tb_billproduct where bid='" + str(id) + "'")
    con.commit()
    return render_template('viewpurchasepdt.html')

@pyfile.route('/viewproductdt',methods=['get','post'])
def viewproductdt():
    id = request.args.get('id')
    cmd.execute("select * from tb_billproduct where tb_billproduct.bid='"+id+"'")
    s = cmd.fetchall()
    return render_template('productdt2.html',val=s)

@pyfile.route('/viewcomplaintshop',methods=['get','post'])
def viewcomplaintshop():
    cmd.execute("SELECT `tb_publicreg`.`fname`,`tb_publicreg`.`lname`,`tb_complaint`.* FROM `tb_publicreg` INNER JOIN `tb_complaint` ON `tb_complaint`.`lid`=`tb_publicreg`.`id` ")
    s=cmd.fetchall()
    return render_template('mngecomplaintshop.html',val=s)

@pyfile.route('/replyshop',methods=['get','post'])
def replyshop():
    id = request.args.get('id')
    session['id'] = id
    return render_template("replyshop.html")

@pyfile.route('/sendreplyshop',methods=['get','post'])
def sendreplyshop():
    id=session['id']
    reply=request.form["textarea"]
    cmd.execute("update tb_complaint set reply='"+reply+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('send reply successfully');window.location="/shophome"</script>'''




@pyfile.route('/viewnotishop',methods=['get','post'])
def viewnotishop():
    cmd.execute("select * from tb_notification")
    s = cmd.fetchall()
    return render_template('viewnotishop.html',val=s)

@pyfile.route('/viewchangepassshop',methods=['get','post'])
def viewchangepassshop():
      return render_template('changepswdshop.html')

@pyfile.route('/changepassshop',methods=['get','post'])
def changepassshop():
    currentpass=request.form["textfield"]
    newpass=request.form["textfield2"]
    confirmpass=request.form["textfield3"]
    cmd.execute("select * from tb_login_master where password='"+currentpass+"' and lid='"+str(session['sid'])+"'")
    s=cmd.fetchone()
    if s is not None:
        if newpass==confirmpass:
            cmd.execute("update tb_login_master set password='"+newpass+"' where lid='"+str(session['sid'])+"'")
            con.commit()
            return '''<script>alert('update successfully');window.location="/shophome"</script>'''
        else:
            return '''<script>alert('invalid');window.location="/shophome"</script>'''

    else:
        return '''<script>alert('password mismatch');window.location="/shophome"</script>'''


@pyfile.route('/voluntreg',methods=['get','post'])
def voluntreg():
    return render_template('volunteerreg.html')

@pyfile.route('/vreg',methods=['get','post'])
def vreg():
    Firstname=request.form["textfield"]
    Lastname=request.form["textfield2"]
    DateOfBirth=request.form["textfield3"]
    Gender=request.form["radiobutton"]
    Place=request.form["textfield5"]
    PostOffice=request.form["textfield11"]
    Pin=request.form["textfield4"]
    PhoneNumber=request.form["textfield6"]
    Email=request.form["textfield7"]
    Qualifications=request.form.getlist('checkbox')
    Username = request.form["textfield9"]
    Password = request.form["textfield10"]
    cmd.execute("insert into tb_login_master values(null,'" + Username + "','" + Password + "','pending')")
    lid = con.insert_id()
    cmd.execute("insert into tb_registration values(null,'"+str(lid)+"','"+Firstname+"','"+Lastname+"','"+DateOfBirth+"','"+Gender+"','"+Place+"','"+PostOffice+"','"+Pin+"','"+PhoneNumber+"','"+Email+"','"+str(','.join(Qualifications))+"','volunteer','0')")
    con.commit()
    return '''<script>alert("registered successfully");window.location="/"</script>'''

@pyfile.route('/volunteerhome',methods=['get','post'])
def volunteerhome():
    return render_template('volunteerhome.html')

@pyfile.route('/addreportvolun',methods=['get','post'])
def addreportvolun():
    return render_template("addreportvolun.html")

@pyfile.route('/addreportvolun2',methods=['get','post'])
def addreportvolun2():
    id=session['vid']
    tribearea=request.form["textfield"]
    title=request.form["textfield3"]
    report=request.files["file"]
    img=secure_filename(report.filename)
    report.save(os.path.join(path,img))
    cmd.execute("insert into tb_report values(null,'"+str(id)+"',curdate(),'"+tribearea+"','"+title+"','"+img+"')")
    con.commit()
    return '''<script>alert('add report successfully');window.location="/volunteerhome"</script>'''

@pyfile.route('/viewreportvolun',methods=['get','post'])
def viewreportvolun():
    id=session['vid']
    cmd.execute("select * from tb_report where lid='"+str(id)+"'")
    s = cmd.fetchall()
    return render_template('viewreportvolun.html',val=s)

@pyfile.route('/editreportvolun',methods=['get','post'])
def editreportvolun():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_report where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("editreportvolun.html",val=s)

@pyfile.route('/updatereportvolun',methods=['get','post'])
def updatereportvolun():
    id=session['id']
    tribearea=request.form["textfield"]
    title=request.form["textfield3"]
    cmd.execute("update tb_report set date=curdate(),tribe_area='"+tribearea+"',title='"+title+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update report successfully');window.location="/viewreportvolun"</script>'''

@pyfile.route('/changereportvolun',methods=['get','post'])
def changereportvolun():
    return render_template("changereportvolun.html")

@pyfile.route('/upreportvolun',methods=['get','post'])
def upreportvolun():
    rprt=request.files['file']
    img = secure_filename(rprt.filename)
    rprt.save(os.path.join(path, img))
    cmd.execute("update tb_report set report='"+img+"' where id='"+str(session['id'])+"'")
    con.commit()
    return '''<script>alert('update report successfully');window.location="/viewreportvolun"</script>'''

@pyfile.route('/delereportvolun',methods=['get','post'])
def delereportvolun():
    id=request.args.get('id')
    cmd.execute("delete from tb_report where id='"+id+"'")
    con.commit()
    return render_template("volunteerhome.html")

@pyfile.route('/addcompvolun',methods=['get','post'])
def addcompvolun():
    return render_template("addcomplaintvolun.html")

@pyfile.route('/addcompvolun2',methods=['get','post'])
def addcompvolun2():
    id = session['vid']
    complaint=request.form["textfield"]
    cmd.execute("insert into tb_complaint values(null,'"+str(id)+"',curdate(),'"+complaint+"','pending')")
    con.commit()
    return '''<script>alert('add complaint successfully');window.location="/volunteerhome"</script>'''

@pyfile.route('/viewcompvolun',methods=['get','post'])
def viewcompvolun():
    id=session['vid']
    e="select * from tb_complaint where lid='"+str(id)+"'"
    cmd.execute(e)
    print(e)
    s = cmd.fetchall()
    return render_template('viewcomplaintvolun.html',val=s)

@pyfile.route('/editcompvolun',methods=['get','post'])
def editcompvolun():
    id=request.args.get('id')
    session['id']=id
    print(id)
    cmd.execute("select * from tb_complaint where id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("upcomplaintvolun.html",val=s)

@pyfile.route('/updatecompvolun',methods=['get','post'])
def updatecompvolun():
    id = session['id']
    complaint=request.form["textfield"]
    cmd.execute("update tb_complaint set date=curdate(),complaint='"+complaint+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert('update complaint successfully');window.location="/viewcompvolun"</script>'''

@pyfile.route('/delecompvolun',methods=['get','post'])
def delecompvolun():
    id=request.args.get('id')
    cmd.execute("delete from tb_complaint where id='"+id+"'")
    con.commit()
    return render_template("volunteerhome.html")

@pyfile.route('/addproblmvolun1',methods=['get','post'])
def addproblmvolun1():
    return render_template('addprblm.html')

@pyfile.route('/addproblmvolun',methods=['get','post'])
def addproblmvolun():
    id = session['vid']
    TribeArea=request.form["textfield"]
    ProblemName=request.form["textfield2"]
    Description=request.form["textarea"]
    cmd.execute("insert into tb_tribeproblem values(null,'"+str(id)+"','"+TribeArea+"','"+ProblemName+"','"+Description+"')")
    con.commit()
    return '''<script>alert('add tribal problem successfully');window.location="/volunteerhome"</script>'''

@pyfile.route('/viewproblm',methods=['get','post'])
def viewproblm():
    id=session['vid']
    cmd.execute("select * from tb_tribeproblem where lid='"+str(id)+"'")
    s = cmd.fetchall()
    return render_template('viewprblmvolun.html',val=s)
@pyfile.route('/vwpblm',methods=['get','post'])
def vwpblm():
    cmd.execute("select * from tb_tribeproblem ")
    s = cmd.fetchall()
    return render_template('distviewprblmvolun.html',val=s)
@pyfile.route('/deleproblmvolun',methods=['get','post'])
def deleproblmvolun():
    id=request.args.get('id')
    cmd.execute("delete from tb_tribeproblem where id='"+id+"'")
    con.commit()
    return render_template("volunteerhome.html")

@pyfile.route('/viewprofilevolun',methods=['get','post'])
def viewprofilevolun():
    id=session['vid']
    print(id)
    cmd.execute("select * from tb_registration where lid='" + str(id) + "'")
    s = cmd.fetchone()
    return render_template("viewprofilevolun.html", val=s)



@pyfile.route('/viewnotivolun',methods=['get','post'])
def viewnotivolun():
    cmd.execute("select * from tb_notification")
    s = cmd.fetchall()
    return render_template('viewnotivolun.html',val=s)



@pyfile.route('/viewworkvolun',methods=['get','post'])
def viewworkvolun():
    id=session['vid']
    cmd.execute("SELECT `tb_registration`.`fname`,`tb_registration`.`lname`,`tb_work`.* FROM `tb_registration` INNER JOIN `tb_work` ON `tb_work`.`crid`=`tb_registration`.`lid` where vid='"+str(id)+"' ")
    s = cmd.fetchall()
    return render_template('viewworkvolun.html',val=s)

@pyfile.route('/shopreg',methods=['get','post'])
def shopreg():
      return render_template('shop_reg.html')



@pyfile.route('/shop_reg_post',methods=['get','post'])
def shop_reg_post():
    shopname=request.form["textfield"]
    place=request.form["textfield2"]
    post=request.form["textfield11"]
    pin=request.form["textfield4"]
    contact = request.form["textfield6"]
    liceneno=request.form["textfield7"]
    ownername=request.form["textfield9"]
    Username=request.form["textfield91"]
    Password=request.form["textfield10"]
    cmd.execute("insert into tb_login_master values(null,'"+Username+"','"+Password+"','pending')")
    lid=con.insert_id()
    cmd.execute("insert into tb_shopreg(shopname,place,post,pin,contactno,lid,licenceno,ownername,username) values('"+shopname+"','"+place+"','"+post+"','"+pin+"','"+contact+"','"+str(lid)+"','"+liceneno+"','"+ownername+"','"+Username+"')")
    con.commit()
    return '''<script>alert("successfully inserted");window.location="/"</script>'''

@pyfile.route('/admin_view_shop',methods=['get','post'])
def admin_view_shop():

    cmd.execute("select tb_shopreg.*,tb_login_master.type from tb_shopreg inner join tb_login_master on tb_login_master.lid=tb_shopreg.lid")
    s = cmd.fetchall()
    print(s)
    return render_template('admin_view_shop.html',val=s)


@pyfile.route('/approveshop',methods=['get','post'])
def approveshop():
    id=request.args.get('id')
    cmd.execute("update tb_login_master set type='shop' where lid='"+id+"'")
    con.commit()
    return admin_view_shop()


@pyfile.route('/rejectshop',methods=['get','post'])
def rejectshop():
    id=request.args.get('id')
    cmd.execute("update tb_login_master set type='reject' where lid='"+id+"'")
    con.commit()
    return admin_view_shop()






@pyfile.route('/allotpkg',methods=['get','post'])
def allotpkg():
    id=request.args.get('id')
    session['pkg']=id
    cmd.execute("SELECT * FROM `tb_registration` WHERE TYPE='district'")
    res=cmd.fetchall()
    return render_template("allotpkg.html",val=res)


@pyfile.route('/allotingpkg',methods=['get','post'])
def allotingpkg():

    id=session['pkg']
    dis=request.form['select']
    cmd.execute("INSERT INTO `tb_packagealllot` VALUES(null,'"+dis+"','"+id+"')")
    con.commit()
    return viewpackadmin()




















if __name__=='__main__':
    pyfile.run(debug=True)