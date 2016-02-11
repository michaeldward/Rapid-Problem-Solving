import static java.lang.System.out;
import static java.lang.System.*;

public class chocolates {
	public static void main(String[] args) {
		if (args != null) {
			if (args.length > 1) {
				System.out.println(chocBreak(Long.parseLong(args[0]), Long.parseLong(args[1])));
			}
		}
	}
	public static long chocBreak(long n, long m){ //m is horizontal, n is vertical
		return (n-1) * m + m - 1;
	}
}