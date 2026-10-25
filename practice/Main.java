// public class Main{
 
//     public static void main(String[] args){
//         int age = 23;

//         if (age <= 12){
//             System.out.println("Child");
//         }else if (age <= 19){
//             System.out.println("Teenager");
//         }else{
//             System.out.println("Adult");
//         }
//     }
// }

// public class Main{
//     public static void main(String[] args) {
//         for(int i = 1; i <= 10; i++){
//             System.out.println(i);
//         }
//     }
// }

// public class Main{

//     static String name = "Shahabuddin";
//     public static void main(String[] args) {
//         greet(name);
//     }

//     public static void greet(String name){
//         System.out.println("Hello " + name);
//     }
// }


// public class Main{

//     public static void main(String[] args) {
//        System.out.println(multiply(2, 4));
//     }

//      public static  int multiply(int a, int b){
//         return a * b;
//     }
    
// }

// public class Main{

//     public static void main(String[] args) {
//         String[] friends = {"Hamza", "Shahab", "usman", "Ali","usman"};

//        for(int i = 0; i < friends.length; i++){
//             System.out.println(friends[i]);
//        }
//     }

     
    
// }


// import java.util.ArrayList;

// public class Main{

//     public static void main(String[] args){
//         ArrayList<String> friends = new ArrayList<>();

//         friends.add("Hamzah");
//         friends.add("shahab");
//         friends.add("usman");
//         friends.add("Ali");
//         friends.add("Ahmed");

//         System.out.println(friends.get(2));

//         friends.remove(3);
        
//             for (int i  = 0; i < friends.size(); i++){
//                 System.out.println(friends.get(i));
//                 }
//     }
            

// }



// class Student {
//     String name;
//     int age;
//     String email;
// }

// public class Main{
//     public static void main(String[] args) {
//         Student student1 = new Student();

//         student1.name = "shahab";
//         student1.age = 22;
//         student1.email = "shahab@gmail.com";

//         System.out.println(student1.name);
//         System.out.println(student1.age);
//         System.out.println(student1.email);

//     }

// }


class Student {
    String name;
    int age;
    String email;

    Student(String name, int age, String email){
        this.name = name;
        this.age = age;
        this.email = email;
    }

}

public class Main{

    String name;
    int age;
    String email;

    public  static void main(String[] args){

        Student student1 =  new Student("Shahab",22,"voyager@gmail.com");

        System.out.println(student1.name);
        System.out.println(student1.age);
        System.out.println(student1.email);
        System.out.println(student1);
        
    }
    

}


