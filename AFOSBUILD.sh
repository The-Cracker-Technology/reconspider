rm -rf /opt/ANDRAX/reconspider

cd plugins
tar -xvJf IP2PROXY.tar.xz
cd ..

cp -Rf $(pwd) /opt/ANDRAX/reconspider

pip3 install shodan requests prompt_toolkit wget beautifulsoup4 click urllib3 IP2proxy wget paramiko h8mail nmap pythonping whois gmplot pillow lxml
