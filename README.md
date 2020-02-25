# Assignment-2
# Blockchain & Applications

**About my code**

My code is a program that breaks SHA1 hashes using brute force. The code imported three libraries *time*, *urlopen* and *hashlib*. The *time* library shows the actual time to break the hash. The *urlopen* library is used to open a list of common passwords online. The *hashlib* library is used to get the hashing algorithm SHA1. The program requires user to input a string as the hash value of a password. After that, the program shows numbers of tries before reaching the correct password. 

**Instructions**
  1. Download the Assignment2.py file
  2. Run the content on any Python IDE
  
**Output Answers**
  a.  * b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
      * Found Hash
      * Number of tries: 16
      * The password is  letmein
      * Total running time: 2.6682496070861816

  b.  * 801cdea58224c921c21fd2b183ff28ffa910ce31
      * Found Hash
      * Number of tries: 999968
      * The password is  vjhtrhsvdctcegth
      * Total running time: 4.844195365905762 
     
  c.  * f0744d60dd500c92c0d37c16174cc58d3c4bdd8e ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
      * Found Hash
      * Number of tries: 217
      * The password is  slayer
      * Total running time: 11.550734519958496

**Bonus Question Idea**
      I could hash all the passwords and sort all the values in dictionary order (A-z)(0-9). When I get the input from the user, I can thus save time not going through every value one by one, but compare the input value with the middle element of the list and decide to go lower or higher that the middle element (applying divide and conquer, binary search). By doing that I could reduce the running time of my program. 
  
