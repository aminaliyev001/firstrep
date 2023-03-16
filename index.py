# Who wanto be millionaire game in terminal
import random
import os
import time
questions = [["What is the capital of France?", ["Paris", "Rome", "London", "Berlin"],"Paris"],["What is the capital of Germany?", ["Paris", "Berlin", "London", "Rome"],"Berlin"],["What is the capital of Italy?", ["Paris", "Rome", "London", "Berlin"],"Rome"],["What is the capital of Spain?", ["Paris", "Madrid", "London", "Berlin"],"Madrid"],["What is the capital of United Kingdom?", ["Paris", "Rome", "London", "Berlin"],"London"],["What is the capital of Japan?", ["Tokyo", "Rome", "London", "Berlin"],"Tokyo"],["What is the capital of Russia?", ["Paris", "Moscow", "London", "Berlin"],"Moscow"],["What is the capital of Australia?", ["Paris", "Rome", "Canberra", "Berlin"],"Canberra"],["What is the capital of Canada?", ["Paris", "Ottawa", "London", "Berlin"],"Ottawa"],["What is the capital of China?", ["Paris", "Beijing", "London", "Berlin"],"Beijing"],["What is the capital of India?", ["Paris", "New Delhi", "London", "Berlin"],"New Delhi"],["What is the capital of USA?", ["Paris", "Washington D.C.", "London", "Berlin"],"Washington D.C."],["What is the capital of Brazil?", ["Paris", "Brasília", "London", "Berlin"],"Brasília"],["What is the capital of Argentina?", ["Paris", "Buenos Aires", "London", "Berlin"],"Buenos Aires"],["What is the capital of South Africa?", ["Paris", "Pretoria", "London", "Cape Town"],"Cape Town"] ]
prizes = ["100","200","300","500","1000","2000","4000","8000","16000","25000","50000","100000","250000","500000","1000000"]
help_chances = ["Call to your friend","Get the voting of audience","Get canceled of 2 options"]
current_question = 0
current_money = 0
checkPoint_money = 0 
len_of_questions = len(prizes)
# Functions AMIN
def final_answer_user():
    while True:
            print()
            inputuser = input("Enter your final answer: ")
            inputuser.strip()
            if inputuser.lower() == "a" or inputuser.lower() == "b" or inputuser.lower() == "c" or inputuser.lower() == "d":
                if inputuser.lower() == correct_variant_letter.lower():
                    return True
                else:
                    return False
def checkPointPrize():
    # getting the checkpoint prize when user loses
    print(f"Congratulations :) You could answer to {current_question} questions and got the prize of last checkpoint {checkPoint_money}$.")
def finishTheGame():
    # getting current money of user when completes the game or does not want to continue
    print(f"Congratulations :) You could answer to {current_question+1} questions and got the prize of {current_money}$.")
def endofquestion_clean():
    os.system('cls||clear')
def shuffle_all_options():
    #shuffle the options of the questions
    for a in questions:
        random.shuffle(a[1])
def askForNextQ():
    # ask from user if user is want to pass to the next question or not
    while True:
        inputask = input(f"Are you sure to continue to next question? You have {current_money}$ right now. Press Y to continue or N to finish the game: ")
        if inputask == "y" or inputask == "Y":
            return True
        elif inputask == "n" or inputask == "N":
            return False
def check_checkpoint():
    # check every question passed if passed reached the checkpoint mention it
    global current_money
    global checkPoint_money
    if current_question == 4:
        print("$$$$$$$$$$$$$$$$$")
        print("CONGRATS! You reached checkpoint. You have won 1000$")
        print("$$$$$$$$$$$$$$$$$")
        current_money = 1000
        checkPoint_money = 1000
    elif current_question == 9:
        print("$$$$$$$$$$$$$$$$$")
        print("Checkpoint reached! You have won 25000$")
        print("$$$$$$$$$$$$$$$$$")
        current_money = 25000
        current_money = 25000
def displayQuestion(question):
    #display the question
    question_price = f'Prize for this question: {prizes[current_question]}$'
    result = f'{question[0]}\t\t\t{question_price} \t\t Q: {current_question+1}'
    return result
