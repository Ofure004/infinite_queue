import os


def main():

    while True:
        print("Helloo")
        arrival = int(input("put in rate of arrival: "))
        service = int(input("put in rate of service: "))
        people_in_queue = float(input("how many people in the queue?: "))
        os.system("clear")
        menu()
        ans = input("Please put in your answer below: ")
        os.system('clear')
       
        rho = arrival/service
        choice(ans,rho,arrival,people_in_queue)
        

        option = input("Type 'back' to go to the main menu and 'exit' to exit: ").lower()

        if option == 'back':
            os.system('clear')
        elif option == 'exit':
            quit()
        else: 
            print("Wrong option chosen")



def exact_probability(rho,no_in_system):
    
    prob_of_people_in_system = pow(rho,no_in_system)*(1-rho)

    return prob_of_people_in_system

def at_most_probability(rho,no_in_system):
    sum = 0
    i = 0
    while(i <= no_in_system):
        sum += pow(rho,i)*(1-rho)
        i+=1
    return sum

def at_least_probability(rho, no_in_system):
    real_sum = 0
    real_sum = 1-at_most_probability(rho,no_in_system)
    return real_sum

def length_of_system(rho):
    ans = rho/(1-rho)
    return ans

def length_of_queue(rho):
     ls = rho/(1-rho)
     ans = ls - rho
     return ans

def waiting_time_system(rho, arrival):
    ls = rho/(1-rho)
    ans = ls/arrival
    return ans

def waiting_time_queue(rho, arrival):
    ls = rho/(1-rho)
    lq = ls - rho
    ans = lq/arrival
    return ans

def server_not_free(rho):
    ans = 1 - exact_probability(rho,0)
    return ans

def no_queue(rho):
    ans = exact_probability(rho,0) + exact_probability(rho,1)
    return ans



def menu():
    print("Please choose what you want to calculate")
    print("1. probability that an exact amount of people will be on the queue")
    print("2. probability that at least an amount of people will be on the queue")
    print("3. probability that at most an amount of people will be on the queue")
    print("4. The length of the queue")
    print("5. The length of the system")
    print("6. The waiting time in the queue")
    print("7. The waiting time in the system")
    print("8. The probability that the server is not free")
    print("9. The probability that there is no queue")
    print("0. exit the system")

def choice(ans, rho, arrival, number):
    match ans:
        case "1":
            answer = exact_probability(rho, number)
            print("The probability that exactly", number, "people will be on the queue is ", answer)
        case "2":
            answer = at_least_probability(rho, number)
            print("The probability that at least", number, "people will be on the queue is ", answer)
        case "3":
            answer = at_most_probability(rho, number)
            print("The probability that at most", number, "people will be on the queue is ", answer)
        case "4":
            answer = length_of_queue(rho)
            print("The length of the queue is ", answer)
        case "5":
            answer = length_of_system(rho)
            print("The length of the system is ", answer)
        case "6":
            answer = waiting_time_queue(rho, arrival)
            print("The amount of time you will have to wait on the queue is ", answer)
        case "7":
            answer = waiting_time_system(rho, arrival)
            print("The amount of time you will have to wait in the system is ", answer)
        case "8":
            answer = server_not_free(rho)
            print("The probability that the server is free is ", answer)
        case "9":
            answer = no_queue(rho)
            print("The probability that there is no queue is ", answer)
        case "0":
            quit()
        case _:
            print("No option matches your selection")
        
