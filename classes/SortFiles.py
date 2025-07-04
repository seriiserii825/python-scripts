import os
import shutil


class SortFiles:
    def __init__(self):
        self.current_path = os.getcwd()
        self.folder_path = ""
        self.selected_path = ""
        self.go_on = input(
            f"current folder is: '{self.current_path}', \
                    do you want to continue, (y/n)? "
        )
        if self.go_on != "y":
            exit()

    def createFolder(self, ext: str):
        """
        Create a folder based on the file extension.
        """
        folder_name: str = ext[1:]
        self.folder_path = os.path.join(self.current_path, folder_name)

        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)
            print(f"Folder {folder_name} created.")

    def sortFiles(self):
        """
        Sort files in the current directory based on their extensions.
        """
        for root_dir, sub_dir, filenames in os.walk(self.current_path):
            for filename in filenames:
                file_path = os.path.join(root_dir, filename)
                ext = os.path.splitext(filename)[1]
                if ext:
                    self.createFolder(ext)
                    target_path = os.path.join(self.folder_path, filename)
                    # copy file
                    shutil.copy(file_path, target_path)

    def removeEmptyFolders(self):
        """
        Remove empty folders after sorting files.
        """
        for root_dir, sub_dir, filenames in os.walk(self.current_path):
            for folder in sub_dir:
                folder_path = os.path.join(root_dir, folder)
                if not os.listdir(folder_path):
                    os.rmdir(folder_path)
                    print(f"Removed empty folder: {folder_path}")
