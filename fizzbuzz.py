
#Uppgiften går ut på att skriva ut alla tal mellan 1 och 100, ett tal per rad.

#Om talet är jämnt delbart med 3 så ska ordet “Fizz” skrivas ut istället för talet.

#Om talet är jämnt delbart med 5 så ska ordet “Buzz” skrivas ut istället för talet.

#Om talet är jämnt delbart med både 3 och 5 så ska ordet “Fizzbuzz” skrivas ut istället för någonting annat.

def main():
    for i in range (1,101):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)

if __name__ == "__main__":
    main()
