"""
iTunes reader.
Authored by Prof. Eric Reed.
Modified by Zibin Yang.
"""

from enum import Enum
from functools import total_ordering


# zb: removed __gt__() etc, added @total_ordering
@total_ordering
class iTunesEntry:
    # zb: sort criteria determined by a class attribute is not a clean way
    # for a number of reasons (it cannot support concurrent sorting, and
    # changes the behavior of __eq__(), among other things), and there are
    # better ways to do this.  So for now, we'll only support sorting by time.
    class Sort(Enum):
        # TITLE = 0
        # ARTIST = 1
        TIME = 2

    sort_by = Sort.TIME

    def __init__(self, artist, title, run_time):
        self._artist = artist
        self._title = title
        self._run_time = run_time
        
    """ MODIFIED FOR ASSIGNMENT  #1 """   
    def __add__(self,x):
       return self._run_time + x
   
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
        
    def __eq__(self, other):
       return (self.run_time == other)    
   
    
   
    def __lt__(self, other):
        if self.sort_by is iTunesEntry.Sort.TIME:
            return self.run_time < other
        raise NotImplementedError

    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist

    @property
    def run_time(self):
        return self._run_time

    # zb: these two methods make the class hashable so that it can be used in,
    # say, set
    def __hash__(self):
        return hash((self.artist, self.title, self.run_time))


    def __str__(self):
        return (self.artist + " -> " + self.title + ": "
                + iTunesEntry.convert_time_to_string(self.run_time))

    @staticmethod
    def convert_time_to_string(tune_time):

        minutes = str(tune_time // 60)
        seconds = str(tune_time % 60)

        if len(seconds) < 2:
            seconds = "0" + seconds
        return minutes + ":" + seconds

    @classmethod
    def set_sort_type(cls, sort_type: Sort):
        if sort_type in iTunesEntry.Sort:
            cls.sort_by = sort_type
        else:
            raise ValueError


class iTunesEntryReader:

    def __init__(self, filename):
        self._tunes = []

        # zb: making sure fh is closed properly
        with open(filename, "r") as fh:
            while True:
                line = fh.readline()
                if iTunesEntryReader._is_data_line(line):
                    self._tunes.append(iTunesEntry(*self._read_one_entry(fh)))
                elif line == "":
                    break

    @staticmethod
    def _is_data_line(line):
        if len(line) < 1:
            return False
        if line[0] == "#":
            return True
        return False

    def _read_one_entry(self, fh):
        """
        reads 3 lines from the input stream, for example

        Eric Clapton
        Pretending
        283

        strip newline from each item
        """

        artist = fh.readline()[:-1]
        title = fh.readline()[:-1]
        run_time = int(fh.readline()[:-1])
        return artist, title, run_time

    def __iter__(self):
        self._pos = 0
        return self

    def __next__(self):
        if self._pos < len(self._tunes):
            self._pos += 1
            return self._tunes[self._pos - 1]
        else:
            raise StopIteration

    def __getitem__(self, item):
        if item >= len(self._tunes):
            raise IndexError
        else:
            return self._tunes[item]

    def __setitem__(self, key, value):
        if key >= len(self._tunes):
            self._tunes.extend(key + 1)
        self._tunes[key] = value

    def __len__(self):
        # zb: use @property num_tunes
        return self.num_tunes

    @property
    def num_tunes(self):
        return len(self._tunes)

    def insert_one_item(self, location, entry):
        self._tunes.insert(location, entry)
        
  


if __name__ == '__main__':
    # Sample usage
    itunes = iTunesEntryReader("itunes_file.txt")
    for tune in itunes:
        print(tune)
    print(sum(itunes))    
    