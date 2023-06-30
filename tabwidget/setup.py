import glob
import pandas as pd

class Setup:
    def __init__(self, name, path):
        self.name = name
        self.path = path

        self.search_for_probes()
        self.load_data(0)

    def search_for_probes(self):

        path = self.path

        files = glob.glob(f"{path}**/*probe*.csv", recursive=True)
        files.sort()
        files.append("None")

        self.probefiles = files
        self.selected_probe = 0

    def load_data(self, index):
        filename = self.probefiles[self.selected_probe]
        if filename != "None":
            df = pd.read_csv(filename)
            self.data = df
        else:
            self.data = None
            
    def print_setup(self):
        # maybe better in json.dumps?!
        print(f"name: {self.name}")
        print(f"path: {self.path}")
        print(f"probefiles: {self.probefiles}")
        print(f"selected_probe: {self.selected_probe}")
        # print(f"data: {self.data}")
        # setup["Data"] = df.to_dict()


if __name__ == '__main__':

    setups = []
    setups.append(Setup("Setup_A", "./data_1/"))
    setups.append(Setup("Setup_B", "./data_2/"))
    setups.append(Setup("Setup_C", "./data_2/"))

    for s in setups:
        s.print_setup()
