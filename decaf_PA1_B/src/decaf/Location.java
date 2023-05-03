package decaf;

/**
 * 璇硶绗﹀彿鍦ㄦ簮浠ｇ爜涓殑浣嶇疆<br>
 */
public class Location implements Comparable<Location> {

	public static final Location NO_LOCATION = new Location(-1, -1);
	/**
	 * 璇ョ鍙风涓�涓瓧绗︽墍鍦ㄧ殑琛屽彿
	 */
	private int line;

	/**
	 * 璇ョ鍙风涓�涓瓧绗︽墍鍦ㄧ殑鍒楀彿
	 */
	private int column;

	/**
	 * 鏋勯�犱竴涓綅缃褰�
	 * 
	 * @param lin
	 *            琛屽彿
	 * @param col
	 *            鍒楀彿
	 */
	public Location(int lin, int col) {
		line = lin;
		column = col;
	}

	/**
	 * 杞崲鎴�(x,y)褰㈠紡鐨勫瓧绗︿覆
	 */
	@Override
	public String toString() {
		return "(" + line + "," + column + ")";
	}

	public int compareTo(Location o) {
		if (line > o.line) {
			return 1;
		}
		if (line < o.line) {
			return -1;
		}
		if (column > o.column) {
			return 1;
		}
		if (column < o.column) {
			return -1;
		}
		return 0;
	}
}
