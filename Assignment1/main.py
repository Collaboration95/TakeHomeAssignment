### Guruprasath Gopal guruprsath3200@gmail.com

# Assignment 1
# // PROBLEM DEFINITION
# // ------------------
# // Reverse each word in the input string.
# // The order of the words will be unchanged.
# // A word is made up of letters and/or numbers.
# // Other characters (spaces, punctuation) will not be reversed.
# // NOTES
# // ------
# // Write production quality code
# // We prefer clarity over performance (though if you can achieve both - great!)
# // You can use the language that best highlights your programming ability
# // the template below is in C++
# // A working solution is preferred (assert in main() should succeed)
# // Bonus points for good tests
# #include <string>
# #include <cassert>
# std::string reverse_words(const std::string &str)
# {
# // TODO: Implement this function
# return "???";
# }
# int main()
# {
# std::string test_str = "String; 2be reversed...";
# assert(reverse_words(test_str) == "gnirtS; eb2 desrever...");
# return 0;
# }

def h_reverse_word(input_list:list, left:int, right:int)->list:
    # Helper function to reverse specific substring in workd/ list
    # create copy to avoid side effects ie pure function
    result = input_list.copy() 
    while left < right:
        result[left], result[right] = result[right], result[left]
        left+=1
        right-=1
    return result

def reverse_words(input_str:str)->str:
    # 2p approach , modify in plac e
    # convert string to list ( to simplify helper function 
    #if character is alnum track until it is not then reverse the substring from left , right-1 ( right is not alnum character)
    #convert to string at end 
    left = 0
    input_list = list(input_str)
    length_of_input_list = len(input_list)
    while left < length_of_input_list:
        if not input_list[left].isalnum():
            left+=1
            continue
        
        right = left 
        while right < length_of_input_list and input_list[right].isalnum():
            right+=1
        
        input_list = h_reverse_word(input_list, left, right-1)
        left = right
    return ''.join(input_list)

def main():
    # Original test cases
    test_str = "racecar"
    test_str2 = "String; 2be reversed..."
    assert(reverse_words(test_str)=="racecar")
    assert(reverse_words(test_str2)=="gnirtS; eb2 desrever...")    
    assert(reverse_words("") == "")
    assert(reverse_words("   ") == "   ")
    assert(reverse_words("\t\n ") == "\t\n ")
    assert(reverse_words("!@#$%") == "!@#$%")
    assert(reverse_words("a") == "a")
    assert(reverse_words("1") == "1")
    assert(reverse_words("hello world") == "olleh dlrow")
    assert(reverse_words("abc123!def") == "321cba!fed")
    assert(reverse_words("a!b") == "a!b")
    assert(reverse_words("123 456") == "321 654")
    assert(reverse_words("Hello World") == "olleH dlroW")
    assert(reverse_words("!hello") == "!olleh")
    assert(reverse_words("hello!") == "olleh!")

    # Consecutive punctuation
    assert(reverse_words("hello!!world") == "olleh!!dlrow")

    # Multiple spaces
    assert(reverse_words("hello   world") == "olleh   dlrow")

    # Mixed case and numbers
    assert(reverse_words("Test123!Case456") == "321tseT!654esaC")

    print("All tests passed")



if __name__=="__main__":
    main()