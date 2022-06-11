from threading import Thread


def call_with_timeout(fun, timeout, args=None):
    if args is None:
        args = []
    result = {}

    def wrapped_fun(*args):
        result['result'] = fun(*args)

    thread = Thread(target=wrapped_fun, args=args)
    thread.start()
    thread.join(timeout=timeout)
    if thread.is_alive():
        raise Exception(f"Exceeded time limit of {timeout} seconds.")
    else:
        return result['result']
