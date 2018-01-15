import os
import subprocess
import json
from time import strftime

from flask import current_app

class Documents(object):
    DOC = None
    
    def __init__(self, directory):
        self.directory = directory
        self.documents = None
        self.content = None
        if os.path.exists(directory):
            self.documents = os.path.join(self.directory, 'documents')
            self.content = os.path.join(self.directory, 'content')
            if not os.path.exists(self.documents):
                os.makedirs(self.documents)
            if not os.path.exists(self.content):
                os.makedirs(self.content)

    @classmethod
    def appdoc(cls):
        if Documents.DOC is None:
            Documents.DOC = Documents(current_app.config['DOCUMENT_DIR'])
        return Documents.DOC

    def relative(self, linkpath, docpath):
        dots = []
        commonpath = os.path.commonpath([linkpath, docpath])
        subpath = docpath[len(commonpath) + 1:]
        parentpath, tail = os.path.split(linkpath)

        rest = parentpath

        while rest != commonpath and rest != '':
            dots.append('..')
            rest, tail = os.path.split(rest)

        relativepath = os.path.join(*dots, subpath)
        checkpath = os.path.abspath(os.path.join(parentpath, relativepath))
        if checkpath != docpath:
            raise(ValueError('%s != %s [%s %s] ' % (checkpath, docpath, linkpath, relativepath)))

        return relativepath

    def commit(self):
        datestr = strftime('%Y%m%d%H%M%S')
        cwd = os.getcwd()

        os.chdir(self.directory)

        subprocess.call('git add .', shell=True)
        subprocess.call('git commit -m "%s"' % (datestr), shell=True)
        
        os.chdir(cwd)

    def get_filename(self, docid, filename, doctype, makedirs=False):
        docpath = os.path.join(doctype, docid)
        if makedirs and not os.path.exists(docpath):
            os.makedirs(docpath)
        return os.path.join(self.content, docid, filename)

    def remove_document_link(self, document, docid):
        if self.documents is not None:
            linkpath = os.path.join(self.documents, document, docid)
            if os.path.exists(linkpath):
                os.unlink(linkpath)

    def add_document_link(self, document, docid):
        if self.documents is not None and self.content is not None:
            linkdir = os.path.join(self.documents, document)
            if not os.path.exists(linkdir):
                os.makedirs(linkdir)
            linkpath = os.path.join(self.documents, document, docid)
            docpath =  os.path.join(self.content, docid)
            
            if not os.path.exists(linkpath):
                os.symlink(self.relative(linkpath, docpath), linkpath)

    def saveContent(self, document, docid, content):
        if self.content is not None:
            deltafile = self.get_filename(docid, 'delta', self.content, True)
            with open(deltafile, 'w') as outfile:
                print(content, file=outfile)

            docfile = self.get_filename(docid, 'document', self.content, True)
            current_document = None

            if os.path.exists(docfile):
                with open(docfile, 'r') as outfile:
                    current_document = outfile.readline().strip()
                
            with open(docfile, 'w') as outfile:
                print(document, file=outfile)

            if current_document is not None and document != current_document:
                self.remove_document_link(current_document, docid)

            self.add_document_link(document, docid)
            self.commit()

    def saveDocument(self, document, items):
        docids = []
        for item in items:
            docids.append(item['id'])
            self.saveContent(document,
                             item['id'],
                             json.dumps(item))
        document_file = os.path.join(self.documents, document, 'document.txt')
        with open(document_file, 'w') as outfile:
            print('\n'.join(docids), file=outfile)

    def loadContent(self, docid):
        if self.content is not None:
            deltafile = self.get_filename(docid, 'delta', self.content, True)
            with open(deltafile, 'r') as infile:
                return json.loads(infile.read())
        return {}

    def loadDocument(self, document):
        items = []
        content = []
        document_file = os.path.join(self.documents, document, 'document.txt')
        with open(document_file, 'r') as infile:
            items = infile.read().strip().split('\n')

        for item in items:
            content.append(self.loadContent(item))
        return content
