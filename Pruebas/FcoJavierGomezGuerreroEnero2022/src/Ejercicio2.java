import java.util.Scanner;

public class Ejercicio2 {

	public static Scanner teclado=new Scanner (System.in);

	public static void main(String[] args) {
		int ano;
		String fecha;
		ano=leerEntero("Introduce el año actual");
		fecha=leerCadena("Introduce tu fecha de nacimiento (dd/mm/yyyy)");
		
		System.out.println("Tu FCM es de: "+FCM(ano,fecha));

	}

	public static String leerCadena(String texto) {
		System.out.println(texto);
		return teclado.nextLine();
	}
	public static int leerEntero(String texto) {
		System.out.println(texto);
		return Integer.parseInt(teclado.nextLine());
	}
	//Con el metodo FCM calculamos la frecuencia
	public static Double FCM(int ano, String fecha) {
		String cadena;
		Double frecuencia;
		int edad;
		cadena=fecha.substring(6); //Con la funcion substring lo que hacemos es coger los valores de la cadena fecha desde el 6 hacia delante, por lo que solo cogemos el año de nacimiento
		edad=ano-Integer.parseInt(cadena); //para calcular al edad debemos pasar a entero la cadena que contiene el año de nacimiento
		frecuencia=(double) (220-edad); //ponemos (double) al principio de la operacion para que el tipo sea Real
		return frecuencia;
		
		
	}
}
