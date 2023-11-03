print ("hello")
from sqlalchemy import create_engine, text


# PyMySQL
engine = create_engine("mysql+pymysql://root:test@localhost/stockdb", future=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

def createUser (username, name): #prepared statement
    with engine.connect() as conn:
        result = conn.execute( text("INSERT INTO stockuser (username, name) VALUES (:username, :name)"),
                    [{"username": username, "name": name}] )
        conn.commit()
        print("created user: " + username)
        #print (result.lastrowid) #returns userid

def deleteAll (username): #calling stored procedure
    with engine.connect() as conn:
        result = conn.execute( text("CALL deleteAll(:username)"),
                    [{"username": username}] )
    print("deleted user: " + username)
        
def showAllUsers ():
    print("users in table stockuser:")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT username, name FROM stockuser"))
    for row in result:
        print(f"username: {row.username}  name: {row.name}")

#createUser("john123", "john")
#showAllUsers()
#deleteAll("john123")
showAllUsers()


    