import java.util.Scanner;

public class score {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of subjects: ");
        int numSubjects = scanner.nextInt();
        int totalMarks = 0;

        for (int i = 0; i < numSubjects; i++) {
            System.out.print("Enter marks for subject " + (i + 1) + ": ");
            totalMarks += scanner.nextInt();
        }

        double averagePercentage = (totalMarks / (double) numSubjects);
        String grade = getGrade(averagePercentage);

        System.out.println("Total Marks: " + totalMarks);
        System.out.println("Average Percentage: " + String.format("%.2f", averagePercentage) + "%");
        System.out.println("Grade: " + grade);
    }

    private static String getGrade(double averagePercentage) {
        if (averagePercentage >= 90) return "A";
        if (averagePercentage >= 80) return "B";
        if (averagePercentage >= 70) return "C";
        if (averagePercentage >= 60) return "D";
        return "F";
        
    }
}
