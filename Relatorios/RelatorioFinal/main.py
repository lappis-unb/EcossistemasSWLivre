import codecs

def open_file_with_encoding(file):
    encodings = ['utf-8', 'mac-roman','utf-16-le']
    print(file)
    for e in encodings:
        try:
            fh = codecs.open(file, 'r', encoding=e)
            fh.readlines()
            fh.seek(0)
        except UnicodeDecodeError:
            print('got unicode error with %s , trying different encoding' % e)
        else:
            print('opening the file with encoding:  %s ' % e)
            return e
            break 
    print("Error: Can't decode file: %s", file)
    return -1
    
def convert_file_to_utf8(file):
    sourceEncoding = open_file_with_encoding(file)
    if sourceEncoding == -1:
        print("Unable to read file encoding: %s", file)
        return 

    with codecs.open(file, "r", sourceEncoding) as sourceFile:
        with codecs.open(file + ".utf8", "w", "utf-8") as targetFile:
            while True:
                contents = sourceFile.read()
                if not contents:
                    break
                targetFile.write(contents)
    return

convert_file_to_utf8("relfinal.md")
