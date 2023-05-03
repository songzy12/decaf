package decaf.error;

import decaf.Location;

public class CondTypeError extends DecafError {

	private String type1;

	private String type2;

	public CondTypeError(Location location, String type1, String type2) {
		super(location);
		this.type1 = type1;
		this.type2 = type2;
	}

	@Override
	protected String getErrMsg() {
		return "operands to ?:  have different types " + type1 +
			" and " + type2;
	}
}
