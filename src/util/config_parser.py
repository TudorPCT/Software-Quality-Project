def get_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line:
                line = line.strip().split("=")
                assert len(line) == 2
                data[line[0]] = int(line[1])
    return data
