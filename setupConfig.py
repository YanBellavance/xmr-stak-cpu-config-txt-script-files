#!/usr/bin/python

import sys, getopt
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import io
import re
#./setupConfig.py -i $CONFIG_TXT_INPUT -o $CONFIG_TXT_OUTPUT  -c $NUM_CORES -u $USER_ID

def main(argv):
  inputfile = ''
  outputfile = ''
  numcores = 1
  userid_suffix = ''
  try:
    opts, args = getopt.getopt(argv,"hi:o:c:u:")
  except getopt.GetoptError:
    print 'setupConfig.py -i <inputfile> -o <outputfile>  -c <numcores> -u <userid_suffix>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'setupConfig.py -i <inputfile> -o <outputfile>  -c <numcores> -u <userid_suffix>'
      sys.exit()
    elif opt == '-i':
      inputfile = arg
    elif opt == '-o':
      outputfile = arg      
    elif opt == '-c':
      numcores = int(arg)
    elif opt == '-u':
      userid_suffix = arg

  print 'Input file is :"', inputfile
  print 'Output file is :"', outputfile
  print 'number of cores :', numcores
  print 'user id suffix is :"', userid_suffix

  #Create temp file
  with io.FileIO(outputfile, "w") as new_file:
    with open(inputfile) as old_file:
      for line in old_file:
        if re.search("@TOKEN_CORE",line):
          for core in range(0,numcores):
            core_line = line.replace("@TOKEN_CORE", str(core))
            new_file.write(core_line)
        elif re.search("@TOKEN_USER_ID_SUFFIX",line):
          wallet_address = line.replace("@TOKEN_USER_ID_SUFFIX", userid_suffix)
          new_file.write(wallet_address)
        else:
          new_file.write(line)

if __name__ == "__main__":
  main(sys.argv[1:])
