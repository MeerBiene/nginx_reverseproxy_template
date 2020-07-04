# automatic vhost setup
domain = input("Enter your domain (the one you used in the certbot command after the -d flag): ")
ip = input("Enter the IP, where you want to proxy your traffic to now (for localhost use localhost or 127.0.0.1): ")
port = input("Enter the desired port now: ")

# input
fin = open("example.com.conf", "rt")

# output
domainfinal = domain + ".conf"
fout = open(domainfinal, "wt")

for line in fin:
    fout.write(line.replace('example.com', domain).replace('PROXIEDIP', ip).replace('PORT', port))

fin.close()
fout.close()
print("Done.")
exit()