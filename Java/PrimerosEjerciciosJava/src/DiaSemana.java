import java.util.Scanner;

public class DiaSemana {

	public static Scanner teclado= new Scanner(System.in);
	
	public static void main(String[] args) {
		
		char opcion;
		System.out.println("Introduce un dia de la semana: L,M,X,J,V");
		opcion=teclado.nextLine().charAt(0);
		
		switch (opcion) {
		case 'L': {
			System.out.println("A primera hora toca entornos");
			break;		
		}
		case 'M':
		case 'V': {
			System.out.println("A primera hora toca programacion");
			break;		
		}
		case 'X': {
			System.out.println("A primera hora toca FOL");
			break;		
		}
		case 'J': {
			System.out.println("A primera hora toca sistemas informaticos");
			break;		
		}
		default:
			System.out.println("Introduce un dia correcto");
		}
	}

}
