# nginx reverse proxy vhost template

[![forthebadge](https://forthebadge.com/images/badges/certified-snoop-lion.svg)](https://forthebadge.com)

This is an easy to use nginx reverse proxy vhost template, mainly used by myself. If you want to use it replace example.com with your domain and change the certificate paths. Also make sure to generate the diffie helman parameters.

 For advanced authentification you will need to make yourself familiar with creating a Root Certificate Authority and issuing Client Certificates.
 
 Features:
 - *http2*
 - Cipher suites picked for maximum paranoia
 - Disabled TLSv1/1.1 (enabled by default on most configurations)
 - Option to enable encryption between nginx and your application
 - Authentification stuff if needed (Basic http authentification and client certificates)

 ## Setup:

 This walks you though the steps of gaining a free Lets Encrypt Certificate and proxying your domain to your application.

 - Step 1: Install Certbot.
 - Step 2: Run Certbot with the following command: `certbot -d yourdomain.com certonly`. Remember to replace yourdomain.com with your domain.
 - Step 3: If you have python installed run the command `python setup.py` and enter your domain when asked. This will generate your config file automatically for you.
 - Step 3.1: If you want to do the changes manually, simply open the example.com.conf file and replace example.com with your domain and according certificate paths.

> Some additional Notes: 
> - When using certbot, make sure nginx is not running and choose the option to spin up a temporary web server. 
> - Test your config by running `nginx -t` before reloading or restarting nginx