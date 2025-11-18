def create_user(name, **info):
    d1={'name': name}
    d1.update(info)
    return d1

def main():
    print(create_user(name="mariusz",wiek="30",zawod="piekarz"))

if __name__ == '__main__':
    main()