def answerMenu(chances):
    #display the answer menu
    global list_of_menuOptions
    for count,a in enumerate(chances):
        inside_option = ""
        inside_option+=f"{count}. "
        inside_option+=a
        print(inside_option)
        list_of_menuOptions.append(inside_option)
def help_user(option,correct):
    help_chances.remove(option)
    if option == "Call to your friend":
        probability = random.randint(0,100)
        print("Calling to your friend ...")
        time.sleep(5)
        print("His answer is: ....",end=" ")
        time.sleep(4)
        if probability < 70:
            print(correct)
        else:
            list_of_menuOptions.remove(correct)
            answer_of_friend = list_of_menuOptions[random.randint(0,2)]
            print(answer_of_friend)
        return final_answer_user()    
    elif option == "Get the voting of audience":
        total_percent = 100
        audicence_a = random.randint(0,20)
        total_percent -= audicence_a
        audicence_b = random.randint(0,15)
        total_percent -= audicence_b
        audicence_c = random.randint(0,14)
        total_percent -= audicence_c
        audicence_d = total_percent
        wrong_option = [audicence_a,audicence_b,audicence_c]
        print("Claiming the voting results..")
        time.sleep(5)
        for p in list_of_menuOptions:
            if p[0].isalpha():
                if correct in p:
                    print(f'''
    Audience voted for {p[0]}: {audicence_d}% ''',end="")
                else:
                    print(f'''
    Audience voted for {p[0]}: {wrong_option[0]}% ''',end="")
                    wrong_option.pop(0)
        return final_answer_user()
    elif option == "Get canceled of 2 options":
        print("Cancelling two options ...")
        time.sleep(3)
        coun = 0
        for b in list_of_menuOptions:
            if b[0].isalpha() and b[0] != correct_variant_letter and coun == 0:
                print(f''' 
    {b}
                ''',end="")
                coun+=1
            elif b[0] == correct_variant_letter:
                print(f'''
    {b}
                ''',end="")
        return final_answer_user()
def answerTheQuestion(option,correct_a):
    #returning True if the given answer from user is correcet
    access_to_1 = False
    for x in list_of_menuOptions:
        if option[0].lower() in x[0].lower():
            chosen_one = x[0].lower()
            chosen_option = x
            access_to_1 = True
    if access_to_1:
        if chosen_one.isalpha():
            if chosen_option[3:] == correct_a:
                return True
            else:
                return False
        elif chosen_one.isnumeric():
            return help_user(chosen_option[3:],correct_a)
def option_syntax(user_ans):
    syntax_p = True
    for a in list_of_menuOptions:
        if user_ans.lower() in a[0].lower():
            syntax_p = False
    return syntax_p
def getuser_answer():
    user_answer = input("Enter your answer: ")
    user_answer = user_answer.strip()
    if option_syntax(user_answer) == False:
        return user_answer
    else:
        getuser_answer()
##############
random.shuffle(questions)
shuffle_all_options()
while current_question < len_of_questions:
    option_alphabet = ["A","B","C","D"]
    list_of_menuOptions = []
    question = questions[current_question]
    print(displayQuestion(question))
    options_list = question[1]
    correct_answer = question[2]
    for a in range(0,len(question[1])):
        if question[1][0] == correct_answer:
            correct_variant_letter = option_alphabet[0]
        option_rand_variants = str(option_alphabet[0])+") "+str(question[1][0])
        option_alphabet.pop(0)
        question[1].pop(0)
        print(option_rand_variants)
        list_of_menuOptions.append(option_rand_variants)
    answerMenu(help_chances)        
    result_after_answer = answerTheQuestion(getuser_answer(),correct_answer)
    if result_after_answer:
        print("You got it True. Let's pass to the next one ...")
        current_money = prizes[current_question]
        check_checkpoint()
    else:
        print(":(( Unfortunately wrong answer")
        checkPointPrize()
        break
    if current_question ==  len_of_questions-1:
        finishTheGame()
        break
    PasstonextOne = askForNextQ()
    if PasstonextOne == False:
        finishTheGame()
        break
    endofquestion_clean()
    current_question+=1