from source.behave.research import Research

def before_all(context):
    context.research = Research()