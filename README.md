# Viewstate Extractor
Extract unique values
```
python viewstate-extractor.py ~/all-burp-history -v | grep '__VIEWSTATEGENERATOR:' | cut -d ' ' -f2 | sort | uniq -u > unique_viewstate_generators    
python viewstate-extractor.py ~/all-burp-history -v | grep '__VIEWSTATE:' | cut -d ' ' -f2 | sort| uniq -u > unique_viewstates
```
Spray them with badsecrets
```
for i in $(cat unique_viewstate_generators); do for n in $(cat unique_viewstates); do badsecrets $n $i; done; done
```
