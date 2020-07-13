# function to end if user forgets to enter a certain value
def ender(msg):
    print(msg)
    exit()

# Questions
domain = input("Enter your domain (the one you used in the certbot command after the -d flag) \nAnswer here: ")
if domain == "":
    ender("Hey you forgot to enter a Domain.")
ip = input("Enter the IP, where you want to point NGINX to, without the port (for localhost use localhost or 127.0.0.1) \nAnswer here:  ")
if ip == "":
    ender("Hey, you forgot to enter an IP.")
port = input("Enter the desired port now \nAnswer here: ")
if port == "":
    ender("You forgot to enter a port.")
auth = input("Do you want to use any authentification features? \n(1) BASIC \n(2) ADVANCED \n(3) NONE \nAnswer here: ")
if auth == "":
    print("Using no Authentification.")
    auth = 3
enc = input("Do you want to encrypt the traffic between nginx and your application? \n(1) YES \n(2) NO \nAnswer here: ")
if enc == "":
    print("Using no proxy encryption.")
    enc = 2

# inputfile
fin = open("example.com.conf", "rt")
domainfinal = domain + ".conf"
# outputfile
fout = open(domainfinal, "wt")

def writerfunc(enc):
    if auth == "3" or auth.lower() == "no": # no auth
        for line in fin:
            if enc == "1" or enc.lower() == "yes": # encryption = yes
                fout.write(line.replace('example.com', domain).replace('TARGETIP', ip).replace('PORT', port).replace('#(E)', '').replace('#(E)', ''))
            else:
                fout.write(line.replace('example.com', domain).replace('TARGETIP', ip).replace('PORT', port).replace('#(E)', ''))
        fin.close()
        fout.close()
        print("Done. Remember to check the configuration file for any mistakes that could have occured.")
        exit()
    elif auth == "2" or auth.lower() == "advanced": # advanced 
        for line in fin:
            if enc == "1" or enc.lower() == "yes": # encryption = yes
                fout.write(line.replace('example.com', domain).replace('TARGETIP', ip).replace('PORT', port).replace('#(2)', '').replace('#(E)', ''))
            else:
                fout.write(line.replace('example.com', domain).replace('TARGETIP', ip).replace('PORT', port).replace('#(2)', ''))
        fin.close()
        fout.close()
        print("Done. Remember to check the configuration file for any mistakes that could have occured.")
        exit()
    elif auth == "1" or auth.lower() == "basic": # basic
        for line in fin:
            if enc == 1 or enc.lower() == "yes": # encryption = yes
                fout.write(line.replace('example.com', domain).replace('TARGETIP', ip).replace('PORT', port).replace('#(1)', '').replace('#(E)', ''))
            else:
                fout.write(line.replace('example.com', domain).replace('TARGETIP', ip).replace('PORT', port).replace('#(2)', ''))
        fin.close()
        fout.close()
        print("Done. Remember to check the configuration file for any mistakes that could have occured.")
        exit()
    else:
        print("This option does not match any of the availavle options. Available options are 1 - BASIC, 2 - ADVANCED, 3 - NONE. Quitting . . .")
        exit()
    
writerfunc(enc)