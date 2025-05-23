def get_answer(number: int):

    def _helper(current_str: str):
        if len(current_str) == number:
            print(current_str)
            return

        if 1 < int(current_str[-1]) < 9:
            _helper(current_str+(str(int(current_str[-1])+1)))
            _helper(current_str+(str(int(current_str[-1])-1)))

    for i in range(1, 10):
        _helper(f"{i}")