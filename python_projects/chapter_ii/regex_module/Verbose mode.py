import re

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(exit|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?      #area code
                        (\s|-|\.)?      #seperator
                        \d{3}       #first 3 digits
                        (\s|-|\.)       #seperator
                        \d{4}       #last 4 digits
                        (\s*(exit|x|ext.)\s*\d{2,5})?       #extenstion
                        )''', re.VERBOSE) # re.verbose makes the regex ignore all comments so you can better organize your code
