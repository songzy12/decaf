package decaf.error;

import decaf.Location;

public class BadCaseError extends DecafError{
		
	public BadCaseError(Location location) {
		super(location);
	}
	
	@Override
	protected String getErrMsg() {
		return "incompatible case: int constant is expected";
	}	
}
