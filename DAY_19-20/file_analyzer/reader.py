def file_reader(file_name: str):
    try:
        with open(file_name,'r',encoding='utf-8') as f:
            context = f.readlines()

        return context

    except FileNotFoundError:
        print("No file found")