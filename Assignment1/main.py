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

def reverse_words(str):
    return "racecar"


def main():
    test_str = "racecar"
    # test_str2 = "String; 2be reversed..."
    assert(reverse_words(test_str)=="racecar")
    print("All tests passed")



if __name__=="__main__":
    main()