#!/bin/bash
sudo apt update
sudo apt install -y nginx
sudo systemctl start nginx.service
sudo systemctl enable nginx.service
sudo truncate -s 0 /var/www/html/index.nginx-debian.html
sudo tee -a /var/www/html/index.nginx-debian.html > /dev/null <<EOT
<!DOCTYPE html>
<html>
<head>
<title>DevOps Task</title>
</head>
<body>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Devops-toolchain.svg/640px-Devops-toolchain.svg.png">
</body>
</html>
EOT