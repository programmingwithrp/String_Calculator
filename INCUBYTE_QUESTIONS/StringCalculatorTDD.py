import re


class StringCalculator:
    def add(self, String):
        try:
            # If string is blank
            if String == "":
                return 0
            else:

                #For  Handle for new delimiter and Even Odd Conditions
                if '//' in String:
                    # If new delimiter is given
                    if String.startswith('//'):
                        findSlashN = String.find("\n")
                        find_delimiter_string = String[2:findSlashN]
                        if len(find_delimiter_string) != 1:

                            # Remove brackets from the big delimiter string like [$$$] => $$$
                            delimiter = find_delimiter_string[1:len(find_delimiter_string)-1]
                        else:
                            delimiter = find_delimiter_string
                        New_String = String[findSlashN+1:]

                        # split by comma (,) and new line character (\n), and also with new delimiter
                        numbers_list = re.split(f"{delimiter}|,|\n", New_String)
                    
                    # If Even Odd Number is give at first
                    else:
                        New_String = String[3:]
                        if int(String[0]) == 0:
                            oddFlag = True
                        else:
                            evenFlag = True

                        # split by comma (,) and new line character (\n)
                        numbers_list = re.split(",|\n", New_String)
                else:
                    # split by comma (,) and new line character (\n)
                    numbers_list = re.split(",|\n", String)

                sum_value = 0
                oddFlag = None
                evenFlag = None
                ConditionFlag = None


                # for Even Odd Conditions 
                if oddFlag == True:
                    ConditionFlag = True
                elif evenFlag == True:
                    ConditionFlag = False
                for num in numbers_list:
                    if ConditionFlag == True:
                        ConditionFlag = False

                        # If it is alphanumeric then make it default lower and then convert it in int as per requirement
                        if num.isalpha():
                            sum_value = sum_value + ord(num.lower()) - 96
                        else:
                            if (int(num) < 0):
                                Negetive_list = [int(i) for i in numbers_list if not i.isalpha() and int(i) < 0]

                                # it throws Exception if Negatives values there....
                                raise Exception(f"Negatives not allowed := {Negetive_list}")

                            # It check the num is Bigger than 1000 then pass Element
                            if int(num) >= 1000:
                                continue
                            sum_value = sum_value + int(num)
                    elif ConditionFlag == False:
                        ConditionFlag = True
                    elif ConditionFlag == None:

                        # If it is alphanumeric then make it default lower and then convert it in int as per requirement
                        if num.isalpha():
                            sum_value = sum_value + (ord(num.lower()) - 96)
                        else:
                            if (int(num) < 0):
                                Negetive_list = [int(i) for i in numbers_list if not i.isalpha() and int(i) < 0]

                                # it throws Exception if Negatives values there....
                                raise Exception(f"Negatives not allowed  := {Negetive_list}")
                            
                            # It check the num is Bigger than 1000 then pass Element
                            elif int(num) > 1000:
                                continue
                            
                            else:
                                sum_value = sum_value + int(num)


                return sum_value
        except Exception as e:
            # It shows Exception if any input have negative values
            return (e)

scobject  = StringCalculator()

user_input = input()
scobject.add(user_input)
