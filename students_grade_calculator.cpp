#include <iostream> 
using namespace std;
int main(){
    int numSubjects;
    float marks, total = 0, average;
    char grade; 

    cout << "enter your number of subjects:";
    cin >>  numSubjects;

    //take marks for each subjects loop used here
    for(int i =1; i<=  numSubjects; i++){
        cout << "enter marks for subjects " << i<< endl;
        cin >> marks;
        total+= marks; // add to  total

    }
    // now calculate average
    average = total/ numSubjects;
    // condition to find grade according to marks
    if (average >= 90)
        grade = 'A';
    else if (average >= 80)
        grade = 'B';
    else if (average >= 70)
        grade = 'C';
    else if (average >= 60)
        grade = 'D';
    else
        grade = 'F';

    //  ternery concept used to fing whether fail or pass
    string result = (average>=50)? "pass" : "fail";

    //display result

    cout << "\nTotal Marks = " << total << endl;
    cout << "Average = " << average << endl;
    cout << "Grade = " << grade << endl;
    cout << "Result = " << result << endl;

    return 0;

}
