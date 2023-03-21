# F5 Distributed Cloud TLS and Cipher Comparison

## Purpose

This script will compare the list of documented F5 Distributed Cloud TLS and Cipher versions with the TLS version and Ciphers from an sslscan xml output.

## Limitations

This script will not compare TLS 1.3 Cipher groups. 

## sample sslscan results in this repo include:
From March 2023
  google.xml    #google.com
  nginx.xml     #nginx.org
  xc-high.xml   #F5 Distributed cloud load balancer configured to High
  xc-medium.xml #F5 Distributed cloud load balancer configured to Medium
  xc-low.xml    #F5 Distributed cloud load balancer configured to Low

## Requirements

-   Python 3.x
-   xctlsratings.csv file containing the supported TLS Versions and Ciphers support on XC.
-   xml output from sslscan

## Installation

1.  Ensure Python 3.x is installed on your system.
2.  Clone this repository or download the `f5xcsslcheck.py` script.

## Usage

1.  Run sslscan on the desired domain and save the output in XML format:
```shell
sslscan <domainname> --xml=<xml_file_path>
```

2.  Run the `f5xcsslcheck.py` script with the path to the sslscan XML output file as an argument:
```shell
python f5xcsslcheck.py <xml_file_path>
```
3.  The script will display the list of matching ciphers along with their SSL/TLS version.

## Example

### Input

```shell
sslscan example.com --xml=sslscan_example_com.xml python f5xcsslcheck.py sslscan_example_com.xml
```

### Output

```shell
SSL/TLS Version,Cipher,Rating
TLSv1.2,ECDHE-RSA-AES128-GCM-SHA256,High
TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,High
```

## Additional Information

If your `xctlsratings.csv` file is not in the same directory as the `f5xcsslcheck.py` script, you need to update the `ratings_file_path` variable in the script with the correct path to the file.