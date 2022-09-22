package cs284;
/**
 * Quiz 2
 * 2/13/2019
 * I pledge my honor that I have abided by the Stevens Honor System
 * CS 284-B
 * @author Max Shi
 *
 */
public class complexity {
	public static void method1(int n) {
		int counter = 0;
		for(int i = 0; i<n; i++) {
			for(int j = 0; j<n; j++) {
				System.out.println("Operation " + counter);
				counter++;
			}
		}
	}
	public static void method2(int n) {
		int counter = 0;
		for(int i = 0; i<n; i++) {
			for(int j = 0;j<n; j++) {
				for(int k = 0; k<n; k++) {
					System.out.println("Operation " + counter);
					counter++;
				}
			}
		}
	}
	public static void method3(int n) {
		int counter = 0; 
		for(int i = 1; i<n; i*=2) {
			System.out.println("Operation " + counter);
			counter++;
		}
	}
	public static void method4(int n) {
		int counter = 0;
		for(int i = 0; i<n; i++) {
			for(int j = 1; j<n; j*=2) {
				System.out.println("Operation " + counter);
				counter++;
			}
		}
	}
	public static void method5(int n) {
		int counter = 0;
		for(long i = 2; i<n; i*=i) {
			System.out.println("Operation " + counter);
			counter++;
		}
	}
	public static int sixcounter = 0;
	private static void expAlgo(int n) {
		for(int i = 0; i<n; i++) {
			System.out.println("Operation " + sixcounter);
			sixcounter++;
			if(n>0) expAlgo(n-1);
		}
	}
	public static void method6(int n) {
		sixcounter = 0;
		expAlgo(n);
	}
	
}
