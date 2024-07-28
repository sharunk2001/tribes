from flask import *
import pymysql
con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='tribe')
cmd=con.cursor()
adr=Flask(__name__)

@adr.route('/login',methods=['get','post'])
def login():
    USERNAME=request.form["uname"]
    PASSWORD=request.form["pswd"]
    cmd.execute("select * from tb_login_master where username='"+USERNAME+"' and password='"+PASSWORD+"' and type='public' ")
    s=cmd.fetchone()
    if s is None:
        return jsonify({'task': "invalid"})
    else:
        id = s[0]
        return jsonify({'task': str(id)})

@adr.route('/pubreg',methods=['get','post'])
def pubreg():
    Firstname=request.form['fnm']
    Lastname=request.form['lnm']
    Gender=request.form['gender']
    Place=request.form['place']
    PostOffice=request.form['po']
    Pin=request.form['pin']
    PhoneNumber=request.form['phno']
    Email=request.form['mail']
    Password=request.form['pswd']
    cmd.execute("insert into tb_login_master values(null,'"+Email+"','"+Password+"','public')")
    lid=con.insert_id()
    cmd.execute("insert into tb_publicreg values('"+str(lid)+"','"+Firstname+"','"+Lastname+"','"+Gender+"','"+Place+"','"+PostOffice+"','"+Pin+"','"+PhoneNumber+"','"+Email+"')")
    con.commit()
    return jsonify({'task': "success"})

@adr.route('/addcomppub',methods=['get','post'])
def addcomppub():
    id = request.form['id']
    complaint=request.form['complaint']
    cmd.execute("insert into tb_complaint values(null,'"+str(id)+"',curdate(),'"+complaint+"','pending')")
    con.commit()
    return jsonify({'task': "success"})

@adr.route('/addproblmpub',methods=['get','post'])
def addproblmpub():
    id = request.form['id']
    TribeArea=request.form["tarea"]
    ProblemName=request.form["prblm"]
    Description=request.form["des"]
    cmd.execute("insert into tb_tribeproblem values(null,'"+str(id)+"','"+TribeArea+"','"+ProblemName+"','"+Description+"')")
    con.commit()
    return jsonify({'task': "success"})

@adr.route('/viewpdtpub',methods=['POST'])
def viewpdtpub():
    try:
        #BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

        cmd.execute("SELECT MAX(bid)+1 FROM `tb_bill`")
        s=cmd.fetchone()
        if s is not None:
            bilid=s[0]

        else:
            bilid=1


        #BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        cmd.execute("select * from tb_product")
        row_headers = [x[0] for x in cmd.description]
        s = cmd.fetchall()
        print(s)
        json_data = []
        for result in s:
            json_data.append(dict(zip(row_headers, result)))
        con.commit()
        print(json_data)
        return jsonify({"task":json_data,"id":str(bilid)})
    except Exception as e:
        print(e)

@adr.route('/viewnotification', methods=['POST'])
def viewnotification():
            try:
                cmd.execute("select * from tb_notification")
                row_headers = [x[0] for x in cmd.description]
                s = cmd.fetchall()
                print(s)
                json_data = []
                for result in s:
                    json_data.append(dict(zip(row_headers, result)))
                con.commit()
                print(json_data)
                return jsonify(json_data)
            except Exception as e:
                print(e)

@adr.route('/viewevents', methods=['POST'])
def viewevents():
            try:
                 cmd.execute("SELECT `prgm_name`,`details`,`photo` FROM `tb_event`")
                 row_headers = [x[0] for x in cmd.description]
                 s = cmd.fetchall()
                 print(s)
                 json_data = []
                 for result in s:
                     json_data.append(dict(zip(row_headers, result)))
                 con.commit()
                 print(json_data)
                 return jsonify(json_data)
            except Exception as e:
                        print(e)

@adr.route('/viewawareness', methods=['POST'])
def viewawareness():
            try:
                 cmd.execute("SELECT `prgm_name`,`details`,`photo` FROM `tb_awareness` ")
                 row_headers = [x[0] for x in cmd.description]
                 s = cmd.fetchall()
                 print(s)
                 json_data = []
                 for result in s:
                     json_data.append(dict(zip(row_headers, result)))
                 con.commit()
                 print(json_data)
                 return jsonify(json_data)
            except Exception as e:
                        print(e)


