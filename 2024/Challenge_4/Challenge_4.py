for part in [1,2, 3]:
    with open(f"Input_{part}", 'r') as _file:
        _lines = _file.readlines()

        _nails = [int(nail) for nail in _lines]

    if part == 3:
        target_height = sorted(_nails)[int(len(_nails)/2)] #i.e. the median
    else:
        target_height = min(_nails)

    required_strikes = sum([abs(nail_height - target_height) for nail_height in _nails])


    print(f"Part {part}: {required_strikes}", end="\n\n\n")