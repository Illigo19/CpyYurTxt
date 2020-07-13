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
import pyperclip







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


def client(x):
    
    hote = x
    print(type(hote))
    port = 12800

    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))
    print("Connexion établie avec le serveur sur le port {}".format(port))

    msg_a_envoyer = b""
    cl = ""
    while msg_a_envoyer != b"fin":
        msg_a_envoyer = pyperclip.paste()
        if msg_a_envoyer != cl:

            cl = msg_a_envoyer

            msg_a_envoyer = msg_a_envoyer.encode()
            # On envoie le message
            connexion_avec_serveur.send(msg_a_envoyer)
            msg_recu = connexion_avec_serveur.recv(1024)
            print(msg_recu.decode())
        

         # Là encore, peut planter s'il y a des accents

    print("Fermeture de la connexion")
    connexion_avec_serveur.close()
            


    

def serv():
    hote = ''
    port = 12800

    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_principale.bind((hote, port))
    connexion_principale.listen(5)
    print("Le serveur écoute à présent sur le port {}".format(port))

    connexion_avec_client, infos_connexion = connexion_principale.accept()

    msg_recu = b""
    while msg_recu != b"fin":
        msg_recu = connexion_avec_client.recv(1024)
        # L'instruction ci-dessous peut lever une exception si le message
        # Réceptionné comporte des accents
        se = msg_recu.decode()
        print(se)
        pyperclip.copy(se)
        connexion_avec_client.send(b"5 / 5")

    print("Fermeture de la connexion")
    connexion_avec_client.close()
    connexion_principale.close()

    


        
def conn():
    a = len(ipre)
    print(a)
    if a >= 1:
        print("SERVER OR CLIENT \n")
        print("1 : server \n2 : client")
        answer = input("> ")
        if answer == "1":
            print("server mod")
            serv()

            pass
        elif answer == "2":
            print("client mod")
            print(ipre[0])
            client(ipre[0])



    else:
        print("No IP renseigned")
        print("You can also been server !!!")
        answer = input(" You want ? (print : 'yes' if you want) : ")
        if answer == "yes":
            print("server mod")
            serv()
        else:
            menu()
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
        conn()
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

#fin
mydb.close()
