
def parseCmdArgs(cmd_args):
    """
    Parse command line arguments
    """
    splitted_args = cmd_args.split()
    command = {}
    command["args_count"] = len(splitted_args)
    command["class_name"] = None
    command["id"] = None

    if len(splitted_args) >= 1:
        command["class_name"] = splitted_args[0]
    if len(splitted_args) >= 2:
        command["id"] = splitted_args[1]

    return command
