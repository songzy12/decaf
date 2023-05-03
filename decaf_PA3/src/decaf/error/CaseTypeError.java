package decaf.error;

import decaf.Location;

public class CaseTypeError extends DecafError{
		
	public CaseTypeError(Location location) {
		super(location);
	}
	
	@Override
	protected String getErrMsg() {
		return "incompatible case: int constant is expected";
	}	
}
