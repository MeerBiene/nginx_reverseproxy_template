# nginx reverse proxy vhost template

[![forthebadge](https://forthebadge.com/images/badges/certified-snoop-lion.svg)](https://forthebadge.com)

This is an easy to use nginx reverse proxy vhost template, mainly used by myself. If you want to use it replace example.com with your domain and change the certificate paths. Also make sure to generate the diffie helman parameters.

 For advanced authentification you will need to make yourself familiar with creating a Root Certificate Authority and issuing Client Certificates.
 
 ### Features:
 - *http2*
 - Cipher suites picked for maximum *paranoia*
 - Disabled TLSv1/1.1 (enabled by default in most configurations)
 - Authentification stuff if needed (Basic http authentification and client certificates)
  - Option to enable traffic encryption between the nginx reverse proxy and your application

 ![Security](https://i.imgur.com/G52NR0r.png)

 ## Disclaimer:
 > I made this template with the best of my knowledge. Please do not think that this template is complete. I will keep working on it and try to update its as soon as Issues arise or I learn something new that I consider important for this template to work. <br><br> 
 If you encounter any bugs or something goes wrong, dont hesitate to open an Issue here on Github. 


 ## Setup (ADVANCED):

 This walks you though the steps of gaining a free Lets Encrypt Certificate and proxying your domain to your application.

 Before you start: Clone or download this repository to your desired machine and run the command inside it.

 - **Step 1:** Install Certbot.
 - **Step 2:** Run Certbot with the following command: `certbot -d yourdomain.com certonly`. Remember to replace yourdomain.com with your domain.
 - **Step 3:** If you have python installed run the command `python setup.py` and enter your domain when asked. This will generate your config file automatically for you. If you encounter any errors, make sure you have python3 installed and run the script with python3!
 - **Step 3.1:** If you want to do the changes manually, simply open the example.com.conf file and replace example.com with your domain and according certificate paths. Remembed to rename the file to your domainname.

> Some additional Notes: 
> - When using certbot, make sure nginx is not running and choose the option to spin up a temporary web server. 
> - To enable your config, place the yourdomain.com.conf file in `/etc/nginx/sites_available` and run the command `nginx -t`. If it shows OK, move on and run `ln -s /etc/nginx/sites-enabled/yourdomain.com.conf /etc/nginx/sites-available/`
> - Test your config by running `nginx -t` before reloading or restarting nginx

## Setup (BEGINNER):

This will walk you through all steps required to reverseproxy your domain to your backend application.

> Note: All of the following steps/commands were made and recorded on a Debian 10 VM. If you use a non debian based system for your server, make sure to adjust your commands accordingly, before copypasting them and wondering why it errors.

Before you start: Clone or download this repository to your desired machine.

- **Step 1:** Go to the homepage of your Domainprovider and make a new DNS Record. If you are using Namecheap, its under the option "Advanced DNS". ![Namecheap Exmaple](https://i.imgur.com/FqWMZeG.png)In there, register a new DNS Record like so: ![dns rec namecheap](https://i.imgur.com/TKPjCbX.png) The Host Field is the subdomain where your application will live, so if i wanted to use `app.example.com` I would have to put `app` in the host field. Enter your IP Adress in the designated input field and you're good to go.

- **Step 2:** Make sure nginx and no other webservers are running on your server. Stop nginx with `systemctl stop nginx` and make sure its not running with `systemctl status nginx`. If its not running the output will look like this: ![Nginx not running example](https://i.imgur.com/yBHRXgV.png)

- **Step 3:** Install Certbot. Instructions can be found [here](https://certbot.eff.org/)

- **Step 4:** Obtain a certificate for your domain. Do so by running the command `certbot -d yourdomain.com certonly`. Remember to replace yourdomain.com with your domain. During the setup, certbot will ask you if you want to spin up a temporary webserver or use nginx. Pick the standalone Webserver option, as seen here: ![certbot standalone example](https://i.imgur.com/thfwa0m.png)

- **Step 4.1** Obtain the Diffie Helman Parameters. Do so by installing openssl. When youre done run the command `openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096` and be prepared to wait a very long time. (between 1 and 15 minutes depending on your system). ![dhparams running](https://i.imgur.com/n7QSmeh.png)

- **Step 5:** Download or clone this repository if you havn't already.

- **Step 6:** *(Needs python installed)* If you have python installed, run `python3 setup.py` inside the repositories folder. Enter your domain and answer all other questions. When the script is done, you will find a newly generated file with the name of your domain. Place this inside of `/etc/nginx/sites-available` and run the command `nginx -t`. If it shows OK, move on to step 7. If there are any syntax errors, go ahead and try to fix them. If you dont fix them and restart NGINX, it will break. If everything went correctly your output should look like this: ![nginx configtest ok](https://i.imgur.com/gP8HwXa.png)


- **Step 6.1** If you don't have Python installed, you have to manually go over the config file and change your desired values. I would recommend to just copy the exmaple.conf file and name the new file yourdomain.com.conf (e.g.: `app.example.com.conf` for app.example.com THe command for this example would be: `cp example.com.conf /etc/nginx/sites-available/app.example.com.conf`. Adjust it before running this command and remember to put in your domain. 
> Its not directly neccessary to name your configuration files after your domain, but I like to handle it that way, for easier overview.
<br>

> Note: Remember to put `.conf` at the end of you domain configuration file, so `subdomain.domain.com.conf` or `app.example.com.conf` or `meer.is-in-outer.space.conf` (yes the last one is a real example, if you want a subdomain with `is-in-outer.space` for an imageserver or so, slide me a DM on discord (MeerBiene#7060)) 

- **Step 7:** Create a symlink. Do so by running the command `ln -s /etc/nginx/sites-availabe/yourdomain.com.conf /etc/nginx/sites-enabled/`. Check your nginx config again with `nginx -t`and if it shows "OK", move on to step 8.

- **Step 8:** Restart Nginx. Do so by running the command `systemctl restart nginx`. Check that it started correctly by running `systemctl status nginx`. Your output should look like this if no errors were encountered: ![nginx running](https://i.imgur.com/jrdPgfD.png)

- **Step 9:** Start your application on the port that you specified in the setup process. Then visit your domain in the browser to ensure everything worked properly.

## Contributing:

If you find an Issue that you know how to resolve, simply submit a pull request, its greatly appreciated.