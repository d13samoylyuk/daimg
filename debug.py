DEBUG_COUNT = 1
Debug = True


def DebugPrint(*args, **kwargs):
    global DEBUG_COUNT
    
    if Debug:
        print(DEBUG_COUNT, *args, **kwargs)
        DEBUG_COUNT += 1