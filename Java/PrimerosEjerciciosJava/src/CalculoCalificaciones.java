import java.util.Scanner;

public class CalculoCalificaciones {

	public static Scanner teclado= new Scanner(System.in);
	
	public static void main(String[] args) {
		int practica,problemas,teorica;
		float total;
		
		System.out.println("Introduce la calificacion de la parte practica");
		practica=Integer.parseInt(teclado.nextLine());
		
		System.out.println("Introduce la calificacion de la parte de problemas");
		problemas=Integer.parseInt(teclado.nextLine());
		
		System.out.println("Introduce la calificacion de la parte teorica");
		teorica=Integer.parseInt(teclado.nextLine());
		
		if (practica<0 || practica>10 || problemas<0 || problemas>10 || teorica<0 || teorica>10) {
			
			System.out.println("Tienes que introducir notas del 0 al 10");
		}
		else {
			total=(float) (practica*0.1)+ (float) (problemas*0.5)+ (float) (teorica*0.4);
			if (total<5) {
				System.out.println("Insuficiente");
			}
			else if (total>=5 && total<6) {
				System.out.println("Suficiente");
			}
			else if (total<7) {
				System.out.println("Bien");
			}
			else if (total<9) {
				System.out.println("Notable");
			}
			else if (total<=10) {
				System.out.println("Sobresaliente");
			}
			
			System.out.println("La nota final es: "+total);
		}
		
	}

}
