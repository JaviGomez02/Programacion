import java.util.Scanner;

public class Ejercicio3 {

	public static Scanner teclado=new Scanner(System.in);
	
	public static void main(String[] args) {

		String tecla;
		char sostenida='a';
		Boolean flag;
		
		tecla=leerCadena("Introduce una tecla");
		while (sostenida!='S' && sostenida!='N') { //Con este bucle nos aseguramos de que se introduzcan los valores correctos
			sostenida=leerCaracter("¿Es una tecla sostenida?(S/N)");
			if (sostenida!='S' && sostenida!='N') {
				System.out.println("Introduce S o N");
			}
		}
		
		switch (sostenida) { //Creamos un switch para obtener el boolean que utilizaremos en la funcion frecuencia
		case 'S':{
			flag=true;
			break;
		}
		default:
			flag=false;

			break;
			
		}
		System.out.println("La frecuencia de la tecla pulsada es " +frecuencia(tecla,flag));
}
		
			//Definimos funciones para leer los datos introducidos
	public static String leerCadena(String texto) {
		System.out.println(texto);
		return teclado.nextLine();
	}
	public static char leerCaracter(String texto) {
		System.out.println(texto);
		return teclado.nextLine().charAt(0);
	}
	
	public static Double frecuencia(String tecla, boolean flag) {//definimos una funcion para calcular la frecuencia
		Double resultado=0.0;
		if (tecla.equals("DO") || tecla.equals("do")) { //creamos varios if para cada caso
			resultado=523.25;
		}
		else if (tecla.equals("RE") || tecla.equals("re")) {
			resultado=587.33;
		}
		else if (tecla.equals("MI") || tecla.equals("mi")) {
			resultado=659.26;
		}
		else if (tecla.equals("FA") || tecla.equals("fa")) {
			resultado=698.46;
		}
		else if (tecla.equals("SOL") || tecla.equals("sol")) {
			resultado=783.99;
		}
		else if (tecla.equals("LA") || tecla.equals("la")) {
			resultado=880.00;
		}
		else if (tecla.equals("SI") || tecla.equals("si")) {
			resultado=987.77;
		}
		if (flag==true) { //aqui utilizaremos la bandera que hemos obtenido anteriormente con el switch
			resultado=resultado*1.03;
		}
		return resultado;
	}
	
}
