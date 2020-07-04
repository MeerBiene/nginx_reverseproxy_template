# automatic vhost setup
domain = input("Enter your domain (the one you used in the certbot command after the -d flag): ")

# input
fin = open("example.com.conf", "rt")

# output
domainfinal = domain + ".conf"
fout = open(domainfinal, "wt")

for line in fin:
    fout.write(line.replace('example.com', domain))
    
fin.close()
fout.close()
print("Done.")
exit()