package cs284;

import java.util.Arrays;

public class Sort<E> {
	public static int[] merge(int[] a, int[] b){
		int[] result = new int[a.length + b.length];
		int indexA = 0;
		int indexB = 0;
		int indexR = 0;
		while(indexA<a.length || indexB<b.length) {
			if(indexB>=b.length || (indexA<a.length && a[indexA]<b[indexB]) ) {
				result[indexR] = a[indexA];
				indexA++;
			}
			else {
				result[indexR] = b[indexB];
				indexB++;
			}
			indexR++;
		}
		
		return result;
	}
	public static int[] mergeSort(int[] a) {
		return mergeSort(Arrays.copyOf(a, a.length/2), Arrays.copyOfRange(a, a.length/2, a.length));
	}
	private static int[] mergeSort(int[] a, int[] b) {
		if(a.length <= 1 && b.length <= 1) return merge(a,b);
		else {
			return merge(mergeSort(Arrays.copyOf(a, a.length/2), Arrays.copyOfRange(a, a.length/2, a.length)),
					mergeSort(Arrays.copyOf(b,b.length/2), Arrays.copyOfRange(b, b.length/2, b.length)));
		}
	}
	private static void swap(int[] array, int a, int b) {
		
		int temp = array[a];
		array[a] = array[b];
		array[b] = temp;
	}
	private static int[] quickSort(int[] a, int bottom, int top) {
		if(bottom<top) {
			int pivot = a[bottom];
			int pivotIndex = bottom;
			int origTop = top;
			int origBot = bottom;
			bottom++;
				System.out.println(bottom+":"+top);
				do {
					//System.out.println(bottom);
					if(bottom<top && a[bottom]<pivot) bottom++;
					else if (a[top]>pivot) top--;
					else {
						swap(a, bottom, top);
					}
				}while(bottom<top);
				swap(a, pivotIndex, bottom-1);
				pivotIndex = bottom-1;
				
				a = quickSort(a, origBot, pivotIndex-1);
				a = quickSort(a, pivotIndex+1, origTop);
		}
		return a;
	}
	public static int[] quickSort(int[] a) {
		
		return quickSort(a, 0, a.length-1);
	}
	public static <E extends Comparable<E>> void qs(E[] a) {
		qs(a, 0, a.length - 1);
	}
	private static <E extends Comparable<E>> void qs(E[] a, int first, int last) {
		if (first < last) { // There is data to be sorted.
			int pivIndex = partitionb(a, first, last);
			qs(a, first, pivIndex - 1);
			qs(a, pivIndex + 1, last);
		}
	}
	private static <E extends Comparable<E>> int partition(E[] a, int first, int last) {
		int pivotIndex = first;
		do {
			while(first<last && a[first].compareTo(a[pivotIndex]) <= 0) first++;
			while(a[last].compareTo(a[pivotIndex]) > 0 )last--;
			if(last>first) {
				E temp = a[first];
				a[first] = a[last];
				a[last] = temp;
			}
		}while(first<last);
		E temp = a[pivotIndex];
		a[pivotIndex] = a[last];
		a[last] = temp;
		
		return last;
		
	}
	public static <E extends Comparable<E>> int partitionb(E[] a, int first, int last) { 
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
		// TODO Auto-generated method stub
		int[] first = {50,60,90,30};
		int[] second = {45,20,80,15,33};
		int[] merged = mergeSort(first, second);
		System.out.println(Arrays.toString(merged));
		Integer[] test = {10,7,19,22,30,2,4,5};
		qs(test);
		System.out.println(Arrays.toString(test));
		int[] single = {6};

	}

}
