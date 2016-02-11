import static java.lang.System.out;
import static java.lang.System.*;
import java.math.BigInteger;

public class chocolates {
	public static void main(String[] args) {
		if (args != null) {
			if (args.length > 1) {
				BigInteger m = new BigInteger(args[0]), n = new BigInteger(args[1]);
				System.out.println(chocCut(m, n));
			}
		}
	}
	public static BigInteger chocCut(BigInteger n, BigInteger m) {
		return m.add(n).subtract(gcd(m,n));
	}
	public static BigInteger gcd(BigInteger a, BigInteger b){
		return b.equals(BigInteger.ZERO)?a:gcd(b,a.mod(b));
	}
}