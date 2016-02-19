import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CoinSums {
//	In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
//
//		1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
//		It is possible to make £2 in the following way:
//
//		1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
//		How many different ways can £2 be made using any number of coins?
//	
	public static void main(String[] args){
		runProblem(200);
	}
	
	public static void runProblem(int max) {
		String value = "";
		value = CoinSums.waysToMakeCoin(Coin.TwoPound);
		System.out.println(value);
		value = CoinSums.bruteForce();
		System.out.println(value);
		value = CoinSums.dynamicProgramming();
		System.out.println(value);
	}
	public static class Coin{
		public static int OnePence = 1, TwoPence = 2, FivePence = 5, TenPence = 10, TwentyPence = 20, FiftyPence = 50, OnePound = 100, TwoPound = 200;
		public static Integer[] coinDenominations = {1,2,5,10,20,50,100,200};
	}
	

	public static String dynamicProgramming(){
		int target = 200;
		int[] coinSizes = { 1, 2, 5, 10, 20, 50, 100, 200 };
		int[] ways = new int[target+1];
		ways[0] = 1;
		 
		for (int i = 0; i < coinSizes.length; i++) {
		    for (int j = coinSizes[i]; j <= target; j++) {
		        ways[j] += ways[j - coinSizes[i]];
		    }
		}
		return ways[ways.length-1]+"";
	}
	
	public static String bruteForce(){
		int target  = 200;
		int ways = 0;
		 
		for (int a = target; a >= 0; a -= 200) {
		    for (int b = a; b >= 0; b -= 100) {
		        for (int c = b; c >= 0; c -= 50) {
		            for (int d = c; d >= 0; d -= 20) {
		                for (int e = d; e >= 0; e -= 10) {
		                    for (int f = e; f >= 0; f -= 5) {
		                        for (int g = f; g >= 0; g -= 2) {
		                            ways++;
		                        }
		                    }
		                }
		            }
		        }
		    }
		}
		return ways+"";
	}
	
	public static int totalCount = 0;
	public static String waysToMakeCoin(int coin){
		//permute a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 + h*200 = 200;
		// 200-1*1 = b*2 + c*5 + d*10 + e*20 + f*50 + g*100 + h*200
		_coinPermuter(coin, Arrays.asList(Coin.coinDenominations), new ArrayList<String>());
		
		return totalCount+"";
	}private static void _coinPermuter(int coin, List<Integer> asList, List<String> values) {
		if(asList.isEmpty())
			return;
		int coinValue = asList.get(asList.size()-1);
		for(int i = 0; i<=coin/coinValue; i++){
			if(coin-i*coinValue <= 0){
				if(coin-i*coinValue == 0){
//					String totalValues = ""; int k = 0;
//					for(String s : values)
//						totalValues+=s+"+";
//					System.out.println(totalValues+i+"*"+coinValue);
					totalCount++;
				}
				continue;
			}
			List<String> newValues = new ArrayList<>(values); newValues.add(i+"*"+coinValue);
			_coinPermuter(coin-i*coinValue, asList.subList(0, asList.size()-1), newValues);
		}
		
	}
}
