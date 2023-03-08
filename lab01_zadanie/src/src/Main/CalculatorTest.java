package src.Main;

import org.junit.Test;
import static org.junit.Assert.*;

public class CalculatorTest {

    @Test
    public void testAddition() {
        Calculator calculator = new Calculator(2.5,3.5);
        double result = calculator.add(calculator.getNum1(), calculator.getNum2());
        assertEquals(6.0, result, 0.0001);
    }

    @Test
    public void testSubtraction() {
        Calculator calculator = new Calculator(5.5, 3.5);
        double result = calculator.subtract(calculator.getNum1(), calculator.getNum2());
        assertEquals(2.0, result, 0.0001);
    }

    @Test
    public void testMultiplication() {
        Calculator calculator = new Calculator(2.5, 3.5);
        double result = calculator.multiply(calculator.getNum1(), calculator.getNum2());
        assertEquals(8.75, result, 0.0001);
    }

    @Test
    public void testDivision() {
        Calculator calculator = new Calculator(10.0, 2.0);
        double result = calculator.divide(calculator.getNum1(), calculator.getNum2());
        assertEquals(5.0, result, 0.0001);
    }

    @Test (expected = IllegalArgumentException.class)
    public void testDivideByZero() {
        Calculator calculator = new Calculator(10.0, 0.0);
        calculator.divide(calculator.getNum1(), calculator.getNum2());
    }

    @Test
    public void testAdditionWithNegativeNumbers() {
        Calculator calculator = new Calculator(-2.5, -3.5);
        double result = calculator.add(calculator.getNum1(), calculator.getNum2());
        assertEquals(-6.0, result, 0.0001);
    }

    @Test
    public void testSubtractionWithNegativeNumbers() {
        Calculator calculator = new Calculator(-5.5, -3.5);
        double result = calculator.subtract(calculator.getNum1(), calculator.getNum2());
        assertEquals(-2.0, result, 0.0001);
    }

    @Test
    public void testMultiplicationWithNegativeNumbers() {
        Calculator calculator = new Calculator(-2.5, 3.5);
        double result = calculator.multiply(calculator.getNum1(), calculator.getNum2());
        assertEquals(-8.75, result, 0.0001);
    }

    @Test
    public void testDivisionWithNegativeNumbers() {
        Calculator calculator = new Calculator(-10.0, 2.0);
        double result = calculator.divide(calculator.getNum1(), calculator.getNum2());
        assertEquals(-5.0, result, 0.0001);
    }

    @Test
    public void testAdditionWithZero() {
        Calculator calculator = new Calculator(0.0, 3.5);
        double result = calculator.add(calculator.getNum1(), calculator.getNum2());
        assertEquals(3.5, result, 0.0001);
    }
}
