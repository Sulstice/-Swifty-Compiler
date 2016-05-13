 # **Introduction**

Swifty is a ratio of python, swift and java implementation using the parsing tools of lex and yacc. Here are a few highlights:

  - Swifty can demonstrate closure functionality with each function taking in a set of parameters and returning a type. Functions can also contain functions with functions that serve as methods to that particular function. For example:
  
                func main() -> Bool {
                          let a = 5;
                          let b = 6;
                          func anotherFunction(a, b) -> Int {
                                    return a + b
                          }
                          print (anotherFunction(a, b))
                }
                Output: 11
                
  - Swifty can also implement java classes using the intepreter Jython(2.7) to perform easy use functions. The user has the option to run pipe commands in either python or java but with out implementation the user only has to define a method in the java class and call it in Swifty to run. For Example:
  
                **Java Syntax**

                public class Stream {
                          public static void streamOperation(List<Integer> number) {
                                    number.stream()
                                              .sorted()
                                              .map(n -> n+2)
                                              .forEach(n -> System.out.print(n.toString() + ", "));
                           }
                }
                
                **Swifty Command**

                func main() -> List {
                          list a = [5, 4, 6]
                          a | stream();
                          return a
                }
                Output: [6, 7, 8]


  - Swift also allows for user List Comprehension statements. For now the only implementation is filter used to filter lists in way that if the statement of INTEGER % != INTEGER it removes it from the list. This was implemented using python lambda expressions.
  
                func main() -> int {
	                      let a = Array(0 -< 10) | filter{<0> % 2 == 0}

                }
                Output: [0, 2, 4, 6, 8]

 -Swifty is still in process of being developed and was written in 1 week, so there is a lot of work to be done in the improvement of the language. Functions that are up and coming are ability for the user to write their own lambda expressions and print statements.
 
 
- [x] Implementation of Swift Hierachy; Declarations, Statements, Functions
- [x] Ability to use Java Classes within the language and open for edits
- [x] Ability to use List Comprehension statements from a built in Library developed by us
- [x] Generates AST trees for easy access into following the hierachy of the code
- [ ] Needs an Eval Function in the lis.py file to implment environments for the closure statements to work
- [ ] Basic Programming Language functionality and syntax implementation

**Team:**
@github/dmnelsonrr

**Acknowledgements:**
@github/Pcannata
