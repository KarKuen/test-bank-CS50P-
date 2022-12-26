def main():
    greeting = input('Greeting: ').strip().lower()
    greeting = greeting.split()[0]
    print(f'${str(value(greeting))}')

def value(greeting):
    if 'hello' in greeting:
        return(0)
    elif greeting[0] == 'h':
        return(20)
    else:
        return(100)

if __name__ == '__main__':
    main()
