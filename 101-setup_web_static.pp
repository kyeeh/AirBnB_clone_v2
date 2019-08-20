# Install Nginx web server with custom header response
exec { 'Nginx install with custom header response':
command => 'sudo apt-get update -y && sudo apt-get install nginx -y && 
            header="\\\tadd_header X-Served-By $HOSTNAME;\n" && 
            sudo sed -i "38i $header" /etc/nginx/sites-available/default && 
            sudo service nginx restart',
provider => shell,
}
