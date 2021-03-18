from setuptools import setup
import os
import pip

fout = open("core/config.py", "w")
fout.write("shodan_api = " + '"' + "C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by" + '"' + "\n")
fout.close()

fout = open("plugins/api.py", "w")
fout.write("def phoneapis():"+ "\n")
fout.write("    api= "+ '"' + "e01791e4d18fbbdfa0c9033bf207decd,2f8c8e865a0b25bbf4da08c4db039b8d" + '"' + "\n")
fout.write("    return str(api)"+ "\n")
fout.write("def ipstack():"+ "\n")
fout.write("    api="+ '"' +"276cfee2c31729505691e515e8321a02"+ '"' + "\n")
fout.write("    return str(api)"+ "\n")
fout.write("def gmap():"+ "\n")
fout.write("    api="+ '"' +"AIzaSyAKGik6Fok3_mbIsgquaAnDGNy-h_AjhVw"+ '"' + "\n")
fout.write("    return str(api)"+ "\n")
fout.close()


setup(
    name="ReconSpider",
    version="1.0.5",
    description="Most Advanced OSINT Framework",
    url="https://github.com/bhavsec/reconspider/",
    author="BhavKaran (@bhavsec)",
    author_email="contact@bhavkaran.com",
    license="GPL-3.0",
    install_requires=["shodan", "requests", "prompt_toolkit","wget","beautifulsoup4","click","urllib3","IP2proxy","wget","paramiko","h8mail","nmap","pythonping","whois","gmplot","pillow","lxml"],
    console=["reconspider.py"],
)

print("\nInstallation Successfull")
