
public class Ejercicio4 {

	public static void main(String[] args) {
		// Transforma esta estructura en un bucle for:

		int num = 4, a = 3;
		do{
			a+=num;
			num++;
		}while(num > 15);
		System.out.println(a);

		
		//Podemos observar que en el bucle anterior se realiza la operacion a+=num una vez, pero como num=0 el resultado de a es 3
		
		//Le damos un valor mayor de 15 a num (en este caso le he dado 20).
		//Así que se mete en el bucle, llega al if donde num obtiene el valor de 0,
		//por lo que realizara la instruccion a+=num (donde da que a=3) y se
		//sale del bucle ya que num es menor de 15
		for (num=20; num > 15; num++) {
			if (num==20) {
				num=0;
			}
			a+=num;
		}
		System.out.println(a);
	}

}
