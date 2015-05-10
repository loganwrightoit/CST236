import getpass
import random
import socket
import subprocess
import threading
import time
import math

seq_finder = None
fact_finder = None
num_counter = None
num_opp_counter = None

def feet_to_miles(feet):
    return "{0} miles".format(float(feet) / 5280)

def hal_20():
    return "I'm afraid I can't do that {0}".format(getpass.getuser())

def get_git_branch():
    try:
        process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_git_url():
    try:
        process = subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_other_users():
    try:
        host = '192.168.64.3'
        port = 1337

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send('Who?')
        data = s.recv(255)
        s.close()
        return data.split('$')

    except:
        return "IT'S A TRAAAPPPP"


class FibSeqFinder(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(FibSeqFinder, self).__init__(*args, **kwargs)
        self.sequence = [0, 1]
        self._stop = threading.Event()
        self.num_indexes = 0

    def stop(self):
        self._stop.set()

    def run(self):
        self.num_indexes = 0
        while not self._stop.isSet() and self.num_indexes < 1000:
            self.sequence.append(self.sequence[-1] + self.sequence[-2])
            self.num_indexes += 1
            time.sleep(.04)

def get_fibonacci_seq(index):
    index = int(index)
    global seq_finder
    if seq_finder is None:
        
        seq_finder = FibSeqFinder()
        seq_finder.start()

    if index > seq_finder.num_indexes:
        value = random.randint(0, 9)
        if value >= 4:
            return "Thinking..."
        elif value > 1:
            return "One second"
        else:
            return "cool your jets"
    else:
        return seq_finder.sequence[index]

class FactSeqFinder(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(FactSeqFinder, self).__init__(*args, **kwargs)
        self.sequence = []
        self._stop = threading.Event()
        self.num_indexes = 0

    def stop(self):
        self._stop.set()

    def run(self):
        while not self._stop.isSet() and self.num_indexes < 100:
            self.sequence.append(math.factorial(self.num_indexes))
            time.sleep(.2)
            self.num_indexes += 1

def get_factorial_seq(index):
    index = int(index)
    global fact_finder
    if fact_finder is None:
        fact_finder = FactSeqFinder()
        fact_finder.start()
    return fact_finder.sequence[index]
    
class IndexIncrementer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(IndexIncrementer, self).__init__(*args, **kwargs)
        self._stop = threading.Event()
        self.count = 0

    def stop(self):
        self._stop.set()

    def run(self):
        while not self._stop.isSet():
            self.count += 1
            time.sleep(0.1)

def get_number_count():
    global num_counter
    if num_counter is None:
        num_counter = IndexIncrementer()
        num_counter.start()
    return num_counter.count

class IndexDecrementer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(IndexDecrementer, self).__init__(*args, **kwargs)
        self._stop = threading.Event()
        self.count = 0

    def stop(self):
        self._stop.set()

    def run(self):
        while not self._stop.isSet():
            self.count -= 1
            time.sleep(0.1)    
    
def get_opposite_number_count():
    global num_opp_counter
    if num_opp_counter is None:
        num_opp_counter = IndexDecrementer()
        num_opp_counter.start()
    return num_opp_counter.count
    
def get_root_info(index):
    return os.listdir('.')