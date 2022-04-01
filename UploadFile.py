import dropbox
import os
class TransferData:

    def _init_(self,accessToken):
        self.accessToken=accessToken

    def Upload_file(self, file_from,file_to):
        dbx=dropbox.Dropox(self.accessToken)

        for roots, dirs, files in os.walk(file_from): 

            for filename in files:
             local_path = os.path.join(roots, filename)

            relative_path = os.path.relpath(local_path, file_from)   
            dropbox_path = os.path.join(file_to, relative_path)
            
            with open(local_path,'rb') as f:
                     dbx.files_upload(f.read(), dropbox_pathsss)
def main():
                

     accessToken:"sl.BD1FPr5KkcDCJW1WaK3z5rHEP3VVkamooojA0IG6jtPC_HxOezVSIkKmPEHWx0lfU8QBgODPgqSulJrNRtooKhgNJAQQUF903TQHzHVCoXY6CEuMt77lXfRmRPvHawsvrBhLKSZwwgk"
     transferData =TransferData(accessToken)
                    




    
    