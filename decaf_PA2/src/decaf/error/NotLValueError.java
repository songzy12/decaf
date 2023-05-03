package decaf.error;

import decaf.Location;

public class NotLValueError extends DecafError {

	private String op;

	public NotLValueError(Location location, String op) {
		super(location);
		this.op = op;
	}

	@Override
	protected String getErrMsg() {
		return "lvalue required as " + op + " operand";
	}
}