@adr.route('/addbill',methods=['get','post'])
def addbill():
    bilid = request.form['billid']
    cuid=request.form['cuid']
    total=request.form['total']
    try:
        cmd.execute("insert into tb_bill values('"+str(bilid)+"','" + str(cuid) + "',curdate(),'" + total + "','pending')")
        con.commit()
    except:
        cmd.execute("UPDATE `tb_bill` SET DATE=CURDATE(),total='" + total + "' WHERE cuid='" + str(cuid) + "' AND bid='"+str(bilid)+"'")
        con.commit()
    return jsonify({'task': "success"})


@adr.route('/billpdt',methods=['get','post'])
def billpdt():
    print(request.form)
    bilid=request.form['bid']
    cuid=request.form['cuid']
    total=request.form['total']
    product = request.form['product']

    quantity = request.form['quantity']
    if str(bilid)=="None" or str(bilid)=="0":
        try:
            cmd.execute("SELECT MAX(bid)+1 FROM `tb_bill`")
            s=cmd.fetchone()
            print(s,"+++++++++++")
            if s is not None:
                bilid=int(s[0])

            else:
                bilid=1
        except:
            bilid=1
    print(bilid,"+=================")
    qr="SELECT `quantity` FROM `tb_product` WHERE `id`='"+product+"'"
    cmd.execute(qr)
    respc=cmd.fetchone()
    if int(respc[0])>int(quantity):
        print(cuid,"======================================")
        cmd.execute("insert into tb_billproduct values(null,'" + str(bilid) + "','"+product+"','" + total + "','"+quantity+"','"+cuid+"')")
        con.commit()

        upt="UPDATE tb_product SET quantity=quantity-'"+quantity+"' WHERE id='"+product+"'"
        cmd.execute(upt)
        con.commit()
        return jsonify({'task': "success"+"#"+str(bilid)})
    else:
        return jsonify({'task': "no"})




@adr.route('/viewpurchasepdt', methods=['POST'])
def viewpurchasepdt():
            lid=request.form['lid']
            bid=request.form['bid']
            try:
                

                cmd.execute("SELECT  `tb_product`.*,`tb_billproduct`.`quantity`,tb_billproduct.`price`,tb_billproduct.`bpid` FROM `tb_product` INNER JOIN `tb_billproduct` ON `tb_product`.`id`=`tb_billproduct`.`product` WHERE lid='"+str(lid)+"' and  tb_billproduct.bid='"+str(bid)+"'")
                row_headers = [x[0] for x in cmd.description]
                s = cmd.fetchall()
                print(s)
                json_data = []
                for result in s:
                    json_data.append(dict(zip(row_headers, result)))
                con.commit()
                print(json_data)
                return jsonify(json_data)
               
            except Exception as e:
                print(e)


@adr.route('/payment',methods=['get','post'])
def payment():
    try:
        cuid=request.form['cuid']
        total=request.form['total']
        accno = request.form['accno']
        billid = request.form['billid']

        cmd.execute("SELECT * FROM `tb_account` WHERE `lid`='"+str(cuid)+"' AND `accno`='"+accno+"'")
        s=cmd.fetchone()
        if s is not None:
            amount=s[3]
            if int(total)<int(amount):
                cmd.execute("UPDATE `tb_account` SET `amount`=amount - '"+total+"' WHERE  `lid`='"+str(cuid)+"' AND `accno`='"+accno+"' ")
                cmd.execute("UPDATE `tb_bill` SET `status`='payed' WHERE `bid`='"+str(billid)+"'")
                con.commit()
                return jsonify({'task': "success"})
            else:
                return jsonify({'task': "insufficent amount"})
        else:
           return jsonify({'task': "invalid account"})
    except Exception as e:
        print("err"+str(e))

@adr.route('/viewcomplaints', methods=['POST'])
def viewcomplaints():
    lid=request.form["lid"]

    try:
            cmd.execute("select * from tb_complaint where lid='"+lid+"'")
            row_headers = [x[0] for x in cmd.description]
            s = cmd.fetchall()
            print(s)
            json_data = []
            for result in s:
                json_data.append(dict(zip(row_headers, result)))
            con.commit()
            print(json_data)
            return jsonify(json_data)
    except Exception as e:
                print(e)
@adr.route('/deletepurchasepdt', methods=['POST'])
def deletepurchasepdt():
            bpid=request.form['bpid']
            
            try:
                cmd.execute("delete from tb_billproduct where bpid='"+str(bpid)+"'")
                
                con.commit()

           
                return jsonify({'task': "ok"})
            except Exception as e:
                print(e)










if __name__ == '__main__':
    adr.run(host='0.0.0.0', port=5000)