import os.path
from source.behave.research import Research

def before_all(context):
    context.research = Research()
    dir = os.path.dirname(__file__)
    context.data_path = os.path.join(dir, "data.txt")
    print(context.data_path)