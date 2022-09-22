
package cs284;
import java.util.ArrayList;
import java.util.EmptyStackException;
public class StackSLL<E>  {
	// Data fields
	private SingleLL<E> stack;
	// Constructor
	StackSLL() {
		stack = new SingleLL<E>();
	}
	// Methods
	public E push(E item) {
		stack.addFirst(item);
		return item;
	}
	public E pop() {
		if (stack.isEmpty()) {
			throw new EmptyStackException();
		}
		return stack.removeFirst();
	}
	public E peek() {
		if (stack.isEmpty()) {
			throw new EmptyStackException();
		}
		return stack.get(0);
	}
	public boolean empty() {
		return stack.isEmpty();
	}
	public int size() {
		return stack.size();
	}
	public String toString() {
		return stack.toString();
	}
	public static ArrayList<Integer> toBinary(int i){
		StackSLL<Integer> stack = new StackSLL<>();
		int power = 0;
		while(Math.pow(2, power+1)<=i) {
			power++;
		}
		for(int index = 0; index<=power; index++) {
			if(Math.pow(2, power-index)<=i) {
				stack.push(1);
				i-=Math.pow(2,power-index);
			}
			else {
				stack.push(0);
			}
		}
		ArrayList<Integer> binary = new ArrayList<>();
		while(!stack.empty()) {
			binary.add(0,stack.pop());
		}
		return binary;
	}
	public static void main(String[] args) {
		System.out.println(toBinary(1));
		
	}
}