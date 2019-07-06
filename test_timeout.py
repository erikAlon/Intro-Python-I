from threading import Thread


class Input:
    _response = None  # internal use only

    @classmethod
    def timeout(cls, message, timeout):
        cls._response = None
        print('You have {0} seconds to answer'.format(timeout))
        thread = Thread(target=cls.do_input, args=(message,))
        thread.start()
        # wait for a response
        thread.join(timeout)
        # closing input after timeout
        if cls._response is None:
            print('\nTimes up. Press enter to continue')
            thread.join()
            # clear response from enter key
            cls._response = None
        return cls._response

    @classmethod
    def do_input(cls, message):
        cls._response = input(message)


def main():
    r = Input.timeout('Type anything >> ', 2)
    print(r)
    r = Input.timeout('Type anything >> ', 3)
    print(r)


main()
