package src.Main;

public class Calculator {
    private final double num1;
    private final double num2;

    public Calculator(double num1, double num2) {
        this.num1 = num1;
        this.num2 = num2;
    }

    public double getNum1() {
        return num1;
    }

    public double getNum2() {
        return num2;
    }

    public double add(double num1, double num2) {
        return num1 + num2;
    }

    public double subtract(double num1,double num2) {
        return num1 - num2;
    }

    public double multiply(double num1,double num2) {
        return num1 * num2;
    }

    public double divide(double num1,double num2) {
        if (num2 == 0) {
            throw new IllegalArgumentException("Cannot divide by zero.");
        }
        return num1 / num2;
    }
}
