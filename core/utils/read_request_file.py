import docx2txt

def read_request_file(file):
    if str(file).split('.')[-1] == 'docx':
        return docx2txt.process(file)
    return file.read().decode('utf-8')