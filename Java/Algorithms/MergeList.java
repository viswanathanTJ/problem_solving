import java.io.*;
import java.util.*;
class MergeList{
	public static final Scanner sn = new Scanner(System.in);
	public static final Random rn = new Random();
	public static class node{
		node next;
		int data;
		node(int data){
			this.data = data;
			next = null;
		}
	}
	public static node insert(node head, int data){
		node newnode = new node(data);
		if( head == null ){
			return newnode;
		}else{
			node cur = head;
			while ( cur.next != null ) {
				cur = cur.next;
			}
			cur.next = newnode;
		}
		return head;
	}
	public static void printList(node head){
		if( head != null ){
			node cur = head;
			while ( cur != null ) {
				System.out.print(cur.data+"->");
				cur = cur.next;
			}
			System.out.println();
		}
	}
	public static node merge(node head, node head2){
		if( head != null && head2 == null ){
			return head;
		}else if( head == null && head2 != null ){
			return head2;
		} else if (head2 != null && head != null) {
			node h1 = head, h2 = head2;
			while (h1 != null && h2 != null) {
				if (h1.data > h2.data) {
					node cur = h1.next;

				}
				h1 = h1.next;
				h2 = h2.next;
			}
		}
		return head;
	}
	public static void main(String[] args) {
		
	}
}