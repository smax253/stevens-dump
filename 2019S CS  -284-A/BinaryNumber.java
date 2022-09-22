package hw1;
/**
 * Homework 1: BinaryNumber
 * Binary Number class using little-endian format
 * @author Max Shi
 * Class section CS 284 A
 */
public class BinaryNumber {
	private int[] data;
	private boolean overflow;
	
	/**
	 * Constructor to create a binary number 0 with given data length
	 * @param length The maximum length of the data, must be positive
	 */
	public BinaryNumber(int length){
		if(length<1) {
			throw new IllegalArgumentException();
		}
		else {
			data = new int[length];
			overflow = false;
		}
	}
	/**
	 * Constructor to create a binary number with given string data
	 * @param str The binary little-endian representation of a binary number, chars must be 1 or 0
	 */
	public BinaryNumber(String str) {
		data = new int[str.length()];
		for(int i = 0; i<str.length(); i++) {
			data[i] =  Character.getNumericValue(str.charAt(i));
			if (data[i]<0 || data[i]>1) 
				throw new IllegalArgumentException();
		}
	}
	/**
	 * Returns the number of bits that represent this binary number
	 * @return The number of bits
	 */
	public int getLength() {
		return data.length;
	}
	/**
	 * Returns the bit at the given index
	 * @param index The requested index in the data of bits, must be greater than 0 and less than length-1
	 * @return The bit at the given index
	 */
	public int getDigit(int index) {
		if(index>=0 && index<data.length)
			return data[index];
		else
			throw new IllegalArgumentException();
	}
	/**
	 * Shifts the bits to the right by adding 0's to the left of the bits
	 * @param amount The amount of 0's to add on the left, must be positive
	 */
	public void shiftR(int amount) {
		if(amount<0) throw new IllegalArgumentException();
		int[] newArr = new int[amount+data.length];
		for(int i = data.length-1; i>=0; i--){
			newArr[amount+i] = data[i];
		}
		data = newArr;
	}
	/**
	 * Adds to binary numbers and modifies the parameter object with the result
	 * @param aBinaryNumber The binary number to add to this number, must be the same length
	 */
	public void add(BinaryNumber aBinaryNumber) {
		if (this.getLength() != aBinaryNumber.getLength()) throw new IllegalArgumentException();
		else {
			int length = this.getLength();
			int carry = 0;
			for(int i = 0; i<length; i++) {
				int sum = getDigit(i)+aBinaryNumber.getDigit(i)+carry;
				aBinaryNumber.data[i] = sum%2;
				carry = sum/2;
			}
			if (carry==1) aBinaryNumber.overflow = true; 
		}
	}
	/**
	 * Returns a string representation of the binary number with 1's and 0's
	 * @return The representative string of 1's and 0's
	 */
	public String toString() {
		if(overflow) return "Overflow";
		String s = "";
		for(int digit:data) {
			s += digit;
		}
		return s;
	}
	/**
	 * Returns the decimal representation of the number
	 * @return	The base-10 representation of the binary number
	 */
	public int toDecimal() {
		int number = 0;
		for(int i = 0; i<data.length; i++) {
			number += data[i]*Math.pow(2, i);
		}
		return number;
	}
	/**
	 * Clears the overflow parameter
	 */
	public void clearOverflow() {
		overflow = false;
	}
	
}
