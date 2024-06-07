import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyA7dtVBKkqzZF7aHcSpt9hBtxxqC4htOmQ"

# user_text1 = """
# Give me the sentiment of this sentence:
# "I hate this movie"
# """

# user_text2 = """
# Give me hindi translation of this sentence:
# "I hate this movie"
# """

# user_text3 = """
# Detect the language of this sentence:
# "I hate this movie"
# """

# genai.configure(api_key = GOOGLE_API_KEY)
# model = genai.GenerativeModel("gemini-pro")

# response = model.generate_content(user_text3)
# results = response.text
# print(results)

class NLPModel:
    def get_model(self):
        genai.configure(api_key = GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-pro")
        
        return model
        

class NLPApp(NLPModel):
    def __init__(self):
        self.__database = {}
        self.__first_menu()
        
    def __first_menu(self):
        first_input = input("""
                            Hi! How would you like to proceed?
                            
                            1. Not a member? Register
                            2. Already a member? Login
                            3. Bhai galti se aa gaya kya? Exit
                            
                            """)
        
        if first_input == '1':
            #register
            self.__register()
        
        elif first_input == '2':
            self.__login()
        
        else:
            exit()
            
            
    def __register(self):
        name = input("Enter your Name: ")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")
        
        if email in self.__database:
            print("Email already exists")
        
        else:
            self.__database[email] = [name, password]
            print("Registration successful. Now you can login!")
            print(self.__database)
            self.__first_menu()
            
    def __second_menu(self):
        second_input = input("""
                            Hi! How would you like to proceed?
                            
                            1. Sentiment Analysis
                            2. Language Translation
                            3. Language Detection
                            
                            """)
        
        if second_input == '1':
            self.__sentiment_analysis()
        
        elif second_input == '2':
            self.__language_translation()
        
        elif second_input == '3':
            self.__language_detection()
        
        else:
            exit()
            
    def __login(self):
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")
        
        if email in self.__database:
            if self.__database[email][1] == password:
                print("Login successful")
                self.__second_menu()
                
            else:
                print("Wrong password. Try again!!")
                self.__login()
                
        else:
            print("This email is not registered")
            self.__first_menu()
            
    def __sentiment_analysis(self):
        user_text = input("Enter your text:")
        model = super().get_model()
        response = model.generate_content(f"Give me the sentiment of this sentence: {user_text}")
        results = response.text
        print(results)
        self.__second_menu()
        
    def __language_translation(self):
        user_text = input("Enter your text:")
        model = super().get_model()
        response = model.generate_content(f"Give me hindi translation of this sentence: {user_text}")
        results = response.text
        print(results)
        self.__second_menu()
        
    def __language_detection(self):
        user_text = input("Enter your text:")
        model = super().get_model()
        response = model.generate_content(f"Detect the language of this sentence: {user_text}")
        results = response.text
        print(results)
        self.__second_menu()
            
            
obj = NLPApp()