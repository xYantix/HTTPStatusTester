# HTTPStatusTester

This script will take a list of domains and test their HTTP responses. The URLs are then saved into .txt files based on the status code returned. eg 200.txt, 404.txt

## Usage

Run with the following:
python3 statuscheck.py -l subdomains.txt

### Options
-t  Define the number of threads you wish to use. Default value is 10.



First version did not include multithreading. I ran version 1 over a list of 4200 subdomains and it took with the folllwing results:
* real	61m12.330s
* user	5m22.513s
* sys	1m7.630s

After implementing this multithreading method I see a HUGE improvement:
* real	7m15.777s
* user	8m26.937s
* sys	4m40.548s
