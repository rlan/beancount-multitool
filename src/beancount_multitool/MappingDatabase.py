import re
from tqdm import tqdm

from .read_config import read_config


class MappingDatabase:
    def __init__(self, file_name: str):
        # params
        self.file_name = file_name
        # attributes
        self.config = read_config(file_name)
        self.default = self.config["default"]
        # self.blank = self.config["blank"]
        if "mapping" in self.config:
            self.mappings = self.config["mapping"]
        else:
            self.mappings = []
        self.validate()
        self.fill_blanks()
        self.patterns = self.compile(self.mappings)

    def validate(self):
        # TODO
        pass

    def fill_blanks(self):
        # TODO join with self.blank
        pass

    def compile(self, mappings: dict) -> list:
        """Compile regular expressions text into objects"""

        print(f"Found {len(mappings)} mapping(s) in {self.file_name}")
        # print(data) # debug
        # print(type(data)) # debug
        print("Compiling regexp objects...")
        # pattern = [re.compile(x["regex"]) for x in mapping["mapping"]]
        # Use for-loop to catch and skip any regex syntax errors
        patterns = []
        for x in tqdm(mappings):
            # print(x["regex"]) # debug
            try:
                regex = re.compile(x["regex"])
            except re.error as e:
                print(f"Error: {e}")
                print(f"Skipping: {x}")
            else:
                patterns.append(regex)
        print(f"Compiled {len(patterns)} regexp objects")
        return patterns

    def match(self, description: str) -> list[dict]:
        """Given description, return mappings whose regular expression has matched.

        There can be multiple matches.

        Parameters
        ----------
        description : str
            A text signature for regular expressions to match.

        Returns
        -------
        list[dict]
            A list of matched mapping. If no match is found, the default is returned.
        """

        matches = []
        for idx, x in enumerate(self.patterns):
            if x.search(description) is not None:
                matches.append(self.mappings[idx])
        if len(matches) == 0:
            matches.append(self.default)
        return matches
