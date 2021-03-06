import java.util.Scanner;

public class Ejercicio1 {

	public static Scanner teclado=new Scanner (System.in);

	public static void main(String[] args) {
		int entradas=1; //le damos un valor diferente a 0 a la variable para que entre en el bucle
		char dia,tarjeta;
		double precio;
		
		while (entradas!=0) { //este bucle se estará ejecutando hasta que entradas=0
			dia=' ';
			tarjeta=' ';//le damos valores cualquiera a las variables dia y tarjeta para que entre a los bucles posteriores
			precio=0.0;//le damos el valor 0 a precio para que se reinicie cada vez que se repita el bucle
			entradas=leerEntero("Introduce el numero de entradas");
			if (entradas!=0) { //Con este if ejecutaremos todo el programa.
				while (dia!='L' && dia!='M' && dia!='X' && dia!='J' && dia!='V' && dia!='S' && dia!='D') { //Este while nos sirve para asegurarnos de que se introduzcan los datos que queremos
					dia=leerCaracter("Introduce el dia de la semana (L,M,X,J,V,S,D)");
					if (dia!='L' && dia!='M' && dia!='X' && dia!='J' && dia!='V' && dia!='S' && dia!='D') {
						System.out.println("Introduce un dia correcto");
					}
				}
				while (tarjeta!='S' && tarjeta!='N') { //Al igual que el bucle anterior, este while es para obtener los datos correctos
					tarjeta=leerCaracter("¿Tienes la tarjeta CineJacaranda? S/N");
					if (tarjeta!='S' && tarjeta!='N') {
						System.out.println("Introduce S o N");
					}
				}
				switch (dia) { //Switch para calcular el precio en funcion del dia elejido
				case 'M':
				case 'V':
				case 'S':
				case 'D':
				case 'L': {
					for (int i = 0; i < entradas; i++) {//calculamos el precio con un bucle for
						precio=precio+8;
					}
					break;
					
				}
				case 'X':{
					for (int i = 0; i < entradas; i++) {
						precio=precio+5;
					}
					break;
				}
				case 'J':{
					if (entradas>1) {
						if (entradas%2==0) {//en el caso de que las entradas sean pares se entra en este if
							for (int i = 0; i < entradas; i=i+2) {
								precio=precio+11;
							}
						}
						else {
							for (int i = 1; i < entradas; i=i+2) {
								precio=precio+11;
							}
							precio=precio+8;
						}
					}
					else {
						precio=8;
					}
					break;
				}
				default:
					System.out.println("Introduce un valor correcto");
				}
				
				switch (tarjeta) { //switch en el que le aplicaremos el descuento del 10% si el usuario ha marcado que tiene la tarjeta Jacaranda
				case 'S': {
					precio=precio-(precio*0.1);
					break;
				}
				case 'N':{
					break;
				}
				default:
					System.out.println("Introduce valores correctos");
					break;
				}
				System.out.println("El precio total es de "+precio+" euros");
			}
			else { //Este else funciona al haber introducido 0 en entradas
				System.out.println("Apagando programa");
			}
			
			
		}
		
		
		
	}
//Definimos varios metodos para leer los datos introducidos
	public static String leerCadena(String texto) {
		System.out.println(texto);
		return teclado.nextLine();
	}
	public static int leerEntero(String texto) {
		System.out.println(texto);
		return Integer.parseInt(teclado.nextLine());
	}
	public static char leerCaracter(String texto) {
		System.out.println(texto);
		return teclado.nextLine().charAt(0);
	}
}
