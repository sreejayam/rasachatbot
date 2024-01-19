import mysql.connector as my
def Dataupdate(name,Crop_stage):
    db = my.connect(
        host="127.0.0.1",
        user="root",
        password="123Sreejaya123",
        database='db1',
    )

    cr = db.cursor()
    # cr.execute("show databases;")
    # for x in cr:
    #     print(x[0])

    cr.execute("CREATE TABLE IF NOT EXISTS simplify (name VARCHAR(255), Crop_stage VARCHAR(255));")

    cr.execute("show tables;")
    for y in cr:
        print(y[0])

    query = 'INSERT INTO simplify(name,Crop_stage) VALUES("{0}","{1}");'.format(name, Crop_stage)

    cr.execute(query)
    db.commit()  # db.commit() ensures that the changes are permanently saved.
    print(cr.rowcount,"record inserted")
if __name__ == "__main__":
    Dataupdate("minnu", "cultivation")










