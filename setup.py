# automatic vhost setup
domain = input("Enter your domain (the one you used in the certbot command after the -d flag): ")
ip = input("Enter the IP, where you want to proxy your traffic to now (for localhost use localhost or 127.0.0.1): ")
port = input("Enter the desired port now: ")
auth = input("Do you want to use any authentification features? \n(1) BASIC \n(2) ADVANCED \n(3) NONE \nAnswer here: ")
enc = input("Do you want to encrypt the traffic between nginx and your application? \n(1) YES \n(2) NO \nAnswer here: ")

# input
fin = open("example.com.conf", "rt")
domainfinal = domain + ".conf"
# output
fout = open(domainfinal, "wt")

def writerfunc(enc):
    if auth == "3": # no auth
        for line in fin:
            if enc == "1": # encryption = yes
                fout.write(line.replace('example.com', domain).replace('TARGETIP', ip).replace('PORT', port).replace('#(E)', '').replace('#(E)', ''))
            else:
                fout.write(line.replace('example.com', domain).replace('TARGETIP', ip).replace('PORT', port).replace('#(E)', ''))
        fin.close()
        fout.close()
        print("Done. Remember to check the configuration file for any mistakes that could have occured.")
        exit()
    elif auth == "2": # advanced 
        for line in fin:
            if enc == "1": # encryption = yes
                fout.write(line.replace('example.com', domain).replace('TARGETIP', ip).replace('PORT', port).replace('#(2)', '').replace('#(E)', ''))
            else:
                fout.write(line.replace('example.com', domain).replace('TARGETIP', ip).replace('PORT', port).replace('#(2)', ''))
        fin.close()
        fout.close()
        print("Done. Remember to check the configuration file for any mistakes that could have occured.")
        exit()
    elif auth == "1": # basic
        for line in fin:
            if enc == 1: # encryption = yes
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