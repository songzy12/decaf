package decaf.error;

import decaf.Location;

public class BadSwitchError extends DecafError {
	
	private String given;
	
	public BadSwitchError(Location location, String given) {
		super(location);
		this.given = given;
	}
	
	@Override
	protected String getErrMsg() {
		return "incompatible switch: " + given + " given,  int expected";
	}
	
}