import java.util.Scanner;

public class teste {

	public static void main(String[] args) {
		Scanner teclado;
		teclado = new Scanner(System.in);

		System.out.println("Digite dois valores: ");

		int a = teclado.nextInt();
		int b = teclado.nextInt();

		System.out.println("valor antes de a: " + a + " valor b: " + b);

		teste troca = new teste();
		troca.trocaSemAux(a, b);
	}

	public void trocaSemAux(int a, int b) {
		a = a + b;
		b = a - b;
		a = a - b;
		System.out.println("valor de a: " + a + " valor de b: " + b);
	}

}
