'''
Purpose: 
This script will compare the list of documented F5 Distributed Cloud TLS and 
Cipher versions with the TLS version and Ciphers from an sslscan xml output

Requirements:
  xctlsratings.csv file containing the support TLS Versions, and Ciphers support on XC.
  xml output from sslscan

Usage:
  sslscan <domainname> --xml=<xml_file_path>
  python f5xcsslcheck.py <xml_file_path>
'''


import xml.etree.ElementTree as ET
import csv
import sys

def process_sslscan(xml_file_path, ratings_file_path):
    # Parse sslscan.xml
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    accepted_ciphers = []

    # Get the accepted ciphers along with their SSL/TLS version
    for cipher in root.iter('cipher'):
        sslversion = cipher.get('sslversion')
        cipher_name = cipher.get('cipher')
        accepted_ciphers.append((sslversion, cipher_name))

    # Read xctlsratings.csv
    with open(ratings_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        print(','.join(header))

        # Find and print matching rows
        for row in csvreader:
            if (row[1], row[2]) in accepted_ciphers:
                print(','.join(row))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("This script requires the xml output from the command: sslscan <domainname> --xml=<xml_file_path>")
        print("Usage: python f5xcsslcheck.py <xml_file_path>")
        sys.exit(1)

    xml_file_path = sys.argv[1]
    ratings_file_path = 'xctlsratings.csv'  # Replace this with the path to your xctlsratings.csv file if necessary

    process_sslscan(xml_file_path, ratings_file_path)
