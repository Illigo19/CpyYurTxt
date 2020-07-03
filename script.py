"""  _____                   __     __                _______   _   
    / ____|                  \ \   / /               |__   __| | |  
    | |     ___  _ __  _   _   \ \_/ /__  _   _ _ __     | |_  _| |_ 
    | |    / _ \| '_ \| | | |   \   / _ \| | | | '__|    | \ \/ / __|
    | |___| (_) | |_) | |_| |    | | (_) | |_| | |       | |>  <| |_ 
    \_____\___/| .__/ \__, |    |_|\___/ \__,_|_|       |_/_/\_\\__|
             | |     __/ |                                        
             |_|    |___/         
BY socket()    

Illigo ---- 2020                            
"""

# on import les libraries
import socket 
import mysql.connector







#debut du programme
print(" \n deboggue Zone")
print("***********")


# Variables et listes
ipdb = 0

ipre = [] # stock l'ip du pc auquel le programmes va se connecté

# cherche et trouve l'IP du PC
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)


#connexion à une base de donné MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python"
    )


#determine Mycursor pour facilité le parcours de la Base de donnée
mycursor = mydb.cursor()
mycursor.execute("SELECT ip FROM user")
#DEBBOGUAGE
myresult = mycursor.fetchall()
a = len(myresult)


if a >= 1: # check si il y a des valeurs dans la base de donné

    

    #cherche si l'IP est déja renseignée dans la base de donné
    for x in myresult:
        
        x = str(x)
        
        ipf = "('" + ip + "',)"

        if ipf == x:
            ipdb = 1 #l'Ip est renseigné , on passe à la suite

if ipdb == 0:
     #l'IP n'est pas renseignée
    print(type(ip))
    print("Aucune IP reconnue ... \n")
    print("création d'un slot ....")
    query = "INSERT INTO user (ip) VALUES (%s) "
    mycursor.execute(query, (ip, ) )
    mydb.commit() 
    
def pipe():
    print("ADD a PIPE")
    print("\n 1 : with IP \n 2 : with Name")
    answer = input(" \n your choice : ")

    if answer == "1":
        print("say the EXACT IP")
        answer = input("\n IP : ")

        mycursor.execute("SELECT ip FROM user")
        myresult = mycursor.fetchall()
        a = len(myresult)
        if a >= 1:
            ipdb = 0
            for x in myresult:
                x = str(x)
                ipf = "('" + answer + "',)"
                if ipf == x:
                    ipdb = 1 #l'Ip est renseigné , on passe à la suite
            if ipdb == 1:
                print("IP correct")
                ipre.append(answer) #enregistrement de l'IP dans une liste pour pouvor la réutilisé
                print("\n IP enregistrée")

            else:
                print("IP incorrect . Vérifier l'orthographe.")
                pipe()


    elif answer == "2":
        print("say the EXACT name attribut at the IP")
        answer = input("\n Name : ")
        query = "SELECT ip FROM user WHERE name = %s"
        mycursor.execute(query, (answer, ) )
        myresult = mycursor.fetchone() #selectionne un seul, puisqu'il ne doit y en avoir qu'un

        a = len(myresult)
        if a >= 1:
            ipre.append(myresult[0])
            print(myresult)
        else:
            print("Name incorrect verify your writte")
            pipe()

        
        
        



def add():
    print("Your name ?")
    answer = input(": ")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT name FROM user")
    print(answer)

    myresult = mycursor.fetchall()
    a = len(myresult)
    print(a)
    namedb = 0


    if a >= 1: # check si il y a des valeurs dans la base de donné

    

    #cherche si l'IP est déja renseignée dans la base de donné
        for x in myresult:
        
            x = str(x)
        
            
            name = "('" + answer + "',)"
            

            if name == x:
                print("ce nom existe déja !! \n") #le nom existe déja
                add()
             
            
            else:   #le nom n'existe pas , le programme passe à la suite
                namedb = 1
                query = "UPDATE  user SET name = %s WHERE ip = %s"
                mycursor.execute(query, (answer, ip) )
                mydb.commit() 
        if namedb == 1:
            print("nom enregistré")
            menu()







    
def menu():

    print(" \n MENU :")
    print("1 : add or update your name in CYT")
    print("2 : connect (ONLY if you have ALREADY added a pipe")
    print("3 : add a pipe")

    answer = input("\n Your choice n° ")

    if answer == "1":
        print("\n \n ADD OR UPDATE NAME \n")
        add()
    
    
    elif answer == "2":
        pipe()
        menu()
        pass
    elif answer == "3":
        pipe()
        menu()


        pass

# DEBBOGUAGE    
print(ipdb)




#Génerique
print("**********")
print(" _____                    __     __                _______   _ ")
print("/ ____|                   \ \   / /               |__   __| | |")
print("| |     ___  _ __  _   _   \ \_/ /__  _   _ _ __     | |_  _| |")
print("| |    / _ \| '_ \| | | |   \   / _ \| | | | '__|    | \ \/ / __|")
print("| |___| (_) | |_) | |_| |    | | (_) | |_| | |       | |>  <| |")
print(" \_____\___/| .__/ \__, |    |_|\___/ \__,_|_|       |_/_/\_\\__|")
print("            | |     __/ |")
print("            |_|    |___/")
print(" \n by   SOCKET()")

print(" \n \nopensource 2020    --    Illigo \n")

print("your IP : " + ip)
print(" \n**********")


#debut
menu()










mydb.close()