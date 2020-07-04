# nginx reverse proxy vhost template

[![forthebadge](https://forthebadge.com/images/badges/certified-snoop-lion.svg)](https://forthebadge.com)

This is an easy to use nginx reverse proxy vhost template, mainly used by myself. If you want to use it replace example.com with your domain and change the certificate paths. Also make sure to generate the diffie helman parameters.

 For advanced authentification you will need to make yourself familiar with creating a Root Certificate Authority and issuing Client Certificates.
 
 Features:
 - *http2 ready*
 - Cipher suites picked for maximum *paranoia*
 - Disabled TLSv1/1.1 (enabled by default in most configurations)
 - Authentification stuff if needed (Basic http authentification and client certificates)
  - Option to enable traffic encryption between the nginx reverse proxy and your application

 ![Security](https://i.imgur.com/G52NR0r.png)

 ## Setup (ADVANCED):

 This walks you though the steps of gaining a free Lets Encrypt Certificate and proxying your domain to your application.

 Before you start: Clone or download this repository to your desired machine and run the command inside it.

 - Step 1: Install Certbot.
 - Step 2: Run Certbot with the following command: `certbot -d yourdomain.com certonly`. Remember to replace yourdomain.com with your domain.
 - Step 3: If you have python installed run the command `python setup.py` and enter your domain when asked. This will generate your config file automatically for you. If you encounter any errors, make sure you have python3 installed and run the script with python3!
 - Step 3.1: If you want to do the changes manually, simply open the example.com.conf file and replace example.com with your domain and according certificate paths. Remembed to rename the file to your domainname.

> Some additional Notes: 
> - When using certbot, make sure nginx is not running and choose the option to spin up a temporary web server. 
> - To enable your config, place the yourdomain.com.conf file in `/etc/nginx/sites_available` and run the command `nginx -t`. If it shows OK, move on and run `ln -s /etc/nginx/sites-enabled/yourdomain.com.conf /etc/nginx/sites-available/`
> - Test your config by running `nginx -t` before reloading or restarting nginx

## Setup (BEGINNER):

This will walk you through all steps required to reverseproxy your domain to your backend application.

Before you start: Clone or download this repository to your desired machine.

- Step 1: Go to the homepage of your Domainprovider and make a new DNS Record. If you are using Namecheap, its under the option "Advanced DNS" ![Namecheap Exmaple](https://i.imgur.com/FqWMZeG.png). In there, 

- Step 2: Make sure nginx and no other webservers are running on your server. Stop nginx with `systemctl stop nginx` and make sure its not running with `systemctl status nginx`. If its not running the output will look like this: ![Nginx not running example](https://i.imgur.com/yBHRXgV.png)

- Step 3: Install Certbot. Instructions can be found [here](https://certbot.eff.org/)

- Step 4: Obtain a certificate for your domain. Do so by running the command `certbot -d yourdomain.com certonly`. Remember to replace yourdomain.com with your domain. During the setup, certbot will ask you if you want to spin up a temporary webserver or use nginx. Pick the standalone Webserver option, as seen here: ![certbot standalone example](https://i.imgur.com/thfwa0m.png)

- Step 5: Download or clone this repository if you hav'nt already.

- Step 6: If you have python installed, run `python3 setup.py` inside the repostories folder. Enter your domain and answer all other questions. When the script is done, you will find a newly generated file with the name of your domain. Place this inside of `/etc/nginx/sites-available` and run the command `nginx -t`. If it shows OK, move on to step 7. If there are any syntax errors, go ahead and try to fix them. If you dont fix them and restart NGINX, it will break. If everything went correctly your output should look like this: ![nginx configtest ok](https://i.imgur.com/gP8HwXa.png)

- Step 7: Create a symlink. Do sy by running the command `ln -s /etc/nginx/sites-availabe/yourdomain.com.conf /etc/nginx/sites-enabled/`. Check your nginx config again with `nginx -t`and if it shows "OK", move on to step 8.

- Step 8: Restart Nginx. Do so by running the command `systemctl restart nginx`. Check that it started correctly by running `systemctl status nginx`. Your output should look like this if no errors were encountered: ![nginx running](https://i.imgur.com/jrdPgfD.png)

- Step 9: Start your application on the port that you specified in the setup process. Then visit your domain in the browser to ensure everything worked properly.