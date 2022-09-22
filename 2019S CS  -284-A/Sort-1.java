import java.util.Arrays;
/**
 * Quiz 9 CS 284 B
 * April 24
 * I pledge my honor that I have abided by the Stevens Honor System
 * @author Max Shi and Hamzah Nizami
 *
 */
public class Sort {
	public static <E extends Comparable<E>> int partition(E[] a, int first, int last) { 
		 int pivotIndex = first;
		 boolean direction = true;
		 int compareIndex = last;
		 while (pivotIndex != compareIndex) {
			 while(direction && a[pivotIndex].compareTo(a[compareIndex]) < 0) { 
				 compareIndex--;
			 }
			 while(!direction && a[pivotIndex].compareTo(a[compareIndex]) > 0) {
				 compareIndex++;
			 }
			 if(compareIndex!=pivotIndex) {
				 direction = !direction;
				 int temp = compareIndex;
				 E tempE = a[compareIndex];
				 a[compareIndex] = a[pivotIndex];
				 a[pivotIndex] = tempE;
				 compareIndex = pivotIndex;
				 pivotIndex = temp;
			 }
		 }
		 return pivotIndex;
	}
	public static void main(String[] args) {
		Integer[] test = {5,3,2,9,10,4,7,1,11,27,0};
		
		partition(test,0,test.length-1);
		System.out.println(Arrays.toString(test));
	}
}
