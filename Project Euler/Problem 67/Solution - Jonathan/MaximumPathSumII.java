import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class MaximumPathSumII {
	public static String path = "";
	public static void setPath(String thePath){ path = thePath;}
	public static void main(String[] args){
		runProblem("/problem67.txt");
	}
	
	public static void runProblem(String fileName){
		setPath(System.getProperty("user.dir"));
		String numbersToSum = null;
		try {
			numbersToSum = readFileIntoString(fileName);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		long value = 0;
		//value = MaximumPathSumI.maximumPathSum_WAY1(numbersToSum);
		//System.out.println(value);
		//value = MaximumPathSumI.maximumPathSum_WAY2(numbersToSum);
		//System.out.println(value);
		value = MaximumPathSumI.maximumPathSum_WAY3(numbersToSum);
		System.out.println(value);
	}	
	
	
	public static List<String> readFileIntoStringList(String fileName) throws IOException{
		List<String> finalList = new ArrayList<String>();
		BufferedReader reader = new BufferedReader(new FileReader(path+fileName));
		String line;
		while ((line = reader.readLine()) != null) {
			finalList.add(line);
		}
		reader.close();
		
		return finalList;
	}public static String readFileIntoString(String fileName) throws IOException{
		String finalString = "";
		BufferedReader reader = new BufferedReader(new FileReader(path+fileName));
		String line;
		while ((line = reader.readLine()) != null) {
			finalString+=line+"\n";
		}
		reader.close();
		
		return finalString.substring(0, finalString.length()-1);
	}

	public static long maximumPathSum_WAY3(String pyramidString) {
		String[] pyramidRows = pyramidString.split("\n");
		List<HashMap<String, DualNumberObject>> path = new ArrayList<HashMap<String,DualNumberObject>>();
		_maximumPathSum(pyramidRows, path);		
//		List<Integer> finalPath = new ArrayList<Integer>();
		Integer pathLength = Integer.parseInt(path.get(path.size() - 1).keySet().toArray()[0].toString());
//		_getPath(path, pathLength, finalPath);
		
		return pathLength;
	}private static void _getPath(List<HashMap<String, DualNumberObject>> path,
			Integer pathLength, List<Integer> finalPath) {
		DualNumberObject pathNumber = path.get(path.size()-1).get(pathLength+"");
		if(path.size() <= 1){
			finalPath.add((Integer)pathNumber.n1);
			finalPath.add((Integer)pathNumber.n2);
			return;
		}
		finalPath.add((Integer) pathNumber.n1); 
		path.remove(path.size()-1);
		_getPath(path, (Integer) pathNumber.n2, finalPath);
	}
	public static class DualNumberObject{
		Number n1, n2;
		public DualNumberObject(Number n1, Number n2){this.n1 = n1; this.n2 = n2;}
		@Override
		public String toString(){
			return n1+" "+n2;
		}
	}
	
	private static void _maximumPathSum(String[] pyramidRows, List<HashMap<String, DualNumberObject>> path) {
		if(pyramidRows.length == 1) return;
		String[] lastRow = pyramidRows[pyramidRows.length-1].split(" "), secondToLastRow = pyramidRows[pyramidRows.length-2].split(" ");
		String newRow = "";
		HashMap<String, DualNumberObject> info = new HashMap<String, DualNumberObject>();
		for(int i = 0; i<lastRow.length - 1; i++){
			int left = Integer.parseInt(lastRow[i]), right = Integer.parseInt(lastRow[i+1]);
			int compareTo = Integer.parseInt(secondToLastRow[i]);
			int bigger = left > right ? left : right;
			newRow+=(compareTo+bigger)+" ";	
			info.put((compareTo+bigger)+"", new DualNumberObject(compareTo, bigger));
		} path.add(info);
		String[] newPyramidRows = new String[pyramidRows.length - 1];
		for(int i = 0; i<newPyramidRows.length - 1; i++){
			newPyramidRows[i] = pyramidRows[i];
		}
		newPyramidRows[newPyramidRows.length - 1] = newRow;
		_maximumPathSum(newPyramidRows, path);
	}

	public static long maximumPathSum_WAY2(String pyramidString) {
		String[] pyramidRows = pyramidString.split("\n");
		int[][] pyramidGrid = new int[pyramidRows.length][];
		for(int i = 0; i<pyramidRows.length; i++){
			pyramidGrid[i] = new int[pyramidRows[i].split(" ").length];
			for(int j = 0; j<pyramidRows[i].split(" ").length; j++)
				pyramidGrid[i][j] = Integer.parseInt(pyramidRows[i].split(" ")[j]);
		}
		int totalPaths = (int) Math.pow(2, pyramidRows.length);
		int largestSum = 0, tempSum, index;
		for(int i = 0; i<=totalPaths; i++){
			tempSum = pyramidGrid[0][0]; index = 0;
			for(int j = 0; j<pyramidGrid.length - 1; j++){
				index+=(i>>j&1); 
				tempSum+=pyramidGrid[j+1][index];
			}
			largestSum = tempSum > largestSum ? tempSum : largestSum;
		}
		return largestSum;
	}

	public static class Node<T>{
		List<Node<T>> parent, children;
		T info;
		public Node(){ init(); }
		public Node(T info){ init(); this.info = info; }
		private void init(){
			parent = new ArrayList<Node<T>>();
			children = new ArrayList<Node<T>>();
		}
		@Override
		public String toString(){
			return info.toString();
		}
	}
	
	public static class Problem18Object{
		int value, xLocation, yLocation, totalPath;
		public Problem18Object(int value, int xLocation, int yLocation, int totalPath){
			this.value = value; this.xLocation = xLocation; this.yLocation = yLocation; this.totalPath = totalPath;
		}
		@Override
		public String toString(){
			return "value: "+value+" , xLocation: "+xLocation+" , yLocation: "+yLocation+" , totalPath: "+totalPath;
		}
	}
	private static long maximumPathSum_WAY1(String pyramidString) {
		// I want the biggest sum of a path
		//if i pick 0,0 then next is either 1,0 or 1,1 if i pick 1,0 next is either 2,0 or 2,1 if i picked 1,1 next would be 2,1 or 2,2
		//use a shortest path algorithm in reverse for this
		//start with top number options are left or right
		//a tree data structure is best
//		List<List<String>> pyramidGrid = new ArrayList<List<String>>();
		int yLocation = 0;
		int value = Integer.parseInt(""+pyramidString.split("\n")[0]);
		Node<Problem18Object> start = new Node<Problem18Object>(new Problem18Object(value, 0, yLocation++,value));
		String[] yAxis = pyramidString.split("\n");
		_addChildren(start,yAxis,yLocation);
		
		List<Node> leaves = getAllLeaves(start);
		
		long pathLength = 0;
		for(Node i : leaves)
			pathLength = (Long) ((((Problem18Object)i.info).totalPath > pathLength)?((Problem18Object)i.info).totalPath:pathLength);
		return pathLength;
	}private static List<Node> getAllLeaves(Node<Problem18Object> root) {
		List<Node> leaves = new ArrayList<Node>();
		_getAllLeaves(root, leaves);
		return leaves;
	}private static void _getAllLeaves(Node<Problem18Object> node, List<Node> leaves) {
		if(node.children.isEmpty()){
			leaves.add(node);
		}else{
			for(Node<Problem18Object> child : node.children){
				_getAllLeaves(child, leaves);
			}
		}
	}
	private static void _addChildren(Node<Problem18Object> node, String[] yAxis, int yLocation) {
		if(yLocation >= yAxis.length) return;
		
		Problem18Object nodeInfo = (Problem18Object) node.info;
		String[] xAxis = yAxis[yLocation].split(" ");
		int child2Location = nodeInfo.xLocation + 1;
		if(xAxis.length < child2Location){
			child2Location-=2;
		}
		int tempChild1Value = Integer.parseInt(xAxis[nodeInfo.xLocation]), tempChild2Value = Integer.parseInt(xAxis[child2Location]);
		
		Node<Problem18Object> tempChild1 = new Node<Problem18Object>(new Problem18Object(tempChild1Value, nodeInfo.xLocation, yLocation, nodeInfo.totalPath+tempChild1Value));
		Node<Problem18Object> tempChild2 = new Node<Problem18Object>(new Problem18Object(tempChild2Value, child2Location, yLocation, nodeInfo.totalPath+tempChild2Value));
		tempChild1.parent.add(node);
		tempChild2.parent.add(node);
		node.children.add(tempChild2);
		node.children.add(tempChild1);
		yLocation++;
		
		_addChildren(tempChild1, yAxis, yLocation);
		_addChildren(tempChild2, yAxis, yLocation);
	}


}
