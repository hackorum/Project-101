import dropbox
import os
import sys


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_folder(self, folder_from, folder_to):
        dbx = dropbox.Dropbox(self.access_token)

        for (root, dirs, files) in os.walk(folder_from, topdown=True):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_from)
                dropbox_path = os.path.join(folder_to, relative_path)
                with open(file_path, "rb") as f:
                    dbx.files_upload(
                        f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite
                    )


def main():
    access_token = "get_your_own_token"
    transferData = TransferData(access_token)

    folder_from = input("Enter the folder you want to upload: ")
    folder_to = input("Enter the folder you want to name it in dropbox: ")

    transferData.upload_folder(folder_from, folder_to)


if __name__ == "__main__":
    main()